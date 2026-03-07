# PopeBot Execution Guide

PopeBot is responsible for implementing the Bookforge system.

All work must occur under:

Bookforge/

Always reference the directory as:

Bookforge/

(trailing slash required)

---

## Execution Rules

1. Read phase task files under:

Bookforge/plans/tasks/

2. Select the first task with status `todo`.

3. Complete exactly one task at a time.

4. Only modify the files listed in that task's outputs.

5. Run all validation checks defined in the task.

6. If validation passes:
   - commit changes
   - open PR to main

7. If validation fails:
   - attempt one fix
   - rerun validation

8. If validation fails twice:
   - stop task
   - report failure

---

## Scope Rules

PopeBot must not:

- modify files outside `Bookforge/`
- change planning documents unless the task explicitly requires it
- skip validation gates
- implement multiple tasks in a single PR

---

## Task Completion Criteria

A task is considered complete when:

- all required output files exist
- validation passes
- smoke tests pass
- the PR is opened