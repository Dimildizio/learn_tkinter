'''canvas'''


from tkinter import *
from BFS import *

tk = Tk()
canvas = Canvas(tk, width = 1024, height = 768)
canvas.pack()

tilesize = 64
width = 800
height = 600

gridwidth = width // tilesize
gridheight = height // tilesize

pic = PhotoImage(file = 'bat.png')
pic1 = PhotoImage(file = 'g.png')

a = Object('sm.png', 0,0)

def move(event):
    mydict = {'w':(0,-1),'s':(0,1), 'a':(-1,0), 'd':(1,0)}
    try:
        key = mydict[str(event.char)]
    except:
        return
    else:
        newy, newx = a.pos[0]+key[0], a.pos[1]+key[1]
        if newy <= current_location.maxsize[0] and \
           newx <= current_location.maxsize[1] and \
           a.goto((newy, newx)):
            for x in range(64):
                canvas.move(pic_a,key[0],key[1])

pic = PhotoImage(file = a.pic)
pic1 = PhotoImage(file = 'g.png')


for x in range(16):
    for y in range(12):
        canvas.create_image(32+x*64, 32+y*64, image = pic1)
    
pic_a = canvas.create_image(32,32, image = pic)
canvas.focus_set()
canvas.bind('<Key>', move)
mainloop()







