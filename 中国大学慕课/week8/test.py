from tkinter import *


def processOK():
    print('this button is clicked')
def processCancel():
    print('Cancel button is Clicked')


tk = Tk()
lablel = Label(tk,text='welcome to python Tkinter')

buttonOK = Button(tk,text='OK',color='red',command=processOK)
buttonCancel = Button(tk,text='Cancel',fg='blue',command=processCancel)


lablel.pack()
buttonOK.pack()
buttonCancel.pack()

tk.mainloop()