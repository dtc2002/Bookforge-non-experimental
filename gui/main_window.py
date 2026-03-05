import tkinter

class MainWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Literary AI")
        self.create_menu()

    def create_menu(self):
        menu_bar = tkinter.Menu(self.root)
        file_menu = tkinter.Menu(menu_bar, tearoff=0)
        file_menu.add_command(label="Settings", command=self.open_settings)
        menu_bar.add_cascade(label="File", menu=file_menu)
        self.root.config(menu=menu_bar)

    def open_settings(self):
        SettingsWindow(self.root)