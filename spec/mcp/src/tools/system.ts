/**
 * Rendszer toolok: login, blockList, ping, getVersion, paymentModeDownload,
 * companyData, quantityList, currencyDownload, regularityDownload, countryDownload, postcodeDownload,
 * systemErrorCodeList
 */

import { McpServer } from "@modelcontextprotocol/sdk/server/mcp.js";
import { z } from "zod";
import { OnlineSzamlazoClient } from "../client.js";
import { SessionCache } from "../cache.js";

export function registerSystemTools(
  server: McpServer,
  client: OnlineSzamlazoClient,
  cache: SessionCache,
  mcpVersion?: string
) {
  server.tool(
    "login",
    "Bejelentkezés és kapcsolat ellenőrzés az OnlineSzámlázó API-hoz",
    {},
    async () => {
      const result = await client.call("login", {}, { skipBlock: true });
      return {
        content: [{ type: "text", text: JSON.stringify(result, null, 2) }],
      };
    }
  );

  server.tool(
    "block_list",
    "Számlatömbök listázása. A block a számlázási egység azonosító — más hívásokhoz szükséges. Cache-elt: session-ben csak egyszer kérdezi le.",
    {
      active: z
        .number()
        .optional()
        .describe("1 = csak aktívak, 0 = összes"),
      refresh: z
        .boolean()
        .optional()
        .describe("true = cache frissítése, újra lekérdez"),
    },
    async (params) => {
      const cacheKey = `blocks:${params.active ?? 1}`;

      if (!params.refresh) {
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

      const result = await client.call(
        "blockList",
        { active: params.active ?? 1 },
        { skipBlock: true }
      );
      cache.set(cacheKey, result, 60); // 1 óra TTL — ritkán változik
      return {
        content: [{ type: "text", text: JSON.stringify(result, null, 2) }],
      };
    }
  );

  server.tool(
    "ping",
    "API elérhetőség ellenőrzés",
    {},
    async () => {
      const result = await client.call("ping", {}, { skipBlock: true });
      return {
        content: [{ type: "text", text: JSON.stringify(result, null, 2) }],
      };
    }
  );

  server.tool(
    "get_version",
    "API és MCP szerver verzió lekérdezés",
    {},
    async () => {
      const result = await client.call("getVersion", {}, { skipBlock: true });
      const response = {
        mcp_version: mcpVersion ?? "unknown",
        api: result,
      };
      return {
        content: [{ type: "text", text: JSON.stringify(response, null, 2) }],
      };
    }
  );

  server.tool(
    "payment_mode_list",
    "Fizetési módok listázása. Cache-elt: session-ben csak egyszer kérdezi le.",
    {
      refresh: z
        .boolean()
        .optional()
        .describe("true = cache frissítése"),
    },
    async (params) => {
      const cacheKey = "payment_modes";

      if (!params.refresh) {
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

      const result = await client.call(
        "paymentModeDownload",
        {},
        { skipBlock: true }
      );
      cache.set(cacheKey, result, 60);
      return {
        content: [{ type: "text", text: JSON.stringify(result, null, 2) }],
      };
    }
  );

  server.tool(
    "company_data",
    "Saját cégadatok lekérdezése (számla kibocsátó adatok). Cache-elt.",
    {
      refresh: z.boolean().optional().describe("true = cache frissítése"),
    },
    async (params) => {
      const cacheKey = "company_data";
      if (!params.refresh) {
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
      const result = await client.call("companyData", {}, { skipBlock: true });
      cache.set(cacheKey, result, 60);
      return {
        content: [{ type: "text", text: JSON.stringify(result, null, 2) }],
      };
    }
  );

  server.tool(
    "quantity_list",
    "Mennyiségi egységek listája (pl. db, óra, kg). Cache-elt, ritkán változik.",
    {
      refresh: z.boolean().optional().describe("true = cache frissítése"),
    },
    async (params) => {
      const cacheKey = "quantities";
      if (!params.refresh) {
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
      const result = await client.call("quantityList", {}, { skipBlock: true });
      cache.set(cacheKey, result, 120);
      return {
        content: [{ type: "text", text: JSON.stringify(result, null, 2) }],
      };
    }
  );

  server.tool(
    "currency_download",
    "Elérhető pénznemek listája (ISO kódok). Cache-elt, ritkán változik.",
    {
      refresh: z.boolean().optional().describe("true = cache frissítése"),
    },
    async (params) => {
      const cacheKey = "currencies";
      if (!params.refresh) {
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
      const result = await client.call(
        "currencyDownload",
        {},
        { skipBlock: true }
      );
      cache.set(cacheKey, result, 120);
      return {
        content: [{ type: "text", text: JSON.stringify(result, null, 2) }],
      };
    }
  );

  server.tool(
    "regularity_download",
    "Ismétlődési típusok listája (pl. MONTHLY, YEARLY). Díjbekérő automatikus számlázáshoz szükséges. Cache-elt.",
    {
      refresh: z.boolean().optional().describe("true = cache frissítése"),
    },
    async (params) => {
      const cacheKey = "regularities";
      if (!params.refresh) {
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
      const result = await client.call(
        "regularityDownload",
        {},
        { skipBlock: true }
      );
      cache.set(cacheKey, result, 120);
      return {
        content: [{ type: "text", text: JSON.stringify(result, null, 2) }],
      };
    }
  );

  server.tool(
    "country_download",
    "Országkódok listája (ISO 3166-1 alpha-2). Cache-elt, ritkán változik.",
    {
      refresh: z.boolean().optional().describe("true = cache frissítése"),
    },
    async (params) => {
      const cacheKey = "countries";
      if (!params.refresh) {
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
      const result = await client.call(
        "countryDownload",
        {},
        { skipBlock: true }
      );
      cache.set(cacheKey, result, 120);
      return {
        content: [{ type: "text", text: JSON.stringify(result, null, 2) }],
      };
    }
  );

  server.tool(
    "postcode_download",
    "Irányítószámok listája (ország alapján). Cache-elt.",
    {
      country: z
        .string()
        .optional()
        .describe("Országkód szűrő (pl. HU, alapértelmezett: összes)"),
      refresh: z.boolean().optional().describe("true = cache frissítése"),
    },
    async (params) => {
      const { refresh, ...apiParams } = params;
      const cacheKey = `postcodes:${params.country ?? "all"}`;
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
      const result = await client.call("postcodeDownload", apiParams, {
        skipBlock: true,
      });
      cache.set(cacheKey, result, 120);
      return {
        content: [{ type: "text", text: JSON.stringify(result, null, 2) }],
      };
    }
  );

  server.tool(
    "system_error_code_list",
    "Rendszer hibakódok és jelentésük listája. Használd ha egy API hívás hibát ad vissza és tudni akarod mit jelent a status_id. Magyar felhasználónak lang='hu', mindenki másnak lang='en'. Cache-elt nyelvenként.",
    {
      lang: z
        .string()
        .optional()
        .describe("Nyelv kód (2 karakter, pl. 'hu' vagy 'en'). Magyar felhasználónak 'hu', mindenki másnak 'en'."),
      refresh: z.boolean().optional().describe("true = cache frissítése"),
    },
    async (params) => {
      const lang = params.lang ?? "hu";
      const cacheKey = `error_codes:${lang}`;
      if (!params.refresh) {
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
      const result = await client.call(
        "systemErrorCodeList",
        { lang },
        { skipBlock: true }
      );
      cache.set(cacheKey, result, 120); // 2 óra — hibakódok nem változnak
      return {
        content: [{ type: "text", text: JSON.stringify(result, null, 2) }],
      };
    }
  );
}
