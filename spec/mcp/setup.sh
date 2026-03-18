#!/bin/bash
# OnlineSzámlázó MCP szerver — automatikus telepítő
# Használat: bash setup.sh

set -e

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
cd "$SCRIPT_DIR"

echo ""
echo "=== OnlineSzámlázó MCP szerver telepítés ==="
echo ""

# Node ellenőrzés
if ! command -v node &> /dev/null; then
    echo "HIBA: Node.js nem található! Telepítsd: https://nodejs.org/"
    exit 1
fi

NODE_MAJOR=$(node -e "console.log(process.versions.node.split('.')[0])")
if [ "$NODE_MAJOR" -lt 22 ]; then
    echo "HIBA: Node.js 22+ szükséges! (jelenleg: $(node --version))"
    echo "Frissítsd: https://nodejs.org/"
    exit 1
fi

echo "Node.js $(node --version) — OK"
echo ""

# Függőségek
echo "Függőségek telepítése..."
npm install --silent 2>/dev/null
npm run build --silent 2>/dev/null
echo "Build OK"
echo ""

# .env ellenőrzés
if [ -f .env ] && ! grep -q "your@email.com" .env 2>/dev/null && ! grep -q "yourdomain" .env 2>/dev/null; then
    echo ".env fájl megtalálva — OK"
else
    echo "============================================"
    echo "  .env fájl hiányzik vagy nincs beállítva!"
    echo "============================================"
    echo ""
    echo "Töltsd le az .env fájlt az OnlineSzámlázó admin felületéről:"
    echo ""
    echo "  1. Beállítások → Adminisztrátorok"
    echo "  2. API felhasználó sorában: hamburger menü (⋮) → \"MCP .env\""
    echo "  3. Mentsd el a letöltött fájlt ide: $SCRIPT_DIR/.env"
    echo ""
    echo "Ha megvan, futtasd újra: bash setup.sh"
    exit 1
fi

# Fájl jogosultságok — csak a tulajdonos olvashatja/írhatja
chmod 600 .env

# Útvonalak
DIST_PATH="$SCRIPT_DIR/dist/index.js"
ENV_PATH="$SCRIPT_DIR/.env"
PROJECT_ROOT="$SCRIPT_DIR/.."
MCP_JSON="$PROJECT_ROOT/.mcp.json"
CLAUDE_DESKTOP_CONFIG="$HOME/Library/Application Support/Claude/claude_desktop_config.json"

# MCP szerver JSON blokk (node-dal generálva a biztonságos JSON escape miatt)
MCP_SERVER_JSON=$(node -e "console.log(JSON.stringify({type:'stdio',command:'node',args:['--env-file','$ENV_PATH','$DIST_PATH']}))")

# --- 1) Claude Code: .mcp.json ---
echo ""
echo "=== Claude Code konfiguráció ==="

if [ -f "$MCP_JSON" ]; then
    # Meglévő .mcp.json — onlineszamlazo kulcs hozzáadása/felülírása
    UPDATED=$(node -e "
        const fs = require('fs');
        const cfg = JSON.parse(fs.readFileSync('$MCP_JSON', 'utf8'));
        if (!cfg.mcpServers) cfg.mcpServers = {};
        cfg.mcpServers.onlineszamlazo = $MCP_SERVER_JSON;
        console.log(JSON.stringify(cfg, null, 2));
    ")
    echo "$UPDATED" > "$MCP_JSON"
    echo "Frissítve: $MCP_JSON"
else
    # Új .mcp.json létrehozása
    node -e "
        const cfg = { mcpServers: { onlineszamlazo: $MCP_SERVER_JSON } };
        console.log(JSON.stringify(cfg, null, 2));
    " > "$MCP_JSON"
    echo "Létrehozva: $MCP_JSON"
fi

# --- 2) Claude Desktop: claude_desktop_config.json ---
echo ""
echo "=== Claude Desktop konfiguráció ==="

CLAUDE_DESKTOP_DIR="$(dirname "$CLAUDE_DESKTOP_CONFIG")"

if [ -d "$CLAUDE_DESKTOP_DIR" ]; then
    if [ -f "$CLAUDE_DESKTOP_CONFIG" ]; then
        # Meglévő config — onlineszamlazo kulcs hozzáadása/felülírása
        UPDATED=$(node -e "
            const fs = require('fs');
            const cfg = JSON.parse(fs.readFileSync('$CLAUDE_DESKTOP_CONFIG', 'utf8'));
            if (!cfg.mcpServers) cfg.mcpServers = {};
            cfg.mcpServers.onlineszamlazo = $MCP_SERVER_JSON;
            console.log(JSON.stringify(cfg, null, 2));
        ")
        echo "$UPDATED" > "$CLAUDE_DESKTOP_CONFIG"
        echo "Frissítve: $CLAUDE_DESKTOP_CONFIG"
    else
        # Új config létrehozása
        node -e "
            const cfg = { mcpServers: { onlineszamlazo: $MCP_SERVER_JSON } };
            console.log(JSON.stringify(cfg, null, 2));
        " > "$CLAUDE_DESKTOP_CONFIG"
        echo "Létrehozva: $CLAUDE_DESKTOP_CONFIG"
    fi
else
    echo "Claude Desktop nincs telepítve (nem található: $CLAUDE_DESKTOP_DIR)"
    echo "Ha később telepíted, futtasd újra: bash setup.sh"
fi

# --- Összefoglaló ---
echo ""
echo "=== Kész! ==="
echo ""
echo "Indítsd újra a Claude Code-ot / Claude Desktop-ot, és írd be:"
echo "  \"Pingelj meg az onlineszamlazo API-n!\""
echo ""
echo "FONTOS: A jelszavad csak a géped .env fájljában van,"
echo "sem a kódba, sem a git-be, sem az AI-hoz nem kerül."
echo "Ne oszd meg az .env fájlt senkivel!"
echo ""
