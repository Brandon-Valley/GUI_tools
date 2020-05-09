# self.duration: 72 --> '1:12'
def sec_to_min_str(total_sec):
    minutes = int(total_sec / 60)
    seconds = int(total_sec % 60)
    sec_str = str(seconds)
    if len(sec_str) < 2:
        sec_str = '0' + sec_str
    return str(minutes) + ':' + sec_str


# win = master
def center_window(win):
    """
    centers a tkinter window
    :param win: the root or Toplevel window to center
    """
    win.update_idletasks()
    width = win.winfo_width()
    frm_width = win.winfo_rootx() - win.winfo_x()
    win_width = width + 2 * frm_width
    height = win.winfo_height()
    titlebar_height = win.winfo_rooty() - win.winfo_y()
    win_height = height + titlebar_height + frm_width
    x = win.winfo_screenwidth() // 2 - win_width // 2
    y = win.winfo_screenheight() // 2 - win_height // 2
#     win.geometry('{}x{}+{}+{}'.format(width, height, x, y))
    win.geometry('+{}+{}'.format(x, y))
    win.deiconify()