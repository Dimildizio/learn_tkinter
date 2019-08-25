from tkinter import *
import tkinter.messagebox

root = Tk()
menu1 = Menu(root)
root.config(menu = menu1, bg = 'white')
root.config(bg = 'white')
menu1.add_command(label = 'Exit', command = root.destroy)


photo = PhotoImage(file = 'sm.png')

label1 = Label(root, image = photo)
label1.pack()

#canvas, painting in frame, shapes, delete
'''
canvas = Canvas(root, width = 200, height = 100, bg = 'white')
canvas.pack()

blackLine = canvas.create_line(0, 0, 200, 50)
redLine = canvas.create_line(0, 100, 200, 50, fill = 'red')
greenBox = canvas.create_rectangle(25, 40, 130,60, fill = 'green')
canvas.delete(redLine)
canvas.delete(ALL)
'''

#title, messagebox
'''
tkinter.messagebox.showinfo('I am TITLE', 'I really am')
answer = tkinter.messagebox.askquestion('Question 1', 'Are you ready?')
if answer == 'yes':
    print('good for you')
'''
#cascade menu, submenu, separator, assign command
'''
def doNothing():
        print('hihihi')

menu_1 = Menu(root)
root.config(menu = menu_1)

subMenu = Menu(menu_1)
menu_1.add_cascade(label = 'File', menu = subMenu)
subMenu.add_command(label = 'New project...', command = doNothing)
subMenu.add_command(label = 'New...', command = doNothing)
subMenu.add_separator()
subMenu.add_command(label = 'Exit', command = root.destroy)

editMenu = Menu(menu_1)
menu_1.add_cascade(label = 'Edit', menu = editMenu)
editMenu.add_command(label = 'Redo', command = doNothing)
'''
#toolbar
'''
toolbar = Frame(root, bg = 'blue')
insert_b = Button(toolbar, text = 'insert image', command = doNothing)
insert_b.pack(side = LEFT, padx = 2, pady = 2)
print_b = Button(toolbar, text = 'print it', command = doNothing)
print_b.pack(side = LEFT, padx = 2, pady = 2)
toolbar.pack(side = TOP, fill = X)
frame = Frame(root, width = 300, height = 250)
frame.pack(side = TOP)'''


#statusbar
'''
status = Label(root, text = 'Preapearing to do nothing...', bd = 1, relief = SUNKEN, anchor = W)
status.pack(side = BOTTOM, fill = X)'''


#classes frames, command to function, exit
'''
class Mybuttons:
    def __init__(self, master):
        frame = Frame(master, width = 300, height = 250)
        frame.pack()

        self.button1 = Button(frame, text = 'print me', command = self.printme)
        self.button1.pack(side = LEFT)

        self.quit = Button(frame, text = 'quit', command = master.destroy)
        self.quit.pack(side = BOTTOM)

    def printme(self):
        print('hihihihi')


b = Mybuttons(root)
'''

#multiple events in frame
'''
def leftClick(event):
    print('left')
def rightClick(event):
    print('right')
def middleClick(event):
    print('middle')

frame = Frame(root, width = 300, height = 250)

frame.bind('<Button-1>', leftClick)
frame.bind('<Button-3>', rightClick)
frame.bind('<Button-2>', middleClick)
frame.pack()
button1 = Button(root, text = 'im button')
button1.bind('<Button-1>', middleClick)
button1.pack()
'''
#binding
'''
def printname(event):
    print('Hello')
button_1 = Button(root, text = 'print me')
button_1.bind('<Button-1>', printname)
button_1.pack()
'''

#grid, entry and checkbutton
'''
label1 = Label(root, text = 'Name ')
label2 = Label(root, text = 'Password ')
entry_1 = Entry(root)
entry_2 = Entry(root)

label1.grid(row = 0, sticky = E)
label2.grid(row = 1, sticky = E)

entry_1.grid(row = 0, column = 1)
entry_2.grid(row = 1, column = 1)

c = Checkbutton(root, text = 'Keep me signed in')
c.grid(columnspan = 2)
'''

#Labels and pack orientation
'''
one = Label(root, text = 'One', bg = 'red', fg = 'white')
one.pack()
two = Label(root, text = 'two', bg = 'green', fg = 'black')
two.pack(fill = X)
three = Label(root, text = 'three', bg = 'blue', fg = 'yellow')
three.pack(side = RIGHT, fill = Y)
'''


#Frames and buttons
'''
topFrame = Frame(root)
topFrame.pack()

bottomFrame = Frame(root)
bottomFrame.pack(side = BOTTOM)


button1 = Button(topFrame, text = 'Button1', fg = 'red')
button2 = Button(topFrame, text = 'Button2', fg = 'blue')
button3 = Button(topFrame, text = 'Button3', fg = 'black')
button4 = Button(bottomFrame, text = 'Button4', fg = 'green')
buttons = [button1, button2, button3]

for button in buttons:
    button.pack(side = LEFT)
button4.pack(side = BOTTOM)'''

if __name__ == '__main__':
    root.mainloop()
