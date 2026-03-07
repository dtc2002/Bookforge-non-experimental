# Artifact Versioning Rules

Artifacts must never overwrite prior versions.

Instead they must increment version numbers.

Examples:

story_skeleton_v1.json
story_skeleton_v2.json

beat_outline_v1.json
beat_outline_v2.json

chapter_plan_v1.json

The active artifact is tracked in the project manifest.

## Example

project_manifest.json

active_artifacts:

    skeleton: skeleton/story_skeleton_v2.json
    beats: beats/beat_outline_v1.json

Older artifacts remain for traceability.

## When to create new versions

Create a new artifact version when:

- a revision is requested
- validation requires a repair
- operator edits the artifact