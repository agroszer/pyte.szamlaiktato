/**
 * MCP Resources — API dokumentáció szekciókra bontva (HU + EN)
 * Az AI igény szerint olvashatja a releváns szekciókat.
 * Nyelv: ha a felhasználó magyarul beszél → HU, különben EN.
 */

import { readFileSync, existsSync } from "node:fs";
import { McpServer } from "@modelcontextprotocol/sdk/server/mcp.js";

interface DocSection {
  anchor: string;
  title: string;
  startLine: number;
  endLine: number;
}

/** Szekciók leírása — az anchor alapján azonosítjuk a ## fejléceket */
const SECTION_DESCRIPTIONS: Record<string, string> = {
  toc: "API dokumentáció tartalomjegyzék — összes elérhető szolgáltatás listája",
  connection: "API kapcsolódás, autentikáció, kérés/válasz formátum, hibakódok",
  install: "Számlázási példány install/update (központi rendszer)",
  customer: "customerAdd, customerModify, customerGet, customerActivate, customerInactivate, customerList",
  product: "productAdd, productModify, productGet, productActivate, productInactivate, productList, productFileList",
  outerDatasources: "outerDatasources, outerDatasourcesGet, outerDatasourcesSave",
  adminUser: "adminUserAdd, adminUserPassword, adminUserDel",
  block: "blockAdd, blockUpdateCompanyData, blockModify, blockList, blockClose, blockOpen",
  cost: "costCentreAdd/Modify/List/Activate/Inactivate, costTypeAdd/Modify/List/Activate/Inactivate",
  project: "projectList, projectGet, projectCreate, projectUpdate, projectActivate, projectInactivate, timesheet, booking",
  tax: "taxList, taxAdd, taxModify, taxActivate, taxInactivate",
  paymentMode: "paymentModeActivate, paymentModeInactivate, paymentModeDownload",
  order: "orderAdd, orderDetails, orderList, orderBill, orderSetPaid, orderCheckPaid, orderStorno, orderCollective*",
  invoice: "invoiceAdd, invoiceAddPrepayment, invoiceAddFinal, invoiceStorno, invoiceDetails, invoiceList, invoiceSearch, invoiceDownload, invoiceCorrection, invoiceSetPaid, invoiceExport",
  debt: "debtList, debtDetails, debtDownload, debtAdd, debtModify, debtAccept, debtPay, debtDelete, debtGenerate, debtExport",
  other: "getVersion, companyData, quantityList, currencyDownload, regularityDownload, countryDownload, postcodeDownload, ping, monitor",
  deprecated: "Deprecated szolgáltatások",
};

/**
 * Fájl sorait automatikusan szekciókra bontja a `## ` fejlécek és `<a name="...">` anchor-ok alapján
 */
function parseSections(lines: string[]): DocSection[] {
  const sections: DocSection[] = [];
  const anchorRegex = /<a\s+name="([^"]+)"/;

  // Első szekció: TOC (fájl elejétől az első ## fejlécig)
  let firstH2 = lines.findIndex((l) => l.startsWith("## "));
  if (firstH2 === -1) firstH2 = lines.length;

  sections.push({
    anchor: "toc",
    title: "Table of Contents",
    startLine: 1,
    endLine: firstH2,
  });

  // ## fejlécek keresése
  for (let i = 0; i < lines.length; i++) {
    if (!lines[i].startsWith("## ")) continue;

    const anchorMatch = lines[i].match(anchorRegex);
    const anchor = anchorMatch ? anchorMatch[1] : `section-${i}`;
    const title = lines[i]
      .replace(/^##\s+/, "")
      .replace(/<[^>]+>/g, "")
      .trim();

    sections.push({
      anchor,
      title,
      startLine: i + 1,
      endLine: lines.length, // ideiglenes, alább javítjuk
    });
  }

  // endLine kiszámítása: következő szekció startLine-ja
  for (let i = 0; i < sections.length - 1; i++) {
    sections[i].endLine = sections[i + 1].startLine - 1;
  }

  return sections;
}

export function registerResources(server: McpServer, huDocPath: string, enDocPath: string) {
  const docs: { lang: string; path: string; lines: string[] }[] = [];

  for (const { lang, path } of [
    { lang: "hu", path: huDocPath },
    { lang: "en", path: enDocPath },
  ]) {
    if (!existsSync(path)) {
      console.error(`API dokumentáció nem található: ${path}`);
      continue;
    }
    docs.push({ lang, path, lines: readFileSync(path, "utf8").split("\n") });
  }

  for (const doc of docs) {
    const sections = parseSections(doc.lines);

    for (const section of sections) {
      const uri = `onlineszamlazo://api-docs/${doc.lang}/${section.anchor}`;
      const desc =
        SECTION_DESCRIPTIONS[section.anchor] ?? section.title;
      const langLabel = doc.lang === "hu" ? "Magyar" : "English";
      const name = `${section.title} (${langLabel})`;

      server.resource(
        name,
        uri,
        {
          description: `[${doc.lang.toUpperCase()}] ${desc}`,
          mimeType: "text/markdown",
        },
        async () => {
          const content = doc.lines
            .slice(section.startLine - 1, section.endLine)
            .join("\n");
          return {
            contents: [
              {
                uri,
                mimeType: "text/markdown",
                text: content,
              },
            ],
          };
        }
      );
    }
  }
}
