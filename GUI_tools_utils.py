import sys
import os
import ctypes

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
    
    
# this probably dosn't work
# runs given func and prints any stderr, works on subprocess calls
def print_stderr(func):
    def eprint(*args, **kwargs):
        print(*args, file=sys.stderr, **kwargs)
        
    eprint(func())
        
        
        
''' VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV '''
'''                                                                           
        iconphoto and app_id:
        --------------------
        
        If the iconphoto is set but the app_id is not, the image in the top left of the
        Gui window will change to iconphoto (default is tk feather), but the tool bar
        image will not change.
        
        If both the iconphoto and app_id are set, these imgs will match.
'''
''' VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV '''       
    
        

def get_app_id_unique_to_this_file(file_obj, want_duplicate_apps_to_stack_in_toolbar = True):
    '''
        gtu.get_app_id_unique_to_this_file(__file__)       
    
        if 2 GUIs use the same iconphoto, but have different app_ids, they will show as 2 different applications in the tool bar,
        if they use the same app_id, their application windows will stack in the tool bar 
    '''
    
    if want_duplicate_apps_to_stack_in_toolbar:
        return '_app_id__' + os.path.dirname(os.path.abspath(file_obj)) + '__app_id_' # arbitrary string
    else:
        app_id = '_app_id__{}__{}__app_id_'.format(os.path.dirname(os.path.abspath(__file__)), os.getpid()) # arbitrary string
    

  
def set_tool_bar_image_to_match_iconimage_if_exists(file_obj, want_duplicate_apps_to_stack_in_toolbar = True ):
    '''
        gtu.set_tool_bar_image_to_match_iconimage_if_exists(__file__, want_duplicate_apps_to_stack_in_toolbar = True)       
    
        If no iconphoto is set, all this does is set the app_id based on input.
    '''  
    
    app_id = get_app_id_unique_to_this_file(file_obj, want_duplicate_apps_to_stack_in_toolbar)
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(app_id)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
        
        