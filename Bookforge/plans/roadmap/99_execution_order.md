# Execution Order

PopeBot must complete work in this order unless the operator explicitly overrides it.

## Order

1. Phase 0 – Foundation
2. Phase 1 – Story Planning
3. Phase 2 – Scene Packets
4. Phase 3 – Drafting and Validation
5. Phase 4 – Orchestration
6. Phase 5 – GUI
7. Phase 6 – Parallel Runners
8. Phase 7 – Series Support

## Rules

- Do not begin a later phase while required tasks in an earlier phase remain incomplete.
- Do not implement speculative future-phase code unless required for current-phase interfaces.
- Prefer the smallest useful implementation that satisfies current acceptance criteria.