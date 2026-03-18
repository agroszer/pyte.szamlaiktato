#!/bin/bash
# MCP szerver becsomagolása terjesztéshez
# Használat: bash pack.sh

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
cd "$SCRIPT_DIR/.."

OUTFILE="mcp-onlineszamlazo.tar.gz"

tar -czf "$OUTFILE" \
    --exclude='mcp/.env' \
    --exclude='mcp/node_modules' \
    --exclude='mcp/dist' \
    mcp/ \
    .claude/settings.json

echo "Kész: $OUTFILE ($(du -h "$OUTFILE" | cut -f1))"
echo "Ezt küldd el — a másik félnek csak ennyi a dolga:"
echo ""
echo "  tar -xzf $OUTFILE"
echo "  cd mcp"
echo "  bash setup.sh"
