'''
class group
class Student iterator for (subjects) method dict subject:mark
class subject (name, mark)

iter every student in one-direct list of Student in class Student

iter__
next__
'''

from random import randint, shuffle
from tkinter import *
from tkinter import ttk
import tkinter.simpledialog as simpledialog
import tkinter.messagebox as box

LARGE_FONT = ('Times New Roman', 12)

class Myclass(Tk):
    def __init__(self, *args, **kwargs):
        
        Tk.__init__(self, *args, **kwargs)

        Tk.iconbitmap(self, default = 'icon16.ico')
        Tk.wm_title(self, "My group")

        container = Frame(self) #creating mainframe
        container.pack(side = TOP, fill = BOTH, expand = True)
        #positioning mainframe
        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)

        #dict for all frame
        self.frames = {}

        for F in (PageOne, PageTwo, StartPage):
            

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



class StartPage(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        label = Label(self, text = '''

My Group.
This program will create your very own study group\n\n\n
Proceed?''', font = LARGE_FONT)
        label.pack(pady = 10, padx = 10)

        button1 = ttk.Button(self, text = 'Agree', command = lambda: controller.show_frame(PageOne))
        button1.pack(side = LEFT, padx = 55)
        button2 = ttk.Button(self, text = 'Disagree', command = quit)
        button2.pack(side = RIGHT, padx = 55)




        
class PageOne(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        var_1 = StringVar()
        var_2 = StringVar()

        
        def group():
            var1 = int(var_1.get())
            var2 = int(var_2.get())            
            my_group = Group(var1, var2)
            PageTwo.var = my_group
            controller.show_frame(PageTwo)
            
        label = Label(self, text = 'Page One', font = LARGE_FONT, width = 20, height = 2)
        label.pack(pady = 10, padx = 10)
        

        button3 = ttk.Button(self, text = 'generate group', command = group)
        button3.pack(side = BOTTOM, pady = 5, padx = 5)
        
        button1 = ttk.Button(self, text = 'back home', command = lambda: controller.show_frame(StartPage))
        button1.pack(side = TOP, pady = 5, padx = 5)

        frame_1 = Frame(self, pady = 5, padx = 5, bd = 3, relief = 'solid')

        
        label_1 = Label(frame_1, text = 'Number of students:', width = 15)
        label_2 = Label(frame_1, text = 'Number of subjects: ', width = 15)
        entry_1 = Entry(frame_1, textvar = var_1, width = 15)
        entry_2 = Entry(frame_1, textvar = var_2, width = 15)


        label_1.grid(row = 0, column = 0)
        label_2.grid(row = 1, column= 0)
        entry_1.grid(row = 0, column = 1)


        entry_2.grid(row = 1, column = 1)
        frame_1.pack(side = BOTTOM)
        entry_1.focus() #doesn't work


class PageTwo(Frame):
    
    var = None
    #life = 0
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        #self.destr()
        self.frame_1 = Frame(self, pady = 5, padx = 5, bd = 3, relief = 'solid')
        self.frame_1.pack(side = BOTTOM)
        #self.scrollbar = Scrollbar(self.frame_1)
        #self.scrollbar.pack(side = RIGHT, fill = Y)
        
        def show_me():
            box.showinfo('Students', PageTwo.var)

        def gentext():
            try:
                my_text = next(self.all_students)

            except StopIteration:
                pass
            
            except AttributeError:
                self.all_students = iter(PageTwo.var)
                gentext()
            else:
                self.label_1 = Label(self.frame_1, text = my_text, justify = LEFT)          
                self.label_1.pack()


            
            
        self.label_1 = Label(self, text = 'This is a Group page', width = 15)
        self.label_1.pack(side = TOP)
        self.button1 = ttk.Button(self, text = 'back home', command = lambda: controller.show_frame(StartPage))
        self.button1.pack(side = TOP, pady = 5, padx = 5)
        self.button2 = ttk.Button(self, text = 'Show Group', command = show_me)
        self.button2.pack(side = TOP)
        self.button3 = ttk.Button(self, text = 'Student', command = gentext)
        self.button3.pack(side = TOP)


##    def destr(self): #doesn't work properly
##        if PageTwo.life:
##            self.frame_1.destroy()
##            self.label_1.destroy()
##        for child in self.winfo_children():
##            child.destroy()
    


















class Subject():
    def __init__(self, name, mark = None):
        self.name = name
        self.mark = mark
        self.next = None
        
    def __repr__(self):
        text = self.name + ': ' + str(self.mark)
        return text
    
    
    @classmethod
    def generate(cls, num):
        subjects = ['Math', 'Literature', 'Alcotrash', 'Algebra', 'Killmeplease', 'Warhammer', \
                           'Political problems of systems of international relations and global development ', \
                           'Problems of regional and global security in context of non-proliferation of nuclear weapon', \
                    'Ethno-national factor in international relations', 'Post-bipolar system of international relations', 'Defence against the dark arts',\
                    'Arts', 'Your mom\'s back yard', 'Harvard CSx50']
        
        shuffle(subjects)
    
        for x in range(num):
            yield Subject(subjects.pop(), randint(1,101))


class Student():
    def __init__(self, name):
        self.name = name
        self.next = None
        self.total_subj = 0
        
        #subj = {Subject('Bablap',100}
        #self.subjects = {subj:subj.marks}
        
        self.first_subj = None
        self.current_subj = None


        
    def __repr__(self):
        try:
            text = f'Student: {self.name}\nSubjects:\n'
            self.current_subj = self.first_subj
            while True:
                text += '\t'+str(self.__next__())+'\n'
        except StopIteration:
            pass
        finally:
            return text


    def change_mark(self, subject, mark):
            current_subj = self.first_subj
            while current_subj:
                if current_subj.name == subject:
                    current_subj.mark = mark
                    return current_subj
                else:
                    current_subj = current_subj.next

            
    def del_subj(self, subject_name):
        current = self.first_subj
        if current.name == subject_name:
                self.first_subj = current.next
                self.total_subj -= 1
                return
        while current.next:
            if current.next.name == subject_name:                
                to_del = current.next
                current.next = to_del.next
                self.total_subj -= 1
            else:
                current = current.next

        
    def add_subj(self, subject):
        if not self.first_subj:
            self.first_subj = subject
            return
        current = self.first_subj
        while current.next:
            current = current.next
        current.next = subject

    def __iter__(self):
        self.current_subj = self.first_subj
        return self
    
    def __next__(self):
        current_subj = self.current_subj
        if not current_subj:
            raise StopIteration()
        temp = current_subj
        self.current_subj = current_subj.next
        return temp

    

    @classmethod
    def generate_students(cls, students_num, subject_num):
        name = ['Peter', 'John', 'Bill', 'Wanker', 'Trunk', 'Whiskey', 'X-Ray', 'Philip', 'Vovan', 'India', 'Emperor of Mankind', 'Your grandpa', \
                'His Excellency Ambassador Extraordinary and Plentypotential of Republic of Nigeria Mumbasa Khazishupti', 'Eric Vicious Fart, King of Norway', 'Alpharius']
        shuffle(name)
        
        for x in range(students_num):
            student = Student(name.pop())
            subjects = Subject.generate(subject_num)
            for x in subjects:
                student.add_subj(x)
            yield student


class Group():
    def __init__(self, students, subjects):
        self.head = None
        self.current = self.head
        self.total_students = 0
        self.generate_group(students, subjects)

    def add_it(self, student):
        if not self.head:
            self.head = student
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = student
        self.total_students += 1

    def __iter__(self):
        self.current = self.head
        return self

    def __next__(self):
        if not self.current:
            raise StopIteration()
        temp = self.current
        self.current = self.current.next
        return temp

    def __repr__(self):
        text = ''
        a = self.__iter__()
        for x in range(self.total_students+1):
            text += str(a.__next__())+'\n\n'
        return text

    def del_student(self, student_name):
        current = self.head
        if current.name == student_name:
                self.first_subj = current.next
                self.total_students -= 1
                return
        while current.next:
            if current.next.name == student_name:                
                to_del = current.next
                current.next = to_del.next
                self.total_students -= 1
            else:
                current = current.next
    
    def generate_group(self, students_num, subjects_num):
        for x in Student.generate_students(students_num, subjects_num):
            self.add_it(x)


if __name__ == '__main__':
    root = Myclass()
    root.mainloop()
    #my_group = Group(4,4)
    #print(my_group)
