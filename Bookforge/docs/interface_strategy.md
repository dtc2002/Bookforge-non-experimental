# Interface Strategy

Bookforge begins with a CLI only as a temporary operator surface.

The CLI exists to:
- bootstrap the engine
- run tests
- create projects
- execute pipeline stages
- support development and validation

The CLI is not the final user experience.

A GUI is planned in a later phase and must call the same underlying services rather than duplicating engine logic.