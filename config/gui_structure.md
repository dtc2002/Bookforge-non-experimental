## Literary AI Tool - GUI File Structure

### 1. Main Application Components
- **main.py**:
  - Primary entry point for the application
  - Initializes the main window and core systems
  - Manages application lifecycle
- **SceneList.py**:
  - Manages scene organization and display
  - Handles drag-and-drop scene rearrangement
  - Provides scene metadata overview
- **SceneSliderDelegate.py**:
  - Enables drag-and-drop functionality for scenes
  - Handles visual feedback during rearrangement
  - Supports multiple drag-and-drop modes

### 2. Revision Management
- **RevisionTree.py**:
  - Manages revision history visualization
  - Supports hierarchical revision display
  - Enables dropping items for new revisions
- **Revisions.py**:
  - Handles revision comparison and conflict resolution
  - Provides revision metadata and history
  - Implements compare_revisions() method

### 3. Export System
- **ExportOptions.py**:
  - Manages export configuration settings
  - Provides export format selection
  - Handles export parameter validation
- **ExportFunctions.py**:
  - Contains implementation for export operations
  - Supports multiple export formats
  - Handles file format-specific processing

### 4. Configuration and Settings
- **SettingsManager.py**:
  - Manages user preferences and configurations
  - Provides access to application settings
  - Handles configuration file loading/saving
- **ConfigParser.py**:
  - Parses configuration files for application settings
  - Supports multiple configuration formats
  - Provides default configuration values

### 5. Utility Components
- **Utils.py**:
  - Contains general-purpose helper functions
  - Provides string manipulation and file operations
  - Includes utility functions for data processing
- **Logger.py**:
  - Manages application logging and debugging
  - Provides different logging levels
  - Supports log file rotation and management