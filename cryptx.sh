#!/usr/bin/env bash
# ============================================================
#  CryptX – Bash Launcher
#  Author : iamunknown77
#  Usage  : ./cryptx.sh [options]
#           ./cryptx.sh -c caesar -t "hello" -k 13 -m encrypt
# ============================================================

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PY="$SCRIPT_DIR/cryptx.py"

# ── Colours ────────────────────────────────────────────────
R='\033[1;31m' G='\033[1;32m' Y='\033[1;33m'
C='\033[1;36m' W='\033[1;37m' RST='\033[0m'

# ── Check Python ───────────────────────────────────────────
if ! command -v python3 &>/dev/null; then
    echo -e "${R}[!] python3 is required but not found.${RST}"
    echo -e "${Y}    Install with: sudo apt install python3${RST}"
    exit 1
fi

# ── Interactive mode (no args) ─────────────────────────────
if [[ $# -eq 0 ]]; then
    python3 "$PY"
    exit $?
fi

# ── CLI pass-through ───────────────────────────────────────
python3 "$PY" "$@"
