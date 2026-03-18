/**
 * Számla toolok: invoiceAdd, invoiceDetails, invoiceStorno, invoiceList, invoiceSetPaid
 */

import { McpServer } from "@modelcontextprotocol/sdk/server/mcp.js";
import { z } from "zod";
import { OnlineSzamlazoClient } from "../client.js";
import { SessionCache } from "../cache.js";

const invoiceElementSchema = z.object({
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
    .describe("Kedvezmény nettó értéke"),
});

export function registerInvoiceTools(
  server: McpServer,
  client: OnlineSzamlazoClient,
  cache: SessionCache
) {
  server.tool(
    "invoice_add",
    "Azonnali, végleges számla létrehozása. Tételekhez product_sid szükséges (product_list-ből). Ha a felhasználó számlázni szeretne, használd az invoice_wizard prompt-ot a lépésenkénti végigvezetéshez!",
    {
      customer_sid: z
        .string()
        .describe(
          "Ügyfél SID (customer_add-ból vagy customer_list-ből)"
        ),
      elements: z
        .array(invoiceElementSchema)
        .min(1)
        .describe("Számla tételek (legalább 1 kötelező)"),
      payment_mode_id: z
        .number()
        .describe(
          "Fizetési mód ID (payment_mode_list-ből)"
        ),
      trade_date: z
        .string()
        .optional()
        .describe("Teljesítés dátuma (YYYY-MM-DD, default: mai nap)"),
      print_date: z
        .string()
        .optional()
        .describe("Kiállítás dátuma (YYYY-MM-DD, default: mai nap)"),
      pay_date: z
        .string()
        .describe("Fizetési határidő (YYYY-MM-DD)"),
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
      prepayment: z
        .number()
        .optional()
        .describe("0=normál számla, 1=előleg számla (default: 0)"),
      order_number: z
        .string()
        .optional()
        .describe("Külső megrendelési azonosító (generálódik ha üres)"),
      comment: z.string().optional().describe("Megjegyzés a számlára"),
      lang: z
        .string()
        .optional()
        .describe("Számla nyelve (ha eltér a számlatömb nyelvétől)"),
      other: z
        .string()
        .optional()
        .describe("JSON formátumban további meta adatok"),
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
        prepayment: params.prepayment ?? 0,
      };
      const result = await client.call("invoiceAdd", apiParams);
      cache.invalidatePrefix("invoices:");
      return {
        content: [{ type: "text", text: JSON.stringify(result, null, 2) }],
      };
    }
  );

  server.tool(
    "invoice_details",
    "Számla részletes adatainak lekérdezése számlaszám alapján. Cache-elt.",
    {
      invoice_number: z.string().describe("Számlaszám"),
      block: z.string().optional().describe("Számlatömb neve"),
    },
    async (params) => {
      const cacheKey = `invoice:${params.invoice_number}`;
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

      const result = await client.call("invoiceDetails", params);
      cache.set(cacheKey, result, 30);
      return {
        content: [{ type: "text", text: JSON.stringify(result, null, 2) }],
      };
    }
  );

  server.tool(
    "invoice_storno",
    "Számla sztornózása (érvénytelenítés). Sztornó számlát hoz létre.",
    {
      invoice_number: z.string().describe("Sztornózandó számlaszám"),
      storno_reason: z.string().optional().describe("Sztornó ok kódja"),
      admin_comment: z.string().optional().describe("Admin megjegyzés"),
      comment: z.string().optional().describe("Nyilvános megjegyzés"),
      refund: z
        .number()
        .optional()
        .describe("Visszatérítés jelölés (1=igen, 0=nem)"),
      block: z.string().optional().describe("Számlatömb neve"),
    },
    async (params) => {
      const result = await client.call("invoiceStorno", params);
      // Sztornózott számla cache invalidálás
      cache.invalidate(`invoice:${params.invoice_number}`);
      cache.invalidatePrefix("invoices:");
      return {
        content: [{ type: "text", text: JSON.stringify(result, null, 2) }],
      };
    }
  );

  server.tool(
    "invoice_list",
    "Számlák listázása szűréssel (dátum, ügyfél, fizetettség, stb.). Cache-elt.",
    {
      date_from: z.string().optional().describe("Dátumtól (YYYY-MM-DD)"),
      date_to: z.string().optional().describe("Dátumig (YYYY-MM-DD)"),
      customer_sid: z.string().optional().describe("Ügyfél SID szűrő"),
      paid: z.number().optional().describe("Fizetettség szűrő (0/1)"),
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
      const cacheKey = `invoices:${JSON.stringify(apiParams)}`;

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

      const result = await client.call("invoiceList", apiParams);
      cache.set(cacheKey, result, 5); // 5 perc — számlák gyakrabban változnak
      return {
        content: [{ type: "text", text: JSON.stringify(result, null, 2) }],
      };
    }
  );

  server.tool(
    "invoice_set_paid",
    "Számla fizetettnek jelölése",
    {
      invoice_number: z.string().describe("Számlaszám"),
      paid: z.number().describe("1=fizetett, 0=nem fizetett"),
      payment_date: z
        .string()
        .optional()
        .describe("Fizetés dátuma (YYYY-MM-DD)"),
      block: z.string().optional().describe("Számlatömb neve"),
    },
    async (params) => {
      const result = await client.call("invoiceSetPaid", params);
      // Fizetettség változott — cache invalidálás
      cache.invalidate(`invoice:${params.invoice_number}`);
      cache.invalidatePrefix("invoices:");
      return {
        content: [{ type: "text", text: JSON.stringify(result, null, 2) }],
      };
    }
  );

  server.tool(
    "invoice_download",
    "Számla PDF letöltése (base64 kódolt PDF)",
    {
      invoice_number: z.string().describe("Számlaszám"),
      block: z.string().optional().describe("Számlatömb neve"),
    },
    async (params) => {
      const result = await client.call("invoiceDownload", params);
      return {
        content: [{ type: "text", text: JSON.stringify(result, null, 2) }],
      };
    }
  );
}
