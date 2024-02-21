from pathlib import Path
import subprocess
from tkinter.ttk import *
from tkinter import *

class Show_Logs_Button(Button):
    def __init__(self, master, log_file_path: Path, cnf={}, **kw):

        def _show_logs_btn_clk():
            subprocess.Popen(f'explorer /select,"{log_file_path}"')

        # Ensure to pass both cnf and any keyword arguments to the superclass
        super().__init__(master, cnf=cnf, command=_show_logs_btn_clk, **kw)
        self['text'] = 'Logs'  # Set the button text


# Example usage
if __name__ == "__main__":
    root = Tk()
    log_file_path = Path("C:/path/to/your/logfile.log")
    Show_Logs_Button(root, log_file_path).pack()
    root.mainloop()
