/**
 * Ügyfél toolok: customerAdd, customerList, customerModify, customerGet, customerActivate, customerInactivate
 */

import { McpServer } from "@modelcontextprotocol/sdk/server/mcp.js";
import { z } from "zod";
import { OnlineSzamlazoClient } from "../client.js";
import { SessionCache } from "../cache.js";

export function registerCustomerTools(
  server: McpServer,
  client: OnlineSzamlazoClient,
  cache: SessionCache
) {
  server.tool(
    "customer_add",
    "Új ügyfél/partner létrehozása a számlázó rendszerben",
    {
      name: z.string().describe("Ügyfél neve"),
      country: z.string().optional().describe("Országkód (pl. HU)"),
      postcode: z.string().optional().describe("Irányítószám"),
      city: z.string().optional().describe("Város"),
      street: z.string().optional().describe("Utca"),
      street_number: z.string().optional().describe("Házszám"),
      door: z.string().optional().describe("Ajtó"),
      phone: z.string().optional().describe("Telefon"),
      tax_number: z.string().optional().describe("Adószám"),
      eu_tax_number: z.string().optional().describe("EU adószám"),
      email: z.string().optional().describe("Email cím"),
      invoice_send: z
        .number()
        .optional()
        .describe("Számla küldés módja (0=nem küld, 1=email)"),
      comment: z.string().optional().describe("Megjegyzés"),
      bank: z.string().optional().describe("Bankszámlaszám"),
      bank_name: z.string().optional().describe("Bank neve"),
      lang: z.string().optional().describe("Nyelv (hu, en, de, stb.)"),
      sid: z
        .string()
        .optional()
        .describe("Egyedi azonosító (generálódik ha üres)"),
      firm_type: z
        .number()
        .optional()
        .describe("Típus: 1=beszállító, 2=vevő, 3=vevő és beszállító"),
      active: z
        .number()
        .optional()
        .describe("Aktív (1) / Inaktív (0), alapértelmezett: 1"),
      legal_status: z
        .string()
        .optional()
        .describe("Jogi státusz: CORPORATION (cég, default) vagy INDIVIDUAL (magánszemély)"),
      region: z.string().optional().describe("Régió (megye, tartomány)"),
      group_tax_number: z.string().optional().describe("Csoportos adószám"),
      other: z.string().optional().describe("JSON formátumban további meta adatok"),
      block: z
        .string()
        .optional()
        .describe("Számlatömb neve (opcionális, ha az alapértelmezett nem jó)"),
    },
    async (params) => {
      const result = await client.call("customerAdd", params);
      // Ügyfél lista cache invalidálás — új ügyfél hozzáadva
      cache.invalidatePrefix("customers:");
      return {
        content: [{ type: "text", text: JSON.stringify(result, null, 2) }],
      };
    }
  );

  server.tool(
    "customer_list",
    "Ügyfelek keresése és listázása. FONTOS: Ügyfél kereséséhez MINDIG használd a name vagy email paramétert! Ha a user egy konkrét ügyfelet keres név alapján, add meg a name paramétert. Részleges egyezésre is keres (LIKE). Cache-elt azonos szűrési feltételekkel.",
    {
      name: z.string().optional().describe("Keresés név alapján (részleges egyezés, LIKE). Ügyfél kereséséhez MINDIG add meg!"),
      email: z.string().optional().describe("Keresés email alapján (részleges egyezés, LIKE)"),
      sid: z.string().optional().describe("Keresés SID alapján (részleges egyezés, LIKE)"),
      firm_type: z
        .number()
        .optional()
        .describe("Típus szűrő (3=vevő, 4=szállító)"),
      limit: z
        .number()
        .optional()
        .describe("Oldalméret (alapértelmezett: 10, max: 1000)"),
      page: z.number().optional().describe("Oldalszám (alapértelmezett: 1)"),
      refresh: z.boolean().optional().describe("true = cache frissítése"),
    },
    async (params) => {
      const { refresh, ...apiParams } = params;
      const cacheKey = `customers:${JSON.stringify(apiParams)}`;

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

      const result = await client.call("customerList", apiParams, {
        skipBlock: true,
      });
      cache.set(cacheKey, result, 15); // 15 perc — ügyfelek változhatnak
      return {
        content: [{ type: "text", text: JSON.stringify(result, null, 2) }],
      };
    }
  );

  server.tool(
    "customer_get",
    "Egy ügyfél adatainak lekérdezése SID vagy adószám alapján. Ha nem ismered a SID-et, használd a customer_list-et név alapú kereséshez.",
    {
      sid: z.string().optional().describe("Ügyfél egyedi azonosítója (SID)"),
      tax_number: z.string().optional().describe("Adószám alapú keresés (ha SID nem ismert)"),
    },
    async (params) => {
      const cacheKey = `customer:${params.sid || params.tax_number}`;
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

      const result = await client.call("customerGet", params, {
        skipBlock: true,
      });
      cache.set(cacheKey, result, 15);
      return {
        content: [{ type: "text", text: JSON.stringify(result, null, 2) }],
      };
    }
  );

  server.tool(
    "customer_modify",
    "Meglévő ügyfél adatainak módosítása (SID alapján azonosít)",
    {
      sid: z.string().describe("Ügyfél egyedi azonosítója (SID)"),
      name: z.string().optional().describe("Ügyfél neve"),
      country: z.string().optional().describe("Országkód"),
      postcode: z.string().optional().describe("Irányítószám"),
      city: z.string().optional().describe("Város"),
      street: z.string().optional().describe("Utca"),
      street_number: z.string().optional().describe("Házszám"),
      door: z.string().optional().describe("Ajtó"),
      phone: z.string().optional().describe("Telefon"),
      tax_number: z.string().optional().describe("Adószám"),
      eu_tax_number: z.string().optional().describe("EU adószám"),
      email: z.string().optional().describe("Email cím"),
      invoice_send: z.number().optional().describe("Számla küldés módja"),
      comment: z.string().optional().describe("Megjegyzés"),
      bank: z.string().optional().describe("Bankszámlaszám"),
      bank_name: z.string().optional().describe("Bank neve"),
      lang: z.string().optional().describe("Nyelv (hu, en, de, stb.)"),
      active: z.number().optional().describe("Aktív (1) / Inaktív (0)"),
      firm_type: z
        .number()
        .optional()
        .describe("Típus: 1=beszállító, 2=vevő, 3=vevő és beszállító"),
      legal_status: z
        .string()
        .optional()
        .describe("Jogi státusz: CORPORATION (cég) vagy INDIVIDUAL (magánszemély)"),
      region: z.string().optional().describe("Régió (megye, tartomány)"),
      group_tax_number: z.string().optional().describe("Csoportos adószám"),
      other: z.string().optional().describe("JSON formátumban további meta adatok"),
      block: z.string().optional().describe("Számlatömb neve"),
    },
    async (params) => {
      const result = await client.call("customerModify", params);
      // Módosított ügyfél cache invalidálás
      cache.invalidate(`customer:${params.sid}`);
      cache.invalidatePrefix("customers:");
      return {
        content: [{ type: "text", text: JSON.stringify(result, null, 2) }],
      };
    }
  );

  server.tool(
    "customer_activate",
    "Ügyfél aktiválása SID alapján",
    {
      sid: z.string().describe("Ügyfél egyedi azonosítója (SID)"),
    },
    async (params) => {
      const result = await client.call("customerActivate", params);
      cache.invalidate(`customer:${params.sid}`);
      cache.invalidatePrefix("customers:");
      return {
        content: [{ type: "text", text: JSON.stringify(result, null, 2) }],
      };
    }
  );

  server.tool(
    "customer_inactivate",
    "Ügyfél inaktiválása SID alapján",
    {
      sid: z.string().describe("Ügyfél egyedi azonosítója (SID)"),
    },
    async (params) => {
      const result = await client.call("customerInactivate", params);
      cache.invalidate(`customer:${params.sid}`);
      cache.invalidatePrefix("customers:");
      return {
        content: [{ type: "text", text: JSON.stringify(result, null, 2) }],
      };
    }
  );
}
