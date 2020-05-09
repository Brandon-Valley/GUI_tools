''' -- VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV -- All Utilities Standard Header -- VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV -- '''
import sys, os    ;     sys.path.insert(1, os.path.join(sys.path[0], os.path.dirname(os.path.abspath(__file__)))) # to allow for relative imports, delete any imports under this line

util_submodule_l = ['exception_utils']  # list of all imports from local util_submodules that could be imported elsewhere to temporarily remove from sys.modules

# temporarily remove any modules that could conflict with this file's local util_submodule imports
og_sys_modules = sys.modules    ;    pop_l = [] # save the original sys.modules to be restored at the end of this file
for module_descrip in sys.modules.keys():  
    if any( util_submodule in module_descrip for util_submodule in util_submodule_l )    :    pop_l.append(module_descrip) # add any module that could conflict local util_submodule imports to list to be removed from sys.modules temporarily
for module_descrip in pop_l    :    sys.modules.pop(module_descrip) # remove all modules put in pop list from sys.modules
util_submodule_import_check_count = 0 # count to make sure you don't add a local util_submodule import without adding it to util_submodule_l

''' -- VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV -- All Utilities Standard: Local Utility Submodule Imports  -- VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV -- '''

from util_submodules.exception_utils   import exception_utils as eu       ; util_submodule_import_check_count += 1

''' ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ '''
if util_submodule_import_check_count != len(util_submodule_l)    :    raise Exception("ERROR:  You probably added a local util_submodule import without adding it to the util_submodule_l")
''' ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ '''



import sys
import os
import ctypes

from tkinter.ttk import *
from tkinter import *




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
        
        
def rel_path_to_this_file__to__abs_path__if_not_None(file_obj, rel_path):
    '''
        gtu.rel_path_to_this_file__to__abs_path(__file__, 'imgs//git.png')       

    '''
    if rel_path == None:
        return None
    
    eu.error_if_not__file__(file_obj)
    eu.error_if_not_is_file(rel_path)
    
    return os.path.dirname(os.path.abspath(file_obj)) + '//' + rel_path
        
        
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
    eu.error_if_not__file__(file_obj)
    eu.error_if_param_type_not_in_whitelist(want_duplicate_apps_to_stack_in_toolbar, ['bool'])
        
    if want_duplicate_apps_to_stack_in_toolbar:
        return '_app_id__' + os.path.dirname(os.path.abspath(file_obj)) + '__app_id_' # arbitrary string
    else:
        app_id = '_app_id__{}__{}__app_id_'.format(os.path.dirname(os.path.abspath(__file__)), os.getpid()) # arbitrary string
    

def set_app_id(app_id):
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(app_id)
    
  
def set_tool_bar_image_to_match_iconphoto_if_exists(file_obj, want_duplicate_apps_to_stack_in_toolbar = True ):
    '''
        gtu.set_tool_bar_image_to_match_iconphoto_if_exists(__file__, want_duplicate_apps_to_stack_in_toolbar = True)       
    
        If no iconphoto is set, all this does is set the app_id based on input.
    '''  
    eu.error_if_not__file__(file_obj)
    eu.error_if_param_type_not_in_whitelist(want_duplicate_apps_to_stack_in_toolbar, ['bool'])
    
    app_id = get_app_id_unique_to_this_file(file_obj, want_duplicate_apps_to_stack_in_toolbar)
    set_app_id(app_id)
    
    
def set_iconphoto_if_not_None(master, img_path):
    if img_path == None:
        return 
    
    eu.error_if_param_type_not_in_whitelist(master, ['tkinter.Tk', 'tkinter.Toplevel'])
    eu.error_if_not_is_file(img_path)
    
    photo_img = PhotoImage(file = img_path)
    master.iconphoto(master, photo_img)
    
    
    
''' -- VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV -- All Utilities Standard Footer -- VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV -- '''
sys.modules = og_sys_modules
''' ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ '''
if __name__ == '__main__':    
    print('In Main:  GUI_tools_utils')
    print('End ofMain:  GUI_tools_utils')
    
    
    
    
    
    
    
    
    
    
    
    
        
        