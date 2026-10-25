---
name: scripts-python
description: "Use when creating, writing, rewriting, revising, restyling, or reviewing any Python (.py) script or tool - especially short prompts like 'rewrite this script: /path/foo.py'. Auto-applies the Vituvo Python standard: banner header identical in style to scripts-bash (Author/Date/Ver/Name/Define, colon-aligned, = padded to column 75, description + Credits block), snake_case functions/variables, SCREAMING_SNAKE_CASE module constants, PascalCase classes, type hints, argparse, main()->int with SystemExit. On rewrite: write version-bumped sibling (name.py->name-01.py, name-01.py->name-02.py); do not overwrite source unless asked."
version: 1.0.0
author: Vituvo
license: MIT
platforms: [linux]
metadata:
  hermes:
    tags: [Python, Scripts, Automation, CLI, Tools, Style]
    related_skills: [scripts-bash]
---

# scripts-python

Standard for **long-lived Python scripts and tools**. Not for one-liners or throwaway REPL snippets.

## When to use

- **Any** create / write / rewrite / restyle / fix / review of a `.py` file
- Short prompts: `rewrite this script: /path/to/foo.py` (load this skill automatically; user need not list steps)

## Rewrite output naming (automatic)

| Source | Output (same directory) |
|--------|-------------------------|
| `name.py` | `name-01.py` |
| `.name.py` | `.name-01.py` (leading dot preserved) |
| `name-01.py` | `name-02.py` |
| `name-NN.py` | `name-(NN+1).py` (2-digit pad) |

Do not overwrite source unless the user says overwrite. Keep behavior; apply full style law.
Dotfile / hidden names are normal - not special-case blockers.

## Live skill path

Install / load from:

`~/.hermes/skills/software-development/scripts-python/`

Do not require a copy under `profiles/*/skills/`. If lookup fails under a profile, use this absolute path.

## Execution discipline (rewrites)

1. Load this skill + read source in early tool calls.
2. **Call the write tool in the same turn you decide to write** - no "Writing now." / "Resuming..." without a tool call.
3. No multi-paragraph status recaps between tools.
4. After write: `python3 -m py_compile <file>`; chat reports path + size only.
5. If a prior turn stalled before write: **retry write immediately**.

## When NOT to use

- Snippets under ~30 lines, pure library modules with no entrypoint, non-Python

## Skill vs products

The skill is the rules, one template, conventions, and authoring. The script you run is a **product**. Copy **`templates/template_base.py`** out. Never write live products into this skill tree.

## Package contents (lean)

```text
SKILL.md
README.md
templates/template_base.py                 # ONLY skeleton
references/python-conventions.md
references/authoring.md
```

One skeleton only. No duplicate templates. No `examples/` clone. No symlinks.

## Tutorial

Read **`references/authoring.md`** the first time you use the skill.

## File structure (top -> bottom)

```text
1. #!/usr/bin/env python3
2. Banner header identical in style to scripts-bash (Author / Date / Ver / Name / Define + optional description + Credits)
3. from __future__ import annotations
4. stdlib imports (sorted), then third-party, then local
5. Module constants (SCREAMING_SNAKE_CASE)
6. parse_args() -> argparse.Namespace
7. Domain functions (snake_case, type-hinted)
8. run(args) -> int  (core logic; returns exit code)
9. main() -> int     (parse, try/except KeyboardInterrupt, return run())
10. if __name__ == "__main__": raise SystemExit(main())
```

## Header

**Identical style to scripts-bash.** Field name left-justified to width 6, then
colon, space, value, then `=` padding to **column 75**. Fields: Author / Date /
Ver / Name / Define, a `# ===` rule line, an optional multi-line description, a
`Credits:` block, then a closing `# ===` rule. See `templates/template_base.py`.
Only the routines below the header differ from bash - the header and `# === ... ===`
section comments look exactly like `template-base.sh`.

## Style law

- **snake_case** functions and variables; **SCREAMING_SNAKE_CASE** module constants; **PascalCase** classes.
- **Type hints** on every function signature and return.
- **`argparse`** for any script that takes arguments; no manual `sys.argv` parsing.
- **`pathlib.Path`**, not `os.path` string joins.
- **f-strings**, not `%` or `.format()`.
- Entrypoint is `main() -> int` returning an exit code; `raise SystemExit(main())` at bottom.
- Catch `KeyboardInterrupt` in `main()`, print a clean message to stderr, return 1.
- Standard library only unless the user approves a dependency; list any dependency in the header `DEPENDENCIES` block.
- Prefer `from __future__ import annotations` at the top.
- Docstrings on public functions; keep section banner comments (`# === Title 'Quoted' ===`) - do not rewrite them unless asked.

## Cron / headless scripts

Headless or cron scripts must be **silent**: no banner, no stdout chatter. Just core logic and a clean exit code. Keep verbosity only for interactive/CLI use.

## Hard gates

1. `python3 -m py_compile <file>` clean (syntax gate)
2. No `pip install` / network / system writes unless the user asked
3. No destructive surprise; prefer a `--dry-run` flag for anything that changes files
4. Prefer user-local paths (`~/.hermes/`) unless the user sets otherwise
5. Never embed secrets/keys/tokens; read from env or `~/.hermes/.env`
6. Disk evidence after write (path + size); do not claim a write without verifying
7. Full script only - never partial "here's just the changed function"
8. Version-bump on rewrite; do not overwrite source unless asked

## Pitfalls

- Duplicate skeleton files inside the skill (forbidden - one template only)
- Bare `except:` or swallowing exceptions silently
- `print()` debugging left in headless/cron scripts
- Mutable default arguments (`def f(x=[])`)
- Manual `sys.argv` slicing instead of `argparse`
- Shipping a second copy of the template inside the skill
- Skill name confusion: skill is **`scripts-python`**

## Version

- **1.0.0** - Initial release; mirrors scripts-bash 4.3.0 layout and discipline for Python.
