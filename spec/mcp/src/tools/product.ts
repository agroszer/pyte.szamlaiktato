/**
 * Termék toolok: productAdd, productModify, productGet, productList
 */

import { McpServer } from "@modelcontextprotocol/sdk/server/mcp.js";
import { z } from "zod";
import { OnlineSzamlazoClient } from "../client.js";
import { SessionCache } from "../cache.js";

const productLangSchema = z
  .array(
    z.object({
      lang: z.string().describe("Nyelv kód (2 karakter, pl. en, de)"),
      name: z.string().describe("Termék neve ezen a nyelven"),
      short_description: z
        .string()
        .optional()
        .describe("Rövid leírás ezen a nyelven"),
      description: z
        .string()
        .optional()
        .describe("Leírás ezen a nyelven"),
    })
  )
  .optional()
  .describe("Többnyelvű nevek/leírások tömbje");

export function registerProductTools(
  server: McpServer,
  client: OnlineSzamlazoClient,
  cache: SessionCache
) {
  server.tool(
    "product_add",
    "Új termék/szolgáltatás létrehozása a számlázó rendszerben",
    {
      sid: z
        .string()
        .describe("Egyedi azonosító (a-zA-Z0-9_- minta, max 64 karakter)"),
      name: z.string().describe("Termék neve (fő nyelven)"),
      net_price_single: z.number().describe("Nettó egységár"),
      tax_code: z
        .string()
        .describe("ÁFA kód (taxList code érték, pl. '27%', '5%', 'AM')"),
      currency: z
        .string()
        .describe("Pénznem (3 karakter, nagybetű, pl. HUF, EUR)"),
      service_id: z.string().optional().describe("VTSZ/SZJ szám"),
      comment: z.string().optional().describe("Megjegyzés"),
      cost_type: z
        .string()
        .optional()
        .describe("Költség típus kód (costTypeList code)"),
      cost_centre: z
        .string()
        .optional()
        .describe("Költséghely kód (costCentreList code)"),
      lang: productLangSchema,
      other: z
        .string()
        .optional()
        .describe(
          "JSON formátumban: lineNatureIndicator (SERVICE/PRODUCT), intermediatedService (0/1)"
        ),
      block: z
        .string()
        .optional()
        .describe("Számlatömb neve (opcionális, ha az alapértelmezett nem jó)"),
    },
    async (params) => {
      const result = await client.call("productAdd", params);
      cache.invalidatePrefix("products:");
      return {
        content: [{ type: "text", text: JSON.stringify(result, null, 2) }],
      };
    }
  );

  server.tool(
    "product_modify",
    "Meglévő termék/szolgáltatás módosítása (SID alapján azonosít)",
    {
      sid: z.string().describe("Termék egyedi azonosítója (SID)"),
      name: z.string().optional().describe("Termék neve (fő nyelven)"),
      net_price_single: z.number().optional().describe("Nettó egységár"),
      tax_code: z
        .string()
        .optional()
        .describe("ÁFA kód (taxList code érték)"),
      currency: z
        .string()
        .optional()
        .describe("Pénznem (3 karakter, nagybetű)"),
      service_id: z.string().optional().describe("VTSZ/SZJ szám"),
      comment: z.string().optional().describe("Megjegyzés"),
      cost_type: z
        .string()
        .optional()
        .describe("Költség típus kód (costTypeList code)"),
      cost_centre: z
        .string()
        .optional()
        .describe("Költséghely kód (costCentreList code)"),
      lang: productLangSchema,
      other: z
        .string()
        .optional()
        .describe(
          "JSON formátumban: lineNatureIndicator (SERVICE/PRODUCT), intermediatedService (0/1)"
        ),
      block: z.string().optional().describe("Számlatömb neve"),
    },
    async (params) => {
      const result = await client.call("productModify", params);
      cache.invalidate(`product:${params.sid}`);
      cache.invalidatePrefix("products:");
      return {
        content: [{ type: "text", text: JSON.stringify(result, null, 2) }],
      };
    }
  );

  server.tool(
    "product_get",
    "Egy termék/szolgáltatás adatainak lekérdezése SID alapján",
    {
      sid: z.string().describe("Termék egyedi azonosítója (SID)"),
    },
    async (params) => {
      const cacheKey = `product:${params.sid}`;
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

      const result = await client.call("productGet", params);
      cache.set(cacheKey, result, 15);
      return {
        content: [{ type: "text", text: JSON.stringify(result, null, 2) }],
      };
    }
  );

  server.tool(
    "product_list",
    "Termékek/szolgáltatások listázása és keresése. Cache-elt azonos szűrési feltételekkel.",
    {
      cost_type: z
        .string()
        .optional()
        .describe("Költség típus szűrő (costTypeList code)"),
      cost_centre: z
        .string()
        .optional()
        .describe("Költséghely szűrő (costCentreList code)"),
      active: z
        .number()
        .optional()
        .describe("Aktív szűrő: 0=inaktív, 1=aktív"),
      currency: z
        .string()
        .optional()
        .describe("Pénznem szűrő (3 karakter, nagybetű)"),
      lang: z
        .string()
        .optional()
        .describe("Nyelv szűrő (2 karakter)"),
      name: z
        .string()
        .optional()
        .describe("Termék neve (keresés)"),
      sid: z
        .string()
        .optional()
        .describe("Egyedi azonosító (keresés)"),
      limit: z
        .number()
        .optional()
        .describe("Oldalméret (alapértelmezett: 10, max: 1000)"),
      page: z.number().optional().describe("Oldalszám (alapértelmezett: 1)"),
      refresh: z.boolean().optional().describe("true = cache frissítése"),
    },
    async (params) => {
      const { refresh, ...apiParams } = params;
      const cacheKey = `products:${JSON.stringify(apiParams)}`;

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

      const result = await client.call("productList", apiParams, {
        skipBlock: true,
      });
      cache.set(cacheKey, result, 15);
      return {
        content: [{ type: "text", text: JSON.stringify(result, null, 2) }],
      };
    }
  );

  server.tool(
    "product_activate",
    "Termék/szolgáltatás aktiválása SID alapján",
    {
      sid: z.string().describe("Termék egyedi azonosítója (SID)"),
    },
    async (params) => {
      const result = await client.call("productActivate", params);
      cache.invalidate(`product:${params.sid}`);
      cache.invalidatePrefix("products:");
      return {
        content: [{ type: "text", text: JSON.stringify(result, null, 2) }],
      };
    }
  );

  server.tool(
    "product_inactivate",
    "Termék/szolgáltatás inaktiválása SID alapján",
    {
      sid: z.string().describe("Termék egyedi azonosítója (SID)"),
    },
    async (params) => {
      const result = await client.call("productInactivate", params);
      cache.invalidate(`product:${params.sid}`);
      cache.invalidatePrefix("products:");
      return {
        content: [{ type: "text", text: JSON.stringify(result, null, 2) }],
      };
    }
  );
}
