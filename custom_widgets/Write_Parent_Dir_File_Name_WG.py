from tkinter.ttk import *
from tkinter import *
from tkinter import filedialog

# import GUI_tools.custom_widgets.File_System_Browse_WG
# import custom_widgets.File_System_Browse_WG

        # from custom_widgets.File_System_Browse_WG import File_System_Browse_WG
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
            file_path_tb_edit_func = None,# FIX?
        ):

        # Parent Dir File_System_Browse_WG
        parent_dir_fsb_wg = File_System_Browse_WG(
                                                    master = master,
                                                    lbl_txt = parent_dir_lbl_txt, 
                                                    tb_width = parent_dir_tb_width, 
                                                    browse_for = 'dir',  # 'dir' or 'file'
                                                    file_type = None,    # '.jpg', '.mp4', etc...
                                                    init_path = init_parent_dir_path_str, 
                                                    focus_tb_after_browse = focus_parent_dir_tb_after_browse,
                                                    tb_edit_func = parent_dir_tb_edit_func, #FIX?
                                                    browse_btn_txt = browse_btn_txt
                                                )

        self.parent_dir_lbl = parent_dir_fsb_wg.lbl
        self.parent_dir_tb  = parent_dir_fsb_wg.tb
        self.btn = parent_dir_fsb_wg.btn

        # File Name Widgets
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


        if file_path_tb_edit_func != None:

            # Make sure this matches bind_to_edit in Tab
            def bind_to_edit(widget, func):
                widget.bind("<KeyRelease>", func)
                widget.bind("<KeyRelease-BackSpace>", func)
                widget.bind("<KeyRelease-Delete>", func)
                widget.bind("<KeyRelease-space>", func)

            bind_to_edit(self.file_name_tb, file_path_tb_edit_func)


    # # should not be used outside this file
    # def path_tb_browse_btn_clk(self, path_txt_box_widget, browse_for, file_type = None):
    #     #get file path and place it in text box

    #     if browse_for == 'file':
    #         if file_type == None:
    #             file_system_item = filedialog.askopenfilename()

    #         else:
    #             file_system_item = filedialog.askopenfilename(filetypes = (("Images", "*" + file_type), ("All files", "*")))#filetypes = (("Images", '*.png|*.jpg'), ("All files", "*")))#"*" + file_types   #,("Template files", '*.jpg'),
    #     elif browse_for == 'dir':
    #         file_system_item = filedialog.askdirectory()
    #     else:
    #         raise Exception('ERROR:  In Tab.py, in path_tb_browse_btn_clk, invalid value for browse_for: ', browse_for)

    #     if len(file_system_item) != 0: # so if you X out of browse, you dont lose the path you started with
    #         path_txt_box_widget.delete(0, "end")
    #         path_txt_box_widget.insert(END, file_system_item)






def xview_event_handler(e):
    e.widget.update_idletasks()
    e.widget.xview_moveto(1)
    e.widget.unbind('<Expose>')


if __name__ == '__main__':
    import os
    sys.path.insert(1, os.path.join(sys.path[0], '..\\..')) # to import from parent dir
    #from parent dir
    import GUI
    GUI.main()


