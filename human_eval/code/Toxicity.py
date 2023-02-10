# -*- coding: UTF-8 -*-
import sys
print(sys.version_info)
if sys.version_info < (3, 0):
    from Tkinter import *
    import tkMessageBox as messagebox
else:
    from tkinter import *
    import tkinter.messagebox as messagebox

file = open('text_case.txt')
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
        master.title('Document Classification')
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

        frame2 = Frame(master)
        frame2.pack(fill=X)
		
        label1 = Label(frame2, text='Classification')
        label1.grid(row=1, column=0)

        self.label = StringVar()
        label_0 = Radiobutton(frame2, text='Toxic', variable=self.label, value='0', command=self.getlabel)
        label_0.grid(row=1, column=2)
        label_1 = Radiobutton(frame2, text='Non-toxic', variable=self.label, value='1', command=self.getlabel)
        label_1.grid(row=1, column=4)

        label2 = Label(frame2, text='Hardness to classify')
        label2.grid(row=2, column=0)

        self.natural = StringVar()
        natural_0 = Radiobutton(frame2, text='Very Hard', variable=self.natural, value='1', command=self.getnatural)
        natural_0.grid(row=2, column=2)
        natural_1 = Radiobutton(frame2, text='Hard', variable=self.natural, value='2', command=self.getnatural)
        natural_1.grid(row=2, column=4)
        natural_2 = Radiobutton(frame2, text='Average', variable=self.natural, value='3', command=self.getnatural)
        natural_2.grid(row=2, column=6)
        natural_3 = Radiobutton(frame2, text='Easy', variable=self.natural, value='4', command=self.getnatural)
        natural_3.grid(row=2, column=8)
        natural_4 = Radiobutton(frame2, text='Very Easy', variable=self.natural, value='5', command=self.getnatural)
        natural_4.grid(row=2, column=10)
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
        messagebox.showinfo('Description', 'Each question contains two parts. We provide the first part with two choices toxic and non-toxic that you need to figure for each sample. \nFor the second part, we provide with five choices to represent five hardness levels. The five levels are scored from 1 to 5.\n1 Very Hard: Do not know how to label.\n2 Hard: The sample is hard, and the label is possibly wrong.\n3 Average: The sample can be classified but it may be wrong. \n4 Easy: The sample is easy to classify, and the label is probably correct.\n5 Very Easy: The sample is very easy to classify without hesitation.')   # 显示对话框
    def about(self):
        messagebox.showinfo('about', 'In this survey, you will be invited to answer classification question and reflect the hardness you feel when you finish the classification question.')   # 显示对话框



    def getnatural(self):
        natural = self.natural.get()
        print(natural)
    def getlabel(self):
        label = self.label.get()
        print(label)


    # 提交
    def allsubmit(self):
        with open(r'classification.txt', 'a') as f:
            f.write(str(self.i))
            f.write(' ')
            f.write(self.label.get())
            f.write(' ')
            f.write(self.natural.get())
            f.write('\n')
        self.i += 1
        if self.i >= 40:    
            messagebox.showinfo('Success', 'Congratulations! Finish all the questions!')
        else:    
            messagebox.showinfo('Finish question', 'Finish question'+str(self.i)+'\n 40 questions in total.')
            self.text.delete(1.0, "end")
            self.text.insert("insert", data[self.i])

TkDemo()

