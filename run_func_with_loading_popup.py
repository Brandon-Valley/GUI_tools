from tkinter import *
import tkinter.ttk as ttk
import threading
import time


# the given message with a bouncing progress bar will appear for as long as func is running, returns same as if func was run normally
# a pb_length of None will result in the progress bar filling the window whose width is set by the length of msg
# Ex:  run_func_with_loading_popup(lambda: task('joe'), photo_img)  
def run_func_with_loading_popup(func, msg, window_title = None, bounce_speed = 8, pb_length = None):
    func_return_l = []
 
    class Main_Frame(object):
        def __init__(self, top, window_title, title, bounce_speed):
            print('top of Main_Frame')
            self.func = func
            # save root reference
            self.top = top
            # set title bar
            self.top.title(window_title)
      
            self.msg_lbl = Label(top, text=msg)
            self.msg_lbl.pack(padx = 10, pady = 5)
      
            # the progress bar will be referenced in the "bar handling" and "work" threads
            self.load_bar = ttk.Progressbar(top)
            self.load_bar.pack(padx = 10, pady = (0,10))
      
            self.bar_init()
              
     
        def bar_init(self):
            # first layer of isolation, note var being passed along to the self.start_bar function
            # target is the function being started on a new thread, so the "bar handler" thread
            self.start_bar_thread = threading.Thread(target=self.start_bar, args=())
            # start the bar handling thread
            self.start_bar_thread.start()
     
        def start_bar(self):
            # the load_bar needs to be configured for indeterminate amount of bouncing
            self.load_bar.config(mode='indeterminate', maximum=100, value=0, length = pb_length)
            # 8 here is for speed of bounce
            self.load_bar.start(bounce_speed)            
#             self.load_bar.start(8)            
            
            self.work_thread = threading.Thread(target=self.work_task, args=())
            self.work_thread.start()
            
            # close the work thread
            self.work_thread.join()

            
            self.top.destroy()
#             # stop the indeterminate bouncing
#             self.load_bar.stop()
#             # reconfigure the bar so it appears reset
#             self.load_bar.config(value=0, maximum=0)
     
        def work_task(self):
            func_return_l.append(func())


    # create root window
    root = Tk()
    
    # call Main_Frame class with reference to root as top
    Main_Frame(root, window_title, bounce_speed, pb_length)
    root.mainloop() 
    return func_return_l[0]
    
if __name__ == '__main__':
    import time
    def task(i):
        # The window will stay open until this function call ends.
        for x in range(10):
            print('hi: ' + i)
            time.sleep(.5) # Replace this with the code you want to run
        return "this is the func return"
        
    msg = 'running func...'        
        
    bounc_speed = 10
    pb_length = 200
    window_title = "Wait"
        
    r = run_func_with_loading_popup(lambda: task('joe'), msg, window_title, bounc_speed, pb_length)

    print('return of test: ', r)    
     
     
     
     
     
     
     
     
     
     
     
     
     
     