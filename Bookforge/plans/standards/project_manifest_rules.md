# Project Manifest Rules

The project manifest is the authoritative state document for a Bookforge project.

## Responsibilities

The manifest tracks:

- current pipeline stage
- active artifact versions
- artifact history
- project metadata

## Stage transitions

Allowed stage transitions:

brief → skeleton → beats → chapters → scenes → drafting → revision → complete

Stages must advance sequentially unless an operator override occurs.

## Artifact updates

When a new artifact version is created:

1. Append entry to artifact_history
2. Update active_artifacts pointer
3. Update current_stage if appropriate

## Validation

The manifest must always remain schema-valid.

If the manifest becomes invalid, the pipeline must stop.