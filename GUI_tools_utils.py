import sys

# self.duration: 72 --> '1:12'
def sec_to_min_str(total_sec):
    minutes = int(total_sec / 60)
    seconds = int(total_sec % 60)
    sec_str = str(seconds)
    if len(sec_str) < 2:
        sec_str = '0' + sec_str
    return str(minutes) + ':' + sec_str


# win = master
# really quick and dirty
def center_window(win, og_w = None, og_h = None):

    """
    centers a tkinter window
    :param win: the root or Toplevel window to center
    """
    
    # not tested enough to be confident
    try:
        win.update_idletasks()
        width = win.winfo_width()
        frm_width = win.winfo_rootx() - win.winfo_x()
        win_width = width + 2 * frm_width
        height = win.winfo_height()
        titlebar_height = win.winfo_rooty() - win.winfo_y()
        win_height = height + titlebar_height + frm_width
        x = win.winfo_screenwidth() // 2 - win_width // 2
        y = win.winfo_screenheight() // 2 - win_height // 2
#         win.geometry('{}x{}+{}+{}'.format(width, height, x, y))

        if og_w == None and og_h == None:
            win.geometry('+{}+{}'.format( x, y))
        else:
            win.geometry('{}x{}+{}+{}'.format(og_w, og_h, x, y))
#         win.geometry('+{}+{}'.format(x, y))
        win.deiconify()
    except:
        pass
    

# runs given func and prints any stderr, works on subprocess calls
def print_stderr(func):
    def eprint(*args, **kwargs):
        print(*args, file=sys.stderr, **kwargs)
        
    eprint(func())
        
        
        
        
        