```markdown
# Literary AI Project

## Phase 1 Implementation

### Core Pipeline
- passes.py: Project setup (Pass 0) and story skeleton (Pass 1)
- orchestrator.py: Deterministic workflow + repair loop wiring

### CLI Commands
- `literary-ai plan`: Run Pass 0 (project setup)
- `literary-ai draft`: Run Pass 1 (story skeleton)

### Roadmap
Phase 2:
1. Integrate Ollama model selection per role (planner/writer)
2. Implement checker integration (continuity.py, style.py)
3. Expand repair loop with validation logic
4. Add advanced CLI features and documentation
```