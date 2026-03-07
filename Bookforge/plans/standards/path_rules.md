# Path Rules

All writable work must occur under:

Bookforge/

The path must be referenced exactly as:

Bookforge/

## Rules

- Never omit the trailing slash when referring to the writable root.
- Do not create files outside `Bookforge/`.
- Do not assume missing directories should be created outside the declared skeleton.
- Prefer declared paths over inferred paths.
- If a required path is missing under `Bookforge/`, create it there and nowhere else.