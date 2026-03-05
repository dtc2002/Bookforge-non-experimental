class ExportSettings:
    def __init__(self):
        self.format = "pdf"
        self.include_metadata = True

    def save_settings(self):
        # Save settings to SQLite store
        pass

    def load_settings(self):
        # Load settings from SQLite store
        pass