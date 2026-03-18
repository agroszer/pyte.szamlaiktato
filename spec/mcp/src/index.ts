#!/usr/bin/env node

/**
 * OnlineSzámlázó MCP Server
 * Számlázó REST API integrációja Model Context Protocol-on keresztül
 */

import { readFileSync } from "node:fs";
import { fileURLToPath } from "node:url";
import { dirname, join } from "node:path";
import { McpServer } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { OnlineSzamlazoClient } from "./client.js";
import { SessionCache } from "./cache.js";
import { registerSystemTools } from "./tools/system.js";
import { registerCustomerTools } from "./tools/customer.js";
import { registerInvoiceTools } from "./tools/invoice.js";
import { registerProductTools } from "./tools/product.js";
import { registerOrderTools } from "./tools/order.js";
import { registerResources } from "./resources.js";

const __dirname = dirname(fileURLToPath(import.meta.url));
const pkg = JSON.parse(readFileSync(join(__dirname, "../package.json"), "utf8"));
const MCP_VERSION: string = pkg.version;

// Konfiguráció környezeti változókból
const config = {
  apiUrl: process.env.API_URL ?? "",
  uid: process.env.API_UID ?? "",
  password: process.env.API_PASSWORD ?? "",
  block: process.env.API_BLOCK ?? "",
};

if (!config.apiUrl || !config.uid || !config.password) {
  console.error(
    "Hiányzó konfiguráció! Szükséges env változók: API_URL, API_UID, API_PASSWORD"
  );
  console.error("Opcionális: API_BLOCK (alapértelmezett számlatömb)");
  process.exit(1);
}

const client = new OnlineSzamlazoClient(config);
const cache = new SessionCache(30); // 30 perc TTL

const server = new McpServer({
  name: "onlineszamlazo",
  version: MCP_VERSION,
});

// Toolok regisztrálása
registerSystemTools(server, client, cache, MCP_VERSION);
registerCustomerTools(server, client, cache);
registerInvoiceTools(server, client, cache);
registerProductTools(server, client, cache);
registerOrderTools(server, client, cache);

// API dokumentáció resource-ok (HU + EN)
const apiDocsDir = join(__dirname, "../../public/admin/docs");
registerResources(
  server,
  join(apiDocsDir, "onlineszamlazo-api-hu-v7.57.md"),
  join(apiDocsDir, "onlineszamlazo-api-en-v7.57.md")
);

// Számla készítési wizard prompt
server.prompt(
  "invoice_wizard",
  "Számla készítési varázsló — lépésről lépésre végigvezeti a felhasználót a számlázáson. Használd az AskUserQuestion tool-t minden lépésnél!",
  async () => ({
    messages: [
      {
        role: "user",
        content: {
          type: "text",
          text: `Számlát szeretnék készíteni.

FONTOS: Használd az AskUserQuestion tool-t minden egyes lépéshez! Egy kérdés = egy AskUserQuestion hívás. NE lépj tovább amíg nem kaptál választ!

Lépések:
1) AskUserQuestion: Milyen típusú számlát szeretne?
   - Azonnali végleges számla → invoice_add
   - Díjbekérő (tervezett) → order_add (proform_order=1)
   - Automata időzítésű → order_add (regularity + regularities_date)
   - Ismétlődő → order_add (regularity pl. MONTHLY)
   - Gyűjtő díjbekérő → order_collective_add

2) AskUserQuestion: Ki az ügyfél? (keresés neve/adószáma alapján, vagy "új" ha létre kell hozni)
   → customer_list keresés, vagy customer_add

3) AskUserQuestion: Milyen terméket/szolgáltatást számlázzon? (mennyiség, ár)
   → product_list keresés

4) AskUserQuestion: Fizetési mód? (mutasd a lehetőségeket payment_mode_list-ből)

5) AskUserQuestion: Fizetési határidő? (YYYY-MM-DD)

6) Összefoglalás megjelenítése, majd AskUserQuestion: Megerősíti? (igen/nem)
   → Ha igen: invoice_add / order_add végrehajtás`,
        },
      },
    ],
  })
);

// Szerver indítása stdio transport-tal
const transport = new StdioServerTransport();
await server.connect(transport);
