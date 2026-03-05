## Literary AI Tool - CLI Command Reference

### 1. Core Commands
- **`create`**:
  - Creates a new document
  - Options: `--title`, `--genre`, `--format`
- **`open`**:
  - Opens an existing document
  - Options: `--path`, `--mode` (read/write)
- **`export`**:
  - Exports the current document
  - Options: `--format`, `--output`, `--settings`

### 2. Revision Management
- **`revlist`**:
  - Lists all revisions of a document
  - Options: `--document`, `--format`
- **`revert`**:
  - Reverts to a specific revision
  - Options: `--revision`, `--force`
- **`merge`**:
  - Merges two revisions
  - Options: `--base`, `--head`, `--output`

### 3. Utility Commands
- **`info`**:
  - Displays document metadata
  - Options: `--document`, `--format`
- **`settings`**:
  - Manages export and format settings
  - Options: `--load`, `--save`, `--reset`
- **`help`**:
  - Displays command help and options
  - Options: `--all`, `--category`

### 4. Advanced Mode
- **`--debug`**:
  - Enables debug output for troubleshooting
- **`--verbose`**:
  - Increases output detail level
- **`--force`**:
  - Overrides safety checks for advanced operations

### 5. Command Examples
```
# Create a new novel document
gui_cli create --title "The Last Horizon" --genre Sci-Fi --format nov

# Export as EPUB
gui_cli export --format epub --output ./exports/last_horizon.epub

# List all revisions of a document
gui_cli revlist --document ./documents/last_horizon.nov

# Revert to revision 123
gui_cli revert --revision 123 --force
```

### 6. CLI Tips
- Use `--help` with any command for detailed options
- Always back up important documents before reverting
- Use the `settings` command to customize export presets
- The `--debug` flag is useful for troubleshooting export issues