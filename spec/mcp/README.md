# OnlineSzámlázó MCP szerver

Ez az MCP szerver lehetővé teszi, hogy a Claude Code (vagy más MCP-kompatibilis AI) közvetlenül kezelje az OnlineSzámlázó rendszert: számlákat hozzon létre, ügyfeleket kezeljen, stb.

## Telepítés

### 1. Előfeltétel

- **Node.js 22+** szükséges — [letöltés](https://nodejs.org/)
- Ellenőrzés terminálban: `node --version`

### 2. Az `.env` fájl letöltése

1. Lépj be az OnlineSzámlázó admin felületedre
2. Menj a **Beállítások** → **Adminisztrátorok** menüpontra
3. Ha még nincs API felhasználód, hozz létre egyet
4. Az API felhasználó sorában kattints a **hamburger menüre** (⋮) → **"MCP .env"**
5. Mentsd el a letöltött `.env` fájlt az `mcp/` mappába

### 3. Telepítés

Nyiss terminált az `mcp/` könyvtárban és futtasd:

```bash
bash setup.sh
```

A script telepíti a függőségeket, ellenőrzi az `.env` fájlt, és kiírja a Claude Code beállítást.

### 4. Claude Code beállítása

A setup script végén kiír egy JSON blokkot. Ezt másold be a megfelelő helyre:

- **Projekt szintű** (ajánlott): a projekt gyökerében lévő `.mcp.json` fájlba
- **Felhasználó szintű**: a `~/.claude/settings.json` fájlba

Ha a fájl még nem létezik, hozd létre a teljes tartalommal. Ha már létezik, az `mcpServers` objektumba add hozzá az `onlineszamlazo` részt.

### 5. Tesztelés

Indítsd újra a Claude Code-ot, majd írd be:

```
Pingelj meg az onlineszamlazo API-n!
```

Ha jön válasz `status_id: 1000`-rel, minden működik.

## Biztonság

**A jelszavad biztonságban van.** Csak a te gépeden van tárolva, senki más nem fér hozzá:

- **Nem kerül git-be** — a `.gitignore` kizárja az `mcp/.env` fájlt
- **Csak te olvashatod** — a setup script `chmod 600`-ra állítja a jogosultságokat (más felhasználó nem nyithatja meg)
- **Nem kerül a kódba** — a szerver futáskor olvassa be a környezeti változókból
- **A Claude (AI) sem látja a jelszót** — a jelszó a háttérben, a te gépeden fut le a REST API hívásokkor. A Claude csak az API válaszát kapja meg (pl. számlák listája, ügyfél adatok). A jelszó semmilyen formában nem jelenik meg az AI beszélgetésben.
- **Ne add ki másnak** — az `.env` fájl tartalma bizalmas, ne küldd el emailben, chaten, vagy bárhol. Ha más is használni akarja, hozzon létre saját API felhasználót az admin felületen.

> Ha úgy érzed, illetéktelen hozzáfért a gépedhez, az admin felületen bármikor megváltoztathatod az API jelszót.

## Elérhető funkciók

### Rendszer

| Parancs | Mit csinál |
|---------|-----------|
| `login` | Kapcsolat ellenőrzés |
| `ping` | API elérhetőség |
| `get_version` | API verzió |
| `block_list` | Számlatömbök listázása |
| `payment_mode_list` | Fizetési módok |
| `company_data` | Saját cégadatok |
| `quantity_list` | Mennyiségi egységek (db, óra, kg, stb.) |
| `currency_download` | Pénznemek listája |
| `regularity_download` | Ismétlődési típusok (havi, éves, stb.) |
| `country_download` | Országkódok |
| `postcode_download` | Irányítószámok |

### Ügyfelek

| Parancs | Mit csinál |
|---------|-----------|
| `customer_add` | Új ügyfél létrehozása |
| `customer_list` | Ügyfelek keresése (név, email, SID) |
| `customer_get` | Ügyfél adatai (SID vagy adószám) |
| `customer_modify` | Ügyfél módosítása |
| `customer_activate` | Ügyfél aktiválása |
| `customer_inactivate` | Ügyfél inaktiválása |

### Termékek / Szolgáltatások

| Parancs | Mit csinál |
|---------|-----------|
| `product_add` | Új termék/szolgáltatás |
| `product_modify` | Termék módosítása |
| `product_get` | Termék adatai |
| `product_list` | Termékek listázása/keresése |
| `product_activate` | Termék aktiválása |
| `product_inactivate` | Termék inaktiválása |

### Számlák

| Parancs | Mit csinál |
|---------|-----------|
| `invoice_add` | Számla készítés |
| `invoice_details` | Számla részletei |
| `invoice_list` | Számlák listázása |
| `invoice_storno` | Számla sztornó |
| `invoice_set_paid` | Fizetettnek jelölés |
| `invoice_download` | PDF letöltés |

### Megrendelések / Díjbekérők

| Parancs | Mit csinál |
|---------|-----------|
| `order_add` | Megrendelés/díjbekérő létrehozása |
| `order_details` | Megrendelés részletei |
| `order_list` | Megrendelések listázása |
| `order_storno` | Megrendelés sztornó |
| `order_bill` | Díjbekérő kiszámlázása |
| `order_set_paid` | Fizetettnek jelölés |
| `order_check_paid` | Fizetési státusz ellenőrzése |
| `order_paid_change_list` | Fizetett díjbekérők számla nélkül |
| `order_proform_download` | Díjbekérő PDF letöltés |
| `order_collective_add` | Gyűjtő díjbekérő létrehozása |
| `order_collective_add_elements` | Tételek hozzáadása gyűjtőhöz |
| `order_collective_close` | Gyűjtő lezárása és számlázása |
| `order_collective_settling` | Gyűjtő elszámolás lekérdezése |

## Megjegyzések

- A session alatt a ritkán változó adatok (számlatömbök, fizetési módok, ügyfelek) cache-elve vannak — nem kérdezi le minden alkalommal újra
- Bármely tool-nál megadhatsz `refresh: true` paramétert a cache frissítéséhez
