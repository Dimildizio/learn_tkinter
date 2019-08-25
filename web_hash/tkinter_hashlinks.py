'''
1. title
2. saves links to website
3. date
4. make hash

resource files
what files to upload
where to save

4.create a class for it
5. create collection (set()) of link class

6. user can change links
7. save to file
8. links unload to program
9. user sees options

10. database
11. model
12. interface save\del\add\change\show
13. search by keywords
'''

from datetime import datetime
import hashlib
from tkinter import *
import tkinter.simpledialog as simpledialog
import tkinter.messagebox as box
from tkinter import ttk


class Mylink():
    def __init__(self, link, title, date = 'now',imhex = 'no'):
        self.link = link
        self.title = title
        if date == 'now':
            date = datetime.now()
        self.date = Mylink.date_to_string(date)
        if imhex == 'no':
            imhex = self.make_hash([self.title, self.date])
        self.im_hash = imhex
        
    def __repr__(self):
        return f'Link: {self.link}\nTitle: {self.title}\nDate: {self.date}\nHash: {self.im_hash}\n'
    
    @staticmethod
    def string_to_date(a_date):
        mydate = datetime.strptime(a_date.strip(), "%H:%M:%S:%f %d/%m/%Y")
        return mydate
    
    @staticmethod
    def date_to_string(a_date):
        mydate = datetime.strftime(a_date, '%H:%M:%S:%f %d/%m/%Y')
        return mydate

    
    def make_hash(self, data):
        im_hash = hashlib.sha256(self.link.encode('utf-8'))
        #so it updates different im_hash each instance created
        lambda x: im_hash.update(x.encode('utf-8')), data
        im_hash = im_hash.hexdigest()
        return im_hash
        


class LinkSet():
    def __init__(self):
        self.im_set = []

    
    def read(self):
        with open('Newtext.txt', 'r') as mytext:
            mylines = mytext.readlines()
            im_list = [x.split(',') for x in mylines]
            all_links = []
            
            for x in im_list:
                olddate = Mylink.string_to_date(x[2])
                new_inst = Mylink(x[0].strip(), x[1].strip(), olddate, x[3].strip())
                all_links.append(new_inst)
        return all_links

    def save(self, links):
        with open('Newtext.txt', 'w') as mytext:
            for anylink in links:
                print(f'{anylink.link}, {anylink.title}, {anylink.date}, {anylink.im_hash}',\
                  file = mytext)

    def addme(self, anylink):
        with open('Newtext.txt', 'a') as mytext:
            print(f'{anylink.link}, {anylink.title}, {anylink.date}, {anylink.im_hash}',\
                  file = mytext)


class Interface():
    
    def create(self, link = 0, title = 0):
        if link == title == 0:
            createlink = [simpledialog.askstring('Link', 'Please input a link')]
            createlink.append(simpledialog.askstring('Title', 'Please input a title'))
        else:
            createlink = [link, title]
        newlink = Mylink(createlink[0], createlink[1])
        im_set.addme(newlink)
        return im_set

    def show(self):
         readlist = LinkSet.read(self)
         return readlist

    def printme(self):
        text = ''
        for x in self.show():
            text+= f'Keyword: {x.title}\nLink: {x.link}\nDate: {x.date}\nHash: {x.im_hash}\n\n'
        box.showinfo('All links', text)
        return 'End of the list'


    def find_by_key(self):
        key = simpledialog.askstring('Search', 'Please input a keyword')
        mylist = self.show()
        for x in mylist:
            if x.title == key:
                return x

            
    def search_command(self):
        text = self.find_by_key()
        if not text:
            text = 'Keyword not found'
        box.showinfo('Search result', text)
        
    def find_index(self, what):
        a = self.show()
        for x in range(len(a)):
            if what.title == a[x].title:
                return x

    def retry(self, func):
        a = box.askretrycancel('Wrong input', 'Try again?', icon = 'warning')
        if a:
            func()
        else:
            return False
            
    def change(self):
        data = self.find_by_key()
        if not data:
            self.retry(self.change)
        else:
            to_change = simpledialog.askstring('Changing', 'Title or Link?').lower()
            if to_change[0] == 'l':
                newlink = simpledialog.askstring('New link', 'Please enter a new link')
                data.link = newlink
            elif to_change[0] == 't':
                newtitle = simpledialog.askstring('New title', 'Please enter a new title')
                data.title = newtitle
            else:
                self.retry(self.change)

            mylist = self.show()          
            myindex = self.find_index(data)   
            mylist[myindex] = data
            im_set.save(mylist)


    def delete(self):
        data = self.find_by_key()
        mylist = self.show()
        myindex = self.find_index(data)
        name = mylist[myindex].title
        del mylist[myindex]
        box.showinfo('Delete', f'{name} successfully deleted')
        im_set.save(mylist)

    def wipe(self):
        im_set.save('')
        
    def clean(self):
        self.wipe()
        box.showinfo('List cleared', 'All data erased')




im_set = LinkSet()
i = Interface()
i.wipe()

websites = [['yahoo.com', 'yahoo'],['www.ya.ru', 'yandex'], ['www.google.com', 'google']]
for x in websites:
    i.create(x[0],x[1])

#mainframe
root = Tk()
root.title('LinksData')
menu1 = Menu(root)
root.config(menu = menu1, bg = 'white')
width,height = 200,240
root.geometry(f'{width}x{height}+{int(root.winfo_screenwidth()/2-width/2)}+{int(root.winfo_screenheight()/2 - height/1.5)}')
root.resizable(width = True, height = False)
root.iconbitmap(default = 'icon16.ico')

#menu exit
menu1.add_command(label = 'Exit', command = root.destroy)

im_message = Label(root,
                   text = 'Choose an option:',
                   bd = 3,
                   relief = 'groove',
                   width = 20,
                   height = 1,
                   bg = '#EEFFFF',
                   fg = '#115511',
                   font = 'Times 12  bold')

im_message.pack(pady = 4)

#buttons
buttonN = ttk.Button(root, text = 'New link', command = i.create, width = 15)
buttonC = ttk.Button(root, text = 'Change', command = i.change, width = 15)
buttonF = ttk.Button(root, text = 'Find link by title', command = i.search_command, width = 15)
buttonP = ttk.Button(root, text = 'Print all links', command = i.printme, width = 15)
buttonD = ttk.Button(root, text = 'Delete a link', command = i.delete, width = 15)
buttonW = ttk.Button(root, text = 'Clear all', command = i.clean, width = 15)
buttons = [buttonN, buttonC, buttonF, buttonP,buttonD, buttonW]
for x in buttons:
    x.pack(pady = 3)



root.mainloop()
