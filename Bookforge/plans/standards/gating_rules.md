# Gating Rules

Every task must pass validation gates.

Minimum gates:

File Gate
- required files created
- correct directory placement

Schema Gate
- JSON artifacts validate against schemas

Test Gate
- smoke tests pass

CLI Gate
- CLI executes successfully

If validation fails:

1 retry allowed.

If retry fails:

Stop task and report failure.