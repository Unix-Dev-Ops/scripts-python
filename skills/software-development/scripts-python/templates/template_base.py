#!/usr/bin/env python3
#
# Author: Vituvo ==========================================================
# Date  : <Month DD, YYYY> ================================================
# Ver   : 1.0 =============================================================
# Name  : <script_name.py> ================================================
# Define: <One-line purpose statement> ====================================
# =========================================================================
#
# <Optional multi-line description of what this script does.>
# <Note any files/paths it reads or writes, and safe re-run behavior.>
#
# Credits:
#   *  <optional attribution lines>
# =========================================================================

from __future__ import annotations

import argparse
import sys
from pathlib import Path

# === Script 'Constants' ===
TITLE = "<Human Readable Title>"
HERMES_HOME = Path.home() / ".hermes"


# === Parse 'Command-Line' Arguments ===
def parse_args() -> argparse.Namespace:
    """Define and parse command-line arguments."""
    parser = argparse.ArgumentParser(
        prog=Path(__file__).name,
        description="<One-line purpose statement>",
    )
    parser.add_argument(
        "--example",
        action="store_true",
        help="Run example mode.",
    )
    return parser.parse_args()


# === Core 'Logic' ===
def run(args: argparse.Namespace) -> int:
    """Core logic. Return a process exit code (0 = success)."""
    if args.example:
        print(f"{TITLE}: example mode using {HERMES_HOME}")
    else:
        print(f"{TITLE}: OK")
    return 0


# === Main 'Entrypoint' ===
def main() -> int:
    """Parse arguments, run, and return an exit code."""
    args = parse_args()
    try:
        return run(args)
    except KeyboardInterrupt:
        print("Interrupted by user - exiting cleanly", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
