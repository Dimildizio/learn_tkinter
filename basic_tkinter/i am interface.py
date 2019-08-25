'''tkinter'''

import matplotlib
matplotlib.use('TKAgg')

from tkinter import *
from tkinter import ttk


LARGE_FONT = ('Times New Roman', 12)


class Myclass(Tk):
    def __init__(self, *args, **kwargs):
        
        Tk.__init__(self, *args, **kwargs)

        Tk.iconbitmap(self, default = 'icon16.ico')
        Tk.wm_title(self, "I'm frame")

        container = Frame(self) #creating mainframe
        container.pack(side = TOP, fill = BOTH, expand = True)
        #positioning mainframe
        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)

        #dict for all frame
        self.frames = {}

        for F in (PageThree, PageTwo, PageOne, StartPage):
            

            #creating startpage in mainframe
            frame = F(container, self)
            
            self.frames[F] = frame
            frame.grid(row = 0, column = 0, sticky = 'nsew')

            #making startpage appear
            self.show_frame(F)

    def show_frame(self, c):
        frame = self.frames[c]
        frame.tkraise()



class StartPage(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        label = Label(self, text = 'StartPage', font = LARGE_FONT, bg = 'white', width = 20, height = 5)
        label.pack(pady = 10, padx = 10)
        
        button3 = ttk.Button(self, text = 'visit page 3', command = lambda: controller.show_frame(PageOne))
        button3.pack(side = BOTTOM, pady = 5, padx = 5)
        button2 = ttk.Button(self, text = 'visit page 2', command = lambda: controller.show_frame(PageTwo))
        button2.pack(side = BOTTOM, pady = 5, padx = 5)
        button1 = ttk.Button(self, text = 'visit page 1', command = lambda: controller.show_frame(PageOne))
        button1.pack(side = BOTTOM, pady = 5, padx = 5)


        
class PageOne(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        
        label = Label(self, text = 'Page One', font = LARGE_FONT, bg = 'white', width = 20, height = 5)
        label.pack(pady = 10, padx = 10)
        
        button1 = ttk.Button(self, text = 'back home', command = lambda: controller.show_frame(StartPage))
        button1.pack(side = BOTTOM, pady = 5, padx = 5)
        button3 = ttk.Button(self, text = 'page three', command = lambda: controller.show_frame(PageThree))
        button3.pack(side = BOTTOM, pady = 5, padx = 5)
        button2 = ttk.Button(self, text = 'page two', command = lambda: controller.show_frame(PageTwo))
        button2.pack(side = BOTTOM, pady = 5, padx = 5)       
        
class PageTwo(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        
        label = Label(self, text = 'Page Two', font = LARGE_FONT, bg = 'white', width = 20, height = 5)
        label.pack(pady = 10, padx = 10)
        
        button1 = ttk.Button(self, text = 'back home', command = lambda: controller.show_frame(StartPage))
        button1.pack(side = BOTTOM, pady = 5, padx = 5)
        button3 = ttk.Button(self, text = 'page three', command = lambda: controller.show_frame(PageThree))
        button3.pack(side = BOTTOM, pady = 5, padx = 5)
        button2 = ttk.Button(self, text = 'page one', command = lambda: controller.show_frame(PageOne))
        button2.pack(side = BOTTOM, pady = 5, padx = 5)

        
class PageThree(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        
        label = Label(self, text = 'Page three', font = LARGE_FONT, bg = 'white', width = 20, height = 5)
        label.pack(pady = 10, padx = 10)
        
        button1 = ttk.Button(self, text = 'back home', command = lambda: controller.show_frame(StartPage))
        button1.pack(side = BOTTOM, pady = 5, padx = 5)
        button3 = ttk.Button(self, text = 'page two', command = lambda: controller.show_frame(PageTwo))
        button3.pack(side = BOTTOM, pady = 5, padx = 5) 
        button2 = ttk.Button(self, text = 'page one', command = lambda: controller.show_frame(PageOne))
        button2.pack(side = BOTTOM, pady = 5, padx = 5)
      
        


if __name__ == '__main__':
    app = Myclass()
    app.mainloop()
            
    
