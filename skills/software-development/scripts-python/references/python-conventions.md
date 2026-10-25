# Python conventions - scripts-python

Naming, structure, and style law. Read before inventing your own patterns.

## Naming

| Kind | Convention | Example |
|------|------------|---------|
| Function | `snake_case` | `parse_args`, `run` |
| Variable | `snake_case` | `out_path`, `args` |
| Module constant | `SCREAMING_SNAKE_CASE` | `TITLE`, `HERMES_HOME` |
| Class | `PascalCase` | `Config` |
| Private helper | leading underscore | `_read_lines` |
| Module file | `snake_case.py` | `script_name.py` |

Examples must be greppable in `templates/template_base.py`, or they are generic names (`Config`, `_read_lines`) with no product attached.

## Banner header (required)

**Identical in style to scripts-bash `template-base.sh`.** Field name left-justified
to width 6, then colon, space, value, then `=` padding to **column 75**. Same field
set as bash: Author / Date / Ver / Name / Define.

```python
#!/usr/bin/env python3
#
# Author: Vituvo ==========================================================
# Date  : Month DD, YYYY ==================================================
# Ver   : 1.0 =============================================================
# Name  : script_name.py ==================================================
# Define: One-line purpose statement ======================================
# =========================================================================
#
# Optional multi-line description of what this script does.
# Note any files/paths it reads or writes, and safe re-run behavior.
#
# Credits:
#   *  optional attribution lines
# =========================================================================
```

The header and `# === Title 'Quoted' ===` section comments must look exactly like
the bash template. Only the code below the header (imports, argparse, functions)
is Python-specific. Extra `PURPOSE / WHEN TO RUN / ARGUMENTS / EXAMPLES / INPUT /
OUTPUT / DEPENDENCIES` lines belong in the description block if you want them —
they are optional, not a second header format.

## Structure law

1. `#!/usr/bin/env python3`
2. Banner header
3. `from __future__ import annotations`
4. Imports: stdlib, then third-party, then local (each group sorted)
5. Module constants (`SCREAMING_SNAKE_CASE`)
6. `parse_args() -> argparse.Namespace`
7. Domain functions (type-hinted, docstringed)
8. `run(args) -> int` - core logic, returns exit code
9. `main() -> int` - parse, `try/except KeyboardInterrupt`, `return run(args)`
10. `if __name__ == "__main__": raise SystemExit(main())`

## Style rules

- **Type hints** on every signature and return value.
- **`argparse`** for arguments; never hand-parse `sys.argv`.
- **`pathlib.Path`** for filesystem paths; avoid `os.path` string concatenation.
- **f-strings** only; no `%` or `.format()`.
- Exit via `raise SystemExit(main())`; `main()` returns `int`.
- Catch `KeyboardInterrupt` in `main()`, print clean message to stderr, return 1.
- No bare `except:`; catch specific exceptions.
- No mutable default arguments.
- Standard library only unless the user approves a dependency (then list it in `DEPENDENCIES`).
- Keep `# === Title 'Quoted' ===` section banners; do not rewrite them unless asked.
- Docstrings on every public function (`parse_args`, `run`, `main`).

## Headless / cron scripts

Silent by default: no prints, no progress chatter, clean exit code only. Interactive CLIs may use structured output.

## Gates

```bash
python3 -m py_compile path/to/script.py
# ruff / mypy when available; justify remaining warnings
```

- Full script only; path + size in chat after write.
- Bump `Ver` on rewrite; write a version-bumped sibling, do not overwrite source unless asked.
