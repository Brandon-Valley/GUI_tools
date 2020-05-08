from tkinter import *
import tkinter.ttk as ttk
import threading
import time


# the given message with a bouncing progress bar will appear for as long as func is running, returns same as if func was run normally
# Ex:  run_func_with_loading_popup(lambda: task('joe'), photo_img)  
def run_func_with_loading_popup(func, msg, photo_img = None):
    func_return_l = []
 
    class Main_Frame(object):
        def __init__(self, top):
            print('top of Main_Frame')
            self.func = func
            # save root reference
            self.top = top
            # set title bar
            self.top.title("Loading bar example")
      
            self.msg_lbl = Label(top, text=msg)
            self.msg_lbl.pack()
      
      
#             # start button calls the "initialization" function bar_init, you can pass a variable in here if desired
#     #         self.start_button = ttk.Button(top, text='Start bar', command=lambda: self.bar_init(2500))
#             self.start_button = ttk.Button(top, text='Cancel', command=self.top.destroy)
#             self.start_button.pack()
            
            

      
            # the progress bar will be referenced in the "bar handling" and "work" threads
            self.load_bar = ttk.Progressbar(top)
            self.load_bar.pack()
      
      
            self.bar_init()
              
    #         # run mainloop
    #         self.top.mainloop()
     
        def bar_init(self):
            # first layer of isolation, note var being passed along to the self.start_bar function
            # target is the function being started on a new thread, so the "bar handler" thread
            self.start_bar_thread = threading.Thread(target=self.start_bar, args=())
            # start the bar handling thread
            self.start_bar_thread.start()
     
        def start_bar(self):
            # the load_bar needs to be configured for indeterminate amount of bouncing
            self.load_bar.config(mode='indeterminate', maximum=100, value=0)
            # 8 here is for speed of bounce
            self.load_bar.start(8)
            
    #     def run_func(self):
            # start the work-intensive thread, again a var can be passed in here too if desired
            work_thread_return_l = []
            
            
            self.work_thread = threading.Thread(target=self.work_task, args=())
            self.work_thread.start()
            # close the work thread
            self.work_thread.join()
#             print('work_thread_ret: ', work_thread_ret)
            print(work_thread_return_l)

            
            self.top.destroy()
    #         # stop the indeterminate bouncing
    #         self.load_bar.stop()
    #         # reconfigure the bar so it appears reset
    #         self.load_bar.config(value=0, maximum=0)
     
        def work_task(self):
            func_return = func()
            func_return_l.append(func_return)
#             work_thread_return_l.append(func_return)
    #         for x in range(wait_time):
    #             time.sleep(0.001)
#             global func_return
            
#             print('func_return: ', func_return)
            
            
#             return func()
 

    # create root window
    root = Tk()
    # call Main_Frame class with reference to root as top
    Main_Frame(root)
#     return func_return
     
#     root.after(2, task)
     
    # run mainloop
    root.mainloop() 
    return func_return_l[0]
    
if __name__ == '__main__':
    import time
    def task(i):
        # The window will stay open until this function call ends.
        for x in range(5):
            print('hi: ' + i)
            time.sleep(.5) # Replace this with the code you want to run
        return "this is the func return"
        
    msg = 'running func...'        
    photo_img = None
        
    r = run_func_with_loading_popup(lambda: task('joe'), msg, photo_img)
    print('return of test: ', r)    
     
     
     
     
     
     
     
     
     
     
     
     
     
     