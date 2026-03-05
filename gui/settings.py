import tkinter

class SettingsWindow:
    def __init__(self, root):
        self.settings_window = tkinter.Toplevel(root)
        self.settings_window.title("Settings")
        self.create_widgets()

    def create_widgets(self):
        tkinter.Label(self.settings_window, text="Project Settings").pack(pady=10)
        tkinter.Button(self.settings_window, text="Save Settings").pack(pady=5)