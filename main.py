from gui.main_window import MainWindow
from llm_integration.llm_connector import LLMConnector
from content_generator.serial_planner import SerialPlanner
import tkinter

root = tkinter.Tk()
app = MainWindow(root)
root.mainloop()