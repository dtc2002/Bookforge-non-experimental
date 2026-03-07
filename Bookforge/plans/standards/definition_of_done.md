# Definition of Done

A task is done only when all of the following are true:

- required output files exist
- output files are in the correct paths
- code imports successfully
- declared validations pass
- related smoke tests pass if applicable
- no files outside `Bookforge/` were modified unless explicitly allowed
- the pull request includes task ID, summary, files changed, and validation results

A task is not done if:

- code was written but not validated
- files were created in the wrong location
- schema output is invalid
- required fields are missing
- the bot partially implemented multiple tasks in one PR