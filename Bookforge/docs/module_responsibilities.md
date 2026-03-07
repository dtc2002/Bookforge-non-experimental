# Module Responsibilities

This document exists to prevent architectural drift.

## src/bookforge/config.py
Loads runtime configuration and defaults.

## src/bookforge/ollama_client.py
Handles model calls through Ollama.
No planning logic belongs here.

## src/bookforge/project_manifest.py
Creates, loads, validates, and updates project manifests.

## src/bookforge/artifacts.py
Handles artifact naming, versioning, saving, and path resolution.

## src/bookforge/planning/brief_to_skeleton.py
Transforms a project brief into a story skeleton.

## src/bookforge/planning/skeleton_to_beats.py
Transforms a story skeleton into a beat outline.

## src/bookforge/planning/beats_to_chapters.py
Transforms a beat outline into a chapter plan.

## src/bookforge/planning/planning_review.py
Runs planning assessments and readiness checks.

## src/bookforge/validation/planning_checks.py
Runs non-LLM structural validation and sanity checks.

## tests/smoke/
Contains minimal end-to-end tests proving pipeline viability.

## Rules

- Keep modules narrow.
- Do not mix planning, validation, and storage responsibilities in one file.
- Do not place GUI code inside engine modules.