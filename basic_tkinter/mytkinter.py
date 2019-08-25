from tkinter import *
from tkinter import ttk
from random import randint
from time import sleep

root = Tk()

root.title('Window')

width, height = 200, 100
'''root.geometry(f'{root.winfo_screenwidth()}x{root.winfo_screenheight()}+0+0')
    #f'{width}x{height}+{int(root.winfo_screenwidth()/2-width/2)}+{int(root.winfo_screenheight()/2-height/2)}')
root.resizable(height = False, width = True)'''
root.iconbitmap(default = 'icon16.ico')


#drawing shapes

canvas = Canvas(root, width = 400, height = 400, bg = 'white')
canvas.grid(row = 0, column = 0)

canvas.create_line(160,160,199,199, fill = 'blue', width = 5, arrow = 'last', arrowshape = (15, 20, 10))

canvas.create_line(100,100,300,100,200,300,
                   100,100,fill = 'blue', width = 5)
canvas.create_line(100,100,300,100, 350,300,
                   50, 300, 100,100 ,fill = 'blue', width = 5)





root.mainloop()


#class for custom pages and frames
'''
class Myclass(Tk):
    def __init__(self, *args, **kwargs):
        
        Tk.__init__(self, *args, **kwargs)


        container = Frame(self) #creating mainframe
        container.pack(side = TOP, fill = BOTH, expand = True)
        #positioning mainframe
        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)

        #dict for all frame
        self.frames = {}

        for F in ('PUT FRAMES HERE'):
            

            #creating startpage in mainframe
            frame = F(container, self)
            
            self.frames[F] = frame
            frame.grid(row = 0, column = 0, sticky = 'nsew')

            #making startpage appear
            self.show_frame(F)

    #pushing page into dictionary
    def show_frame(self, c):
        frame = self.frames[c]
        frame.tkraise()
'''
#Full screen
'''root.overrideredirect(1)'''

#abstract expressionism drawing lines
'''
def colours():
    numbers = '0123456789abcdef'

    colour = '#'
    for x in range(6):
        colour += numbers[randint(0, 15)]
    return colour

    
canvas = Canvas(root, width = 400, height = 400, bg = 'white')
canvas.grid(row = 0, column = 0)
for x in range(2000):
    canvas.create_line(randint(0, 400), randint(0, 400) ,randint(0, 400),randint(0,400), fill = colours(), width = randint(0, 10))
    sleep(0.5)
    canvas.update()
'''


#inheritance and passing of frame parameters via dict of self
#(!!!!!!!!!!) 
'''
frame_2 = Frame(root, height = 150, width = 150, relief = RAISED, bd = 8, bg = 'red')
frame_2.grid(row = 1, column = 1)

class MyFrame(Frame):
    def __init__(self, myroot):
        Frame.__init__(self, master = myroot)
        self['height'] = 150
        self['width'] = 150
        self['relief'] = RAISED
        self['bd'] = 8
        self['bg'] = 'red'

frame = MyFrame(root)
frame1 = MyFrame(root)
frame.grid(row = 0, column = 0)
frame1.grid(row = 0, column = 1)

class MyFrame(Frame):
    def __init__(self, my_window):
        Frame.__init__(self, master = my_window)
        self.username = StringVar()
        self.show_me = StringVar()

        self.label_1 = Label(self, text = 'Enter name: ')
        self.entry_1 = Entry(self, textvar = self.username)
        self.button = Button(self, text = 'Click me', command = displayit)
        self.display_label = Label(self, textvar = self.show_me, relief = 'solid')

        self.label_1.grid(row = 0, column = 0)
        self.entry_1.grid(row = 0, column = 1)
        self.button.grid(row = 1, column = 0)
        self.display_label.grid(row = 1, column = 1)
        self.entry_1.focus()
        self.a = self.username

    def displayit(self):
        self.show_me.set('hello '+self.username.get())    

frame_1 = MyFrame(root)
frame_1.grid(row =0, column = 0)


'''


#Frames
#columnspan to merge columns
'''
var_1 = StringVar()
var_2 = StringVar()
var_3 = StringVar()
var_4 = StringVar()
var_5 = StringVar()
var_6 = StringVar()

frame_1 = Frame(root, pady = 5, padx = 5, bd = 3, relief = 'solid')
frame_2 = Frame(root, pady = 5, padx = 5, bd = 3, relief = 'solid')

button_1 = Button(frame_1, text = 'Submit', width = 15)
label_1 = Label(frame_1, text = 'First Name: ', width = 15)
label_2 = Label(frame_1, text = 'Middle Name: ', width = 15)
label_3 = Label(frame_1, text = 'Last Name: ', width = 15)
entry_1 = Entry(frame_1, textvar = var_1, width = 15)
entry_2 = Entry(frame_1, textvar = var_2, width = 15)
entry_3 = Entry(frame_1, textvar = var_3, width = 15)
entry_1.focus()

button_2 = Button(frame_2, text = 'Confirm', width = 15)
label_4 = Label(frame_2, text = 'Country:', width = 15)
label_5 = Label(frame_2, text = 'City:', width = 15)
label_6 = Label(frame_2, text = 'Address:', width = 15)
entry_4 = Entry(frame_2, textvar = var_4, width = 15)
entry_5 = Entry(frame_2, textvar = var_5, width = 15)
entry_6 = Entry(frame_2, textvar = var_6, width = 15)

label_1.grid(row = 0, column = 0)
label_2.grid(row = 1, column= 0)
label_3.grid(row = 2, column = 0)
label_4.grid(row = 0, column = 0)
label_5.grid(row = 1, column = 0)
label_6.grid(row = 2, column = 0)
entry_1.grid(row = 0, column = 1)
entry_2.grid(row = 1, column = 1)
entry_3.grid(row = 2, column = 1)
entry_4.grid(row = 0, column = 1)
entry_5.grid(row = 1, column = 1)
entry_6.grid(row = 2, column = 1)
button_1.grid(row = 3, columnspan = 2)
button_2.grid(row = 3, columnspan = 2)
frame_1.grid(row = 0, column = 0)
frame_2.grid(row = 0, column = 1)
'''


#order of writing defines the order of swithing when Tab pressed
#focus
'''
entry_a = Entry(root, bg = 'red')
entry_b = Entry(root, bg = 'yellow')
entry_c = Entry(root, bg = 'white')

label_a = Label(root, text = 'First Name')
label_b = Label(root, text = 'Middle Name')
label_c = Label(root, text = 'Last Name')
entry_a.grid(row = 0, column = 1)
entry_a.focus()
entry_b.grid(row = 1, column = 1)
entry_c.grid(row = 2, column = 1)
label_a.grid(row = 0, column = 0)
label_b.grid(row = 1, column = 0)
label_c.grid(row = 2, column = 0)
'''


#fahrenheir to celsius converter
#getting text from entry, manipulating and assigining
'''
var_1 = StringVar()
var_2 = StringVar()

def convert():
    var_2.set(str('%.2f' % (
        (int(var_1.get()) -32) * 5 / 9)))

label_1 = Label(root, text = 'Enter Fahrenheit', width = 15)
label_2 = Label(root, text = 'Celcius Temperature', width = 15)
entry_1 = Entry(root, textvar = var_1, width = 15)
label_3 = Label(root, textvar = var_2, width = 15)
button = Button(root, text = 'Convert', width = 15, command = convert)

#adding cursor focus on start of the program
entry_1.focus()

label_1.grid(row = 0, column = 0, pady = 2, padx = 2)
entry_1.grid(row = 0, column = 1, pady = 2, padx = 2)
label_2.grid(row = 1, column = 0, pady = 2, padx = 2)
label_3.grid(row = 1, column = 1, pady = 2, padx = 2)
button.grid(row = 2, column = 0, pady = 2, padx = 2)
'''

#getting input and storing in vars
'''
var_1 = StringVar()
var_2 = StringVar()

def show():
    #get text from  text from entry widget
    var_1.set('Hello ' + var_2.get())
    
label_1 = Label(root, text = 'Please enter your name: ')
button = Button(root, text = 'click me to enter name', command = show)
entry_1 = Entry(root, textvar = var_2)
label_2 = Label(root, textvar = var_1)

label_1.grid(row = 0, column = 0)
button.grid(row = 1, column = 0)
entry_1.grid(row = 0, column = 1)
label_2.grid(row = 1, column = 1)
'''

#grid packs elements accoarding to their positions
'''
label_1 = Label(root, width = 20, height = 3, bg = 'red',)
label_2 = Label(root, width = 20, height = 3, bg = 'green')
button_1 = Button(root, text = 'click me 1')
button_2 = Button(root, text = 'click me 2')

label_1.grid(row = 0, column = 0)
label_2.grid(row = 1, column = 1)
button_1.grid(row = 1, column = 0)
button_2.grid(row = 0, column = 1)
'''

#StringVar() passed as any var upon initiation is same as label[text]
#can't create new key/pair in and existing label 
'''
var_1 = StringVar()

label_1 = Label(root,
                #text = 'Text', 
                font = 'Mistral 20',
                relief = 'solid',
                #textvar = var_1
                )
label_2 = Label(root,
                #text = 'Text', 
                font = 'Mistral 20',
                relief = 'solid',
                textvar = var_1
                )

var_1.set('Hi')
label_2['textvar'] = var_1
label_1['text'] = 'Hello'
var_1.set('Oh')
'''


#justify  - position of the text in the text size whereas
#achor positions text in the laber
#access/change any of the values of label
#by key\pair coz it is dictionary
'''
label_1 = Label(root,
                text = 'spacer', 
                )
label_2 = Label(root,
                text = 'Text\nText Text\nText Text Text', 
                font = 'Times 20',
                bd = 1,
                relief = 'solid',
                anchor = NE,
                width = 15,
                height = 4,
                justify = LEFT
                
                )
label_3 = Label(root,
                text = 'spacer', 
                )
label_4 = Label(root,
                text = 'Text\nText Text\nText Text Text', 
                font = 'Times 20',
                bd = 1,
                relief = 'solid',
                #justify = CENTER,
                anchor = NE,
                width = 20,
                height = 4
                )

#dictionary manipulation
print(label_1['font'])
label_1['bg'] = 'blue'
label_1['text'] = "I'm a new text"
label_1['relief'] = 'ridge'
label_1['bd'] = 8
label_1['width'] = 15
for x in label_1.keys():
    print(x, ':', label_1[x])
'''

#relief = flat, sunken, ridge, raised, solid, groove
#anchor = n,s,e,w,ne,se,nw,sw
#padx,y for pack() and for instance also
'''
label_1 = Label(root,
                text = 'I am\nlabel\none',
                bg = '#DDFFEE', 
                font = 'Times 15 bold',
                height = 5,
                width = 10,
                bd = 1,
                relief = 'flat',
                anchor = 's')

label_2 = Label(root,
                text = 'I am\nlabel\ntwo',
                bg = '#EEDDDD', 
                fg = 'black',
                font = 'Times 15 italic', 
                width = 10,
                borderwidth = 8,
                relief = 'raised',
                anchor = NW,
                padx = 2)

label_3 = Label(root,
                text = 'I am\nlabel\nthree',
                bg = '#DDFFAA', \
                fg = 'blue',
                font = 'Verdana 15',
                width = 20,\
                bd = 1,
                relief = 'solid',
                height = 2,
                pady = 4,
                padx = 20
                )
'''


