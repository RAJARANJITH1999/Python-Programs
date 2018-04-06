from tkinter import *

def calculate():
    temp = int(t_val.get())
    temp = (9/5)*temp + 32
    op_lbl.configure(text = 'Converted Value:{:.1f}'.format(temp))


def clear():
    op_lbl.configure(text='')
    t_val.delete(0,END)

root = Tk()

ip_lbl = Label(text = "Enter Temparature: ",font=('Verdana',12))
op_lbl = Label(font=('Verdana',12))
t_val = Entry(font=('Verdana',12),width=4)

calc_but = Button(text = 'OK',font = ('Verdana',12), command = calculate)
clear_but = Button(text = 'CLEAR',font = ('Verdana',12),command = clear)

ip_lbl.grid(row = 0, column = 0,padx=15,pady=10)
t_val.grid(row = 0, column = 1,padx=15,pady=10)
calc_but.grid(row = 0, column = 2,padx=15,pady=10)
clear_but.grid(row =0, column = 3,padx=15,pady=10)
op_lbl.grid(row=1, column = 0, columnspan = 3,padx=15,pady=10)

root.mainloop()
