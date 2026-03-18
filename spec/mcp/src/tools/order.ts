/**
 * Order toolok: orderAdd, orderDetails, orderList, orderStorno, orderBill,
 * orderSetPaid, orderCheckPaid, orderPaidChangeList, orderProformDownload,
 * orderCollectiveAdd, orderCollectiveAddElements, orderCollectiveClose, orderCollectiveSettling
 */

import { McpServer } from "@modelcontextprotocol/sdk/server/mcp.js";
import { z } from "zod";
import { OnlineSzamlazoClient } from "../client.js";
import { SessionCache } from "../cache.js";

const orderElementSchema = z.object({
  product_sid: z.string().describe("Termék/szolgáltatás SID azonosítója"),
  amount: z
    .number()
    .optional()
    .describe("Mennyiség (default: 1)"),
  quantity: z
    .string()
    .optional()
    .describe("Mennyiségi egység kód (default: PIECE, quantityList-ből)"),
  net_price_single: z
    .number()
    .optional()
    .describe("Nettó egységár (kötelező ha gross_price_single nincs megadva)"),
  gross_price_single: z
    .number()
    .optional()
    .describe("Bruttó egységár (kötelező ha net_price_single nincs megadva)"),
  tax_code: z
    .string()
    .optional()
    .describe("ÁFA kód (default: 27 — magyar 27%. Ország függő!)"),
  comment: z.string().optional().describe("Tétel megjegyzés"),
  other: z
    .string()
    .optional()
    .describe("JSON formátumban további meta adatok"),
  discount_type: z
    .string()
    .optional()
    .describe("Kedvezmény típusa: percent vagy value"),
  discount_value: z
    .number()
    .optional()
    .describe("Kedvezmény értéke (nettó)"),
});

export function registerOrderTools(
  server: McpServer,
  client: OnlineSzamlazoClient,
  cache: SessionCache
) {
  server.tool(
    "order_add",
    "Megrendelés/díjbekérő létrehozása. proform_order=1: díjbekérő (tervezett számla, automata számlázáshoz), proform_order=0: azonnali számla (mint invoiceAdd). Ismétlődő számlázáshoz regularity + regularities_date megadása szükséges.",
    {
      customer_sid: z
        .string()
        .describe("Ügyfél SID azonosító"),
      proform_order: z
        .number()
        .describe("1=díjbekérő (tervezett), 0=azonnali számla"),
      elements: z
        .array(orderElementSchema)
        .min(1)
        .describe("Megrendelés tételek"),
      payment_mode_id: z
        .number()
        .describe("Fizetési mód ID (payment_mode_list-ből)"),
      trade_date: z
        .string()
        .optional()
        .describe("Teljesítés dátuma (YYYY-MM-DD, default: mai nap)"),
      print_date: z
        .string()
        .optional()
        .describe("Kiállítás dátuma (YYYY-MM-DD, default: mai nap)"),
      pay_date: z.string().describe("Fizetési határidő (YYYY-MM-DD)"),
      order_date: z
        .string()
        .optional()
        .describe("Megrendelés dátuma (YYYY-MM-DD, default: mai nap)"),
      paid: z
        .number()
        .optional()
        .describe("Fizetési státusz: 0=nincs fizetve, 1=részben, 2=fizetve (default: 0)"),
      currency: z
        .string()
        .optional()
        .describe("Pénznem (3 karakter, nagybetű — default: HUF magyar ügyfélnél, EUR EU ügyfélnél)"),
      order_number: z
        .string()
        .optional()
        .describe("Külső megrendelési azonosító (generálódik ha üres)"),
      comment: z.string().optional().describe("Megjegyzés a számlára"),
      lang: z
        .string()
        .optional()
        .describe("Számla nyelve (ha eltér a számlatömb nyelvétől)"),
      regularity: z
        .string()
        .optional()
        .describe(
          "Ismétlődés kód (regularityDownload-ból, pl. MONTHLY, YEARLY)"
        ),
      regularities_id: z
        .number()
        .optional()
        .describe("Ismétlődés azonosító (regularity helyett)"),
      regularities_date: z
        .string()
        .optional()
        .describe("Következő számlázás dátuma (YYYY-MM-DD HH:MM:SS)"),
      other: z
        .string()
        .optional()
        .describe("JSON formátumban meta adatok"),
      block: z.string().optional().describe("Számlatömb neve"),
    },
    async (params) => {
      const today = new Date().toISOString().slice(0, 10);
      const elements = params.elements.map((el) => ({
        ...el,
        amount: el.amount ?? 1,
        quantity: el.quantity ?? "PIECE",
        tax_code: el.tax_code ?? "27",
      }));
      const apiParams = {
        ...params,
        elements,
        trade_date: params.trade_date ?? today,
        print_date: params.print_date ?? today,
        order_date: params.order_date ?? today,
        paid: params.paid ?? 0,
        currency: params.currency ?? "HUF",
      };
      const result = await client.call("orderAdd", apiParams);
      cache.invalidatePrefix("orders:");
      return {
        content: [{ type: "text", text: JSON.stringify(result, null, 2) }],
      };
    }
  );

  server.tool(
    "order_details",
    "Megrendelés részletes adatainak lekérdezése order_number alapján",
    {
      order_number: z.string().describe("Megrendelés azonosító"),
      block: z.string().optional().describe("Számlatömb neve"),
    },
    async (params) => {
      const cacheKey = `order:${params.order_number}`;
      const cached = cache.get<unknown>(cacheKey);
      if (cached) {
        return {
          content: [
            {
              type: "text",
              text: JSON.stringify(cached, null, 2) + "\n\n(cache-ből)",
            },
          ],
        };
      }

      const result = await client.call("orderDetails", params);
      cache.set(cacheKey, result, 10);
      return {
        content: [{ type: "text", text: JSON.stringify(result, null, 2) }],
      };
    }
  );

  server.tool(
    "order_list",
    "Megrendelések/díjbekérők listázása szűréssel. Csak tervezett megrendeléseket ad vissza, számlákat NEM (ahhoz invoice_list kell).",
    {
      from: z
        .string()
        .optional()
        .describe("Teljesítési dátumtól (YYYY-MM-DD)"),
      to: z
        .string()
        .optional()
        .describe("Teljesítési dátumig (YYYY-MM-DD)"),
      customer_sid: z.string().optional().describe("Ügyfél SID szűrő"),
      regularity: z
        .string()
        .optional()
        .describe("Ismétlődés kód szűrő"),
      regularities_id: z
        .number()
        .optional()
        .describe("Ismétlődés ID szűrő"),
      limit: z
        .number()
        .optional()
        .describe("Oldalméret (alapértelmezett: 10)"),
      page: z.number().optional().describe("Oldalszám"),
      block: z.string().optional().describe("Számlatömb neve"),
      refresh: z.boolean().optional().describe("true = cache frissítése"),
    },
    async (params) => {
      const { refresh, ...apiParams } = params;
      const cacheKey = `orders:${JSON.stringify(apiParams)}`;

      if (!refresh) {
        const cached = cache.get<unknown>(cacheKey);
        if (cached) {
          return {
            content: [
              {
                type: "text",
                text: JSON.stringify(cached, null, 2) + "\n\n(cache-ből)",
              },
            ],
          };
        }
      }

      const result = await client.call("orderList", apiParams);
      cache.set(cacheKey, result, 5);
      return {
        content: [{ type: "text", text: JSON.stringify(result, null, 2) }],
      };
    }
  );

  server.tool(
    "order_storno",
    "Megrendelés sztornózása/törlése. Ha nincs hozzá számla: törlés (1005). Ha van számla: sztornó számla keletkezik (1000).",
    {
      order_number: z.string().describe("Megrendelés azonosító"),
      storno_reason: z
        .string()
        .optional()
        .describe(
          "Sztornó ok: ORDER_STORNO_CUSTOMER_CANCEL, ORDER_STORNO_PAYMENT_DATE_EPIRED, ORDER_STORNO_UNFULFILLABLE_ORDER, ORDER_STORNO_MULTIPLE_OR_WRONG_INVOICING, ORDER_STORNO_WRONG_PAYMENT"
        ),
      admin_comment: z.string().optional().describe("Admin megjegyzés"),
      comment: z.string().optional().describe("Sztornó számla megjegyzés"),
      refund: z
        .number()
        .optional()
        .describe("Visszatérítés: 0=nincs, 1=teljes"),
      block: z.string().optional().describe("Számlatömb neve"),
    },
    async (params) => {
      const result = await client.call("orderStorno", params);
      cache.invalidate(`order:${params.order_number}`);
      cache.invalidatePrefix("orders:");
      return {
        content: [{ type: "text", text: JSON.stringify(result, null, 2) }],
      };
    }
  );

  server.tool(
    "order_bill",
    "Meglévő megrendelés/díjbekérő kiszámlázása. Számlát generál a megrendelésből.",
    {
      order_number: z.string().describe("Megrendelés azonosító"),
      paid: z
        .number()
        .describe("Fizetési státusz: 0=nincs fizetve, 1=részben, 2=fizetve"),
      payment_mode_id: z
        .number()
        .optional()
        .describe("Fizetési mód ID (opcionális, felülírja az eredetit)"),
      block: z.string().optional().describe("Számlatömb neve"),
    },
    async (params) => {
      const result = await client.call("orderBill", params);
      cache.invalidate(`order:${params.order_number}`);
      cache.invalidatePrefix("orders:");
      cache.invalidatePrefix("invoices:");
      return {
        content: [{ type: "text", text: JSON.stringify(result, null, 2) }],
      };
    }
  );

  server.tool(
    "order_set_paid",
    "Megrendelés fizetett státuszának beállítása",
    {
      order_number: z.string().describe("Megrendelés azonosító"),
      block: z.string().optional().describe("Számlatömb neve"),
    },
    async (params) => {
      const result = await client.call("orderSetPaid", params);
      cache.invalidate(`order:${params.order_number}`);
      cache.invalidatePrefix("orders:");
      return {
        content: [{ type: "text", text: JSON.stringify(result, null, 2) }],
      };
    }
  );

  server.tool(
    "order_check_paid",
    "Megrendelés fizetési státuszának ellenőrzése",
    {
      order_number: z.string().describe("Megrendelés azonosító"),
      block: z.string().optional().describe("Számlatömb neve"),
    },
    async (params) => {
      const result = await client.call("orderCheckPaid", params);
      return {
        content: [{ type: "text", text: JSON.stringify(result, null, 2) }],
      };
    }
  );

  server.tool(
    "order_paid_change_list",
    "Fizetett státuszú díjbekérők listája, amelyekhez még nincs számla (banki párosítás után keletkezett fizetések)",
    {
      block: z.string().optional().describe("Számlatömb neve"),
    },
    async (params) => {
      const result = await client.call("orderPaidChangeList", params);
      return {
        content: [{ type: "text", text: JSON.stringify(result, null, 2) }],
      };
    }
  );

  server.tool(
    "order_proform_download",
    "Díjbekérő (proforma) PDF letöltése base64 kódolva",
    {
      order_number: z.string().describe("Megrendelés azonosító"),
      block: z.string().optional().describe("Számlatömb neve"),
    },
    async (params) => {
      const result = await client.call("orderProformDownload", params);
      return {
        content: [{ type: "text", text: JSON.stringify(result, null, 2) }],
      };
    }
  );

  // --- Gyűjtő díjbekérő (collective) ---

  server.tool(
    "order_collective_add",
    "Gyűjtő díjbekérő létrehozása. Több tétel gyűjthető egyetlen számlára. Automata számlázáshoz: regularity=ONCE_AUTOMATE + regularities_date.",
    {
      customer_sid: z.string().describe("Ügyfél SID azonosító"),
      elements: z
        .array(orderElementSchema)
        .min(1)
        .describe("Gyűjtő díjbekérő tételek"),
      payment_mode_id: z
        .number()
        .describe("Fizetési mód ID (payment_mode_list-ből)"),
      trade_date: z
        .string()
        .optional()
        .describe("Teljesítés dátuma (YYYY-MM-DD, default: mai nap)"),
      print_date: z
        .string()
        .optional()
        .describe("Kiállítás dátuma (YYYY-MM-DD, default: mai nap)"),
      pay_date: z.string().describe("Fizetési határidő (YYYY-MM-DD)"),
      order_date: z
        .string()
        .optional()
        .describe("Megrendelés dátuma (YYYY-MM-DD, default: mai nap)"),
      paid: z
        .number()
        .optional()
        .describe("Fizetési státusz: 0=nincs fizetve, 1=részben, 2=fizetve (default: 0)"),
      currency: z
        .string()
        .optional()
        .describe("Pénznem (3 karakter, nagybetű — default: HUF)"),
      order_number: z
        .string()
        .optional()
        .describe("Külső megrendelési azonosító"),
      comment: z.string().optional().describe("Megjegyzés"),
      lang: z.string().optional().describe("Számla nyelve"),
      regularity: z
        .string()
        .optional()
        .describe("Automata számlázáshoz: ONCE_AUTOMATE"),
      regularities_date: z
        .string()
        .optional()
        .describe("Automata számlázás időpontja (YYYY-MM-DD HH:MM:SS)"),
      block: z.string().optional().describe("Számlatömb neve"),
    },
    async (params) => {
      const today = new Date().toISOString().slice(0, 10);
      const elements = params.elements.map((el) => ({
        ...el,
        amount: el.amount ?? 1,
        quantity: el.quantity ?? "PIECE",
        tax_code: el.tax_code ?? "27",
      }));
      const apiParams = {
        ...params,
        elements,
        trade_date: params.trade_date ?? today,
        print_date: params.print_date ?? today,
        order_date: params.order_date ?? today,
        paid: params.paid ?? 0,
        currency: params.currency ?? "HUF",
      };
      const result = await client.call("orderCollectiveAdd", apiParams);
      cache.invalidatePrefix("orders:");
      return {
        content: [{ type: "text", text: JSON.stringify(result, null, 2) }],
      };
    }
  );

  server.tool(
    "order_collective_add_elements",
    "Tételek hozzáadása egy nyitott gyűjtő díjbekérőhöz (customer_sid azonosítja a nyitott collective-et)",
    {
      customer_sid: z
        .string()
        .describe("Ügyfél SID (akinek van nyitott collective-je)"),
      elements: z
        .array(orderElementSchema)
        .min(1)
        .describe("Hozzáadandó tételek"),
      block: z.string().optional().describe("Számlatömb neve"),
    },
    async (params) => {
      const elements = params.elements.map((el) => ({
        ...el,
        amount: el.amount ?? 1,
        quantity: el.quantity ?? "PIECE",
        tax_code: el.tax_code ?? "27",
      }));
      const result = await client.call(
        "orderCollectiveAddElements",
        { ...params, elements }
      );
      cache.invalidatePrefix("orders:");
      return {
        content: [{ type: "text", text: JSON.stringify(result, null, 2) }],
      };
    }
  );

  server.tool(
    "order_collective_close",
    "Gyűjtő díjbekérő lezárása és számlázása. A nyitott collective-et customer_sid alapján azonosítja.",
    {
      customer_sid: z
        .string()
        .describe("Ügyfél SID (akinek van nyitott collective-je)"),
      block: z.string().optional().describe("Számlatömb neve"),
    },
    async (params) => {
      const result = await client.call("orderCollectiveClose", params);
      cache.invalidatePrefix("orders:");
      cache.invalidatePrefix("invoices:");
      return {
        content: [{ type: "text", text: JSON.stringify(result, null, 2) }],
      };
    }
  );

  server.tool(
    "order_collective_settling",
    "Gyűjtő számla elszámolás lekérdezése — visszaadja a gyűjtőhöz tartozó tételeket",
    {
      order_number: z
        .string()
        .optional()
        .describe("Tervezett számla száma (order_number VAGY invoice_number kötelező)"),
      invoice_number: z
        .string()
        .optional()
        .describe("Számla száma (order_number VAGY invoice_number kötelező)"),
      block: z.string().optional().describe("Számlatömb neve"),
    },
    async (params) => {
      const result = await client.call(
        "orderCollectiveSettling",
        params
      );
      return {
        content: [{ type: "text", text: JSON.stringify(result, null, 2) }],
      };
    }
  );
}
