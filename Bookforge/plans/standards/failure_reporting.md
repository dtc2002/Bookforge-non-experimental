# Failure Reporting

If a task fails after the allowed retry count, PopeBot must report failure clearly.

## Failure report must include

- task ID
- attempted outputs
- validation step that failed
- error summary
- whether one retry was attempted
- recommended next action

## Rules

- Do not silently skip failed validation.
- Do not mark failed work as complete.
- Do not continue to the next task after a blocking failure.