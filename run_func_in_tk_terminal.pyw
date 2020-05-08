import tkinter
import sys,string



def run_func_in_tk_terminal(func, parent_gui_pid_l_json_path = None):
    class DbgText:
        Dbgtopwin=None
        Dbgwidget=None
        DbgRoot=None
        
        def _kill_topwin(self):
            DbgText.Dbgwidget=None
            if DbgText.Dbgtopwin != None:
                DbgText.Dbgtopwin.destroy()
            DbgText.Dbgtopwin=None
           
        def __init__(self,kind=''):
            self.kind=kind
            self.window=None
            self.widget=None
            self.called=0
            self.hide=0
            self.buffer=''
    
        def __del__(self):
            "On deletion, wait for user to see the output"
            if DbgText.Dbgtopwin != None:
                See()
            self._kill_topwin()
        
        def write(self,charstr):
            "write text to buffer or window"
            if self.hide:
                self.buffer.append(charstr)
            else:
                if self.window == None:
                    if DbgText.Dbgtopwin == None:
                        DbgText.Dbgtopwin=tkinter.Tk()
                        DbgText.Dbgtopwin.protocol('WM_DELETE_WINDOW',Dbg_kill_topwin)
                        DbgText.Dbgwidget=tkinter.Text(DbgText.Dbgtopwin, background = "black", foreground = 'white')
                        DbgText.Dbgwidget.pack(expand=1)
                    top=DbgText.Dbgtopwin
                    wid=DbgText.Dbgwidget
                    
                    
                else:
                    if self.widget == None:
                        self.widget=tkinter.Text(self.window)
                    top=self.window
                    wid=self.widget
                if self.kind != '':
                    ep=wid.index('end')
                    sp=string.split(ep,'.')
                    # determine length of 'previous' line
                    prevl=int(sp[0])
                    tx='\n'
                    if prevl:
                        pl='%d.0' % (prevl-1)
                        tx=wid.get(pl,ep)
                    # if this is start of a new line
                    if tx[0] == '\n':
                        wid.insert('end',self.kind)
                wid.insert('end',charstr)     
            self.called=1
            top.update()
    
    def Dbg_kill_topwin():
        f=DbgText()
        f._kill_topwin()
        
    def Take_stdout():
        "DIsplay stdout in text widget"
        if not isinstance(sys.stdout,DbgText):
            f=DbgText()
            f.prev=sys.stdout
            sys.stdout=f
    
    def Take_stderr():
        "DIsplay stderr in text widget"
        if not isinstance(sys.stderr,DbgText):
            f=DbgText('*')
            f.prev=sys.stderr
            sys.stderr=f
    
        
    def Restore_stdout():
        f=sys.stdout
        if isinstance(f,DbgText):
            sys.stdout=f.prev
            del f
    
    def Restore_stderr():
        f=sys.stderr
        if isinstance(f,DbgText):
            sys.stderr=f.prev
            del f
    
    def Define_Root():
        root=tkinter.Tk()
        root.withdraw()
        DbgText.DbgRoot=root
    
    
    def See():
        db=DbgText()
        if db.Dbgtopwin != None:
            db.Dbgtopwin.mainloop() # loop for me to see
    
    def Take_all():
        "send stderr/stdout to Tkinter text window/widget"
        Take_stdout()
        Take_stderr()
    
    def Restore_all():
        "restore stderr/stdout"
        Restore_stdout()
        Restore_stderr()
    
            
    
#     print('stdout is here')
    Take_stdout()
    

    func()

#     print('')
#     Dbg_kill_topwin()
#     repo_type = 'ip'
#     # local_ip_repo_dir_path = "C:\\Users\\mt204e\\Documents\\test_ip_repo_2_CE4"
#     #     local_ip_repo_dir_path = "C:\\Users\\mt204e\\Documents\\test_ip_repo_2_CE4 - Copy (2)"
#     local_ip_repo_dir_path = "C:\\Users\\mt204e\\Documents\\test_ip_repo_3"
#     repo_remote_url = 'https://ba-bit.web.boeing.com/scm/mnfcf/tsm15.git'
# #     subprocess.call('setup_new_repo.py', shell = True)
#     e = setup_new_repo.setup_new_repo(repo_type, local_ip_repo_dir_path, repo_remote_url, exit )
#     if e != :
#     exit()
    print('here22222222222222')
#     Dbg_kill_topwin()
    
#     import time
#     while(True):
#         time.sleep(1)
#         print('stdout should now be in window')
#         print(' this is the second line')
    input()
    Restore_stdout()
    print('stdout back to original')
    
    Dbg_kill_topwin()
        
    
    
if __name__ == '__main__':
    import setup_new_repo
    repo_type = 'IP'
    # local_ip_repo_dir_path = "C:\\Users\\mt204e\\Documents\\test_ip_repo_2_CE4"
    #     local_ip_repo_dir_path = "C:\\Users\\mt204e\\Documents\\test_ip_repo_2_CE4 - Copy (2)"
    local_ip_repo_dir_path = "C:\\Users\\mt204e\\Documents\\test_ip_repo_3"
    repo_remote_url = 'https://ba-bit.web.boeing.com/scm/mnfcf/tsm15.git'
    #     subprocess.call('setup_new_repo.py', shell = True)
    run_func_in_tk_terminal(lambda: setup_new_repo.setup_new_repo__(repo_type, local_ip_repo_dir_path, repo_remote_url ))
    
    
    
    
    
    
    