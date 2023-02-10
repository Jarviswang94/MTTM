# -*- coding: UTF-8 -*-
import sys
#print(sys.version_info)
if sys.version_info < (3, 0):
    from Tkinter import *
    import tkMessageBox as messagebox
else:
    from tkinter import *
    import tkinter.messagebox as messagebox

file = open('text_case2.txt')
data = []
for line in file:
    each_line = line.split()
    text = ' '.join(each_line[4:])
    #print(text)
    data.append(text)
file.close()

class TkDemo():
    def __init__(self):
        self.i = 0
        master = Tk()
        master.title('Realistic Scoring')
        menubar = Menu(master)
        master.config(menu=menubar)
        helpmenu = Menu(menubar,tearoff=0)
        menubar.add_cascade(label='Help', menu=helpmenu)
        helpmenu.add_command(label='About', command=self.about)
        helpmenu.add_command(label='Instruction', command=self.description)
        

        textmenu = Menu(menubar,tearoff=0)
        menubar.add_cascade(label='<---Please read About and Instruction!!!', menu=helpmenu)

        title = Label(master, text='User Study', font='15', bg='white', fg='red')
        title.pack()
        

        frame1 = Frame(master)
        frame1.pack(fill=X)

        self.text = Text(frame1, width=150, height=30)
        #text.pack()
        self.text.grid(row=1, column=0)
        self.text.insert("insert", data[0])
        self.text.insert("insert", "\n")
        self.text.insert("insert", "===========================================================\n")
        self.text.insert("insert", data[1])

        frame2 = Frame(master)
        frame2.pack(fill=X)

        label2 = Label(frame2, text='Consistency of the sample')
        label2.grid(row=1, column=0)

        self.natural = StringVar()
        natural_0 = Radiobutton(frame2, text='Not Realistic', variable=self.natural, value='1', command=self.getnatural)
        natural_0.grid(row=1, column=2)
        natural_1 = Radiobutton(frame2, text='Barely Realistic', variable=self.natural, value='2', command=self.getnatural)
        natural_1.grid(row=1, column=4)
        natural_2 = Radiobutton(frame2, text='Average', variable=self.natural, value='3', command=self.getnatural)
        natural_2.grid(row=1, column=6)
        natural_3 = Radiobutton(frame2, text='Realistic', variable=self.natural, value='4', command=self.getnatural)
        natural_3.grid(row=1, column=8)
        natural_4 = Radiobutton(frame2, text='Very Realistic', variable=self.natural, value='5', command=self.getnatural)
        natural_4.grid(row=1, column=10)
        # frame9
        frame9 = Frame(master)
        frame9.pack()
        submit = Button(frame9, text='提交', command=self.allsubmit)
        submit.grid()


        master.mainloop()

    def newfile(self):
        self.file = open(r'test.txt', 'w')
        self.file.close()
    def openfile(self):
        f = open(r'test.txt', 'r')
        try:
            f_read=f.read()
            #f_read_decode=f_read.decode('utf-8')
            print(f_read)
        finally:
            f.close()

    def red(self):
        self.group['bg'] = 'red'
    def blue(self):
        self.group['bg'] = 'blue'
    def yellow(self):
        self.group['bg'] = 'yellow'
    def nomal(self):
        self.group['bg'] = 'SystemButtonFace'


    def description(self):
        messagebox.showinfo('Description', 'For each question, we provide one question with five choices to represent five Realistic levels. The five levels are scored from 1 to 5.\n1 – Not Realistic (Very Bad): I have never seen this kind of transforming.\n2 – Barely Realistic (Bad): I have barely seen this kind of transforming.\n3 – Average (Average): I have seen this kinds of transforming, but not commonly seen. \n4 – Realistic (Good): I have  seen this kind of transforming. It is commonly used transforming.\n5 – Very Realistic (Excellent): I have  seen this kind of transforming. It is very popular transforming.')   # 显示对话框
    def about(self):
        messagebox.showinfo('about', '1. In this survey, you are invited to answer questions to measure the realistic of perturbation samples.\n2. Realistic accounts for criteria that it is real-world uses’ behavior of transforming texts.')   # 显示对话框



    def getnatural(self):
        natural = self.natural.get()
        print(natural)


    # 提交
    def allsubmit(self):
        with open(r'consistent.txt', 'a') as f:
            f.write(str(self.i))
            f.write(' ')
            f.write(self.natural.get())
            f.write('\n')
        self.i += 1
        if self.i >= 20:    
            messagebox.showinfo('Success', 'Congratulations! Finish all the questions!')
        else:    
            messagebox.showinfo('Finish question', 'Finish question'+str(self.i)+'\n 20 questions in total.')
            self.text.delete(1.0, "end")
            self.text.insert("insert", data[2*self.i])
            self.text.insert("insert", "\n")
            self.text.insert("insert", "===========================================================\n")
            self.text.insert("insert", data[2*self.i+1])

TkDemo()

