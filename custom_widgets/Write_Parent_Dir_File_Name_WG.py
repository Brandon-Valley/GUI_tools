from tkinter.ttk import *
from tkinter import *
# from . File_System_Browse_WG import File_System_Browse_WG

if __name__ == '__main__':
    from File_System_Browse_WG import File_System_Browse_WG
else:
    from . File_System_Browse_WG import File_System_Browse_WG


class Write_Parent_Dir_File_Name_WG():
    def __init__(
            self,
            master,
            parent_dir_lbl_txt,
            file_name_lbl_txt,
            parent_dir_tb_width = None,
            file_name_tb_width = None,
            init_parent_dir_path_str = None,
            init_file_name = None,
            write_file_path_updated_func = None,
            focus_parent_dir_tb_after_browse = False,
            browse_btn_txt = 'Browse...',
            parent_dir_tb_edit_func = None,# FIX?
            file_path_tb_edit_func = None,# FIX? - rename
            write_file_path_descrip_lbl_text = "Output will be written to:",# FIX?
        ):

        def _parent_dir_path_tb_updated(event=None):
            _update_write_file_path_lbl()

            if parent_dir_tb_edit_func:
                parent_dir_tb_edit_func()

        # Parent Dir File_System_Browse_WG
        parent_dir_fsb_wg = File_System_Browse_WG(
                                                    master = master,
                                                    lbl_txt = parent_dir_lbl_txt, 
                                                    tb_width = parent_dir_tb_width, 
                                                    browse_for = 'dir',  # 'dir' or 'file'
                                                    file_type = None,    # '.jpg', '.mp4', etc...
                                                    init_path = init_parent_dir_path_str, 
                                                    focus_tb_after_browse = focus_parent_dir_tb_after_browse,
                                                    tb_edit_func = _parent_dir_path_tb_updated, #FIX?
                                                    browse_btn_txt = browse_btn_txt
                                                )

        self.parent_dir_lbl = parent_dir_fsb_wg.lbl
        self.parent_dir_tb  = parent_dir_fsb_wg.tb
        self.btn = parent_dir_fsb_wg.btn

        ################################################################################################################
        # File Name Widgets
        ################################################################################################################
        def _file_name_tb_updated(event=None):
            _update_write_file_path_lbl()

            if file_path_tb_edit_func:
                file_path_tb_edit_func()

        self.file_name_lbl = Label(master, text = file_name_lbl_txt)
        self.file_name_tb = Entry(master, width=file_name_tb_width)

        # Fill default txt if needed
        if init_file_name:
            self.file_name_tb.insert(END, init_file_name)

        # Binds
        self.file_name_tb.bind('<Expose>', xview_event_handler)   # scrolls text to end if needed
        self.file_name_tb.bind('<Enter>' , xview_event_handler)   # scrolls text to end if needed
        self.file_name_tb.bind('<Leave>' , xview_event_handler)   # scrolls text to end if needed
        self.file_name_tb.bind('<FocusIn>' , xview_event_handler) # scrolls text to end if needed

        # Make sure this matches bind_to_edit in Tab
        def bind_to_edit(widget, func):
            widget.bind("<KeyRelease>", func)
            widget.bind("<KeyRelease-BackSpace>", func)
            widget.bind("<KeyRelease-Delete>", func)
            widget.bind("<KeyRelease-space>", func)

        bind_to_edit(self.file_name_tb, _file_name_tb_updated)

    
        ################################################################################################################
        # File Path Widgets
        ################################################################################################################
        self.write_file_path_descrip_lbl = Label(master, text = write_file_path_descrip_lbl_text)


        write_file_path_str_var= StringVar()
        self.write_file_path_lbl = Label(master, textvariable = write_file_path_str_var)

        def _update_write_file_path_lbl():
            print("_update_write_file_path_lbl")
            self.write_file_path_str = self.parent_dir_tb.get() + "\\" + self.file_name_tb.get()
            write_file_path_str_var.set(self.write_file_path_str)

        _update_write_file_path_lbl()

def xview_event_handler(e):
    e.widget.update_idletasks()
    e.widget.xview_moveto(1)
    e.widget.unbind('<Expose>')


if __name__ == '__main__':
    import os
    import sys
    sys.path.insert(1, os.path.join(sys.path[0], '..\\..\\..')) # to import from parent dir
    #from parent dir
    import gui
    gui.main()


