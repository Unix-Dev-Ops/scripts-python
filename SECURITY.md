# Security Policy

## Scope

This repository ships **templates and guidance**, not a running service: one Python
template, a conventions file, and an authoring guide. The threat model is therefore
what the code here *teaches or recommends*, not what it exposes over a network.

## Reporting a vulnerability

Open a **private security advisory** on this repository: Security tab -> *Report a
vulnerability*. It is not public, no issue is created, and you stay anonymous if you
want. There is no email address for this project.

- Acknowledged within **14 days** (single maintainer, not a team).
- The fix lands as an ordinary commit on `main`. This project does not rewrite history.
- No fixed public-disclosure window is promised. Ask, and we'll agree on one.

## What counts as a vulnerability here

Anything the template would let a script do with input it did not author:

- `eval`, `exec`, `compile`, or `pickle.loads` on untrusted data.
- `subprocess` with `shell=True`, or passing unsanitized input as a command list.
- Path joins that follow user-controlled `..` into files the script should not touch.
- Temp files, lock files, or logs written to world-writable paths, where a symlink can win.
- Credentials, tokens, hostnames, or internal paths embedded in script text, arguments, or committed logs.
- Downloads over plaintext, with TLS verify disabled, or from unpinned URLs.
- Loading `.env` or config from a directory another user controls.
- Catching `Exception` (or bare `except:`) and continuing after a security-relevant failure.

## Out of scope

- Bugs in your own private tools — this repo has no visibility into them.
- Anything that already assumes the attacker has a shell on the target host.
- Resource exhaustion / denial of service.

## What is enforced before merge

- CI runs `python3 -m py_compile` and `ruff check` against
  `templates/template_base.py` on every push and pull request, so the skeleton
  cannot ship broken.
- The template uses `argparse` (not `sys.argv` slicing), contains no `eval` /
  `exec`, catches `KeyboardInterrupt` in `main()`, and exits via
  `raise SystemExit(main())`.
