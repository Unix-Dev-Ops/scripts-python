# Authoring guide - scripts-python

How to use this skill to produce excellent long-lived Python scripts and tools.

## Mental model

| Layer | Role |
|-------|------|
| **Skill** | Law: structure, header, naming, gates |
| **Template** | `templates/template_base.py` — only skeleton; copy it, never freestyle past it |
| **Brief** (optional) | Intent: args, inputs, outputs, non-goals |
| **Product** | The `.py` you run. Never write it into this skill tree. |

Copy `templates/template_base.py` out, then fill the header and logic.

## Short rewrite (automatic)

User says only: `Rewrite this script: /path/to/foo.py`

Agent must:

1. Load scripts-python from `~/.hermes/skills/software-development/scripts-python/`
2. Read source
3. Write a version-bumped sibling in the **same directory** (`.foo.py` -> `.foo-01.py`)
4. **Issue the write without preamble** (no "Writing now" status essays)
5. `python3 -m py_compile`; report path + size only

User does not list skill files or steps.

## New script

User names a path. Copy the template to that exact filename. Fill Author / Date / Ver / Name / Define, constants, argparse, `run`, `main`. Do not invent a second header system.

Ask one question at a time only when a required field is missing (name, purpose, arguments). Never present a multi-question list.

## Hard gate

```bash
python3 -m py_compile path/to/script.py
```

Agent: full script only; path + size in chat; bump `Ver`; leave section banner comments alone unless asked.

## What good output looks like

- Aligned banner header (Author / Date / Ver / Name / Define)
- `parse_args()` + `run(args) -> int` + `main() -> int` + `raise SystemExit(main())`
- Type hints; `pathlib`; f-strings; specific exception handling; docstrings on public functions
- `--dry-run` for anything that mutates files
- Stdlib only unless a dependency was approved

## What bad output looks like

- Manual `sys.argv` parsing; bare `except:`; mutable default args
- `print()` chatter in a headless/cron script
- Secrets in the script body
- Partial "here's only the changed function"
- A second copy of the template inside the skill
