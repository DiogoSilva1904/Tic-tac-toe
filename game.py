# Tic-Tac-Toe game in Python

import tkinter
import random

is_x = False
is_o = False

def main():
    global is_x, is_o
    m = tkinter.Tk()
    m.title('Tic-Tac-Toe')
    m.geometry('800x800')
    #is_x = False
    #is_o = False
    """ for i in range(1,4):
        for j in range(3):
            b = tkinter.Button(m, text=' ', font=('Arial', 60), width=4, height=2)
            b.grid(row=i, column=j) """
    
    x = "X começa"
    o = "O começa"
    vez_x="Vez do X"
    vez_o="Vez do O"
    random_num = random.randint(0, 1)
    if(random_num == 0):
        tkinter.Label(m, text=x, font=('Arial', 20)).grid(row=0 ,column=1)
        is_x = True
    else:
        tkinter.Label(m, text=o, font=('Arial', 20)).grid(row=0, column=1)
        is_o = True

    #print("is-o:", is_o)
    #print("is_x" ,is_x)

    b1 = tkinter.Button(m, text=' ', font=('Arial', 60), width=4, height=2,command=lambda:button_pressed(b1))#button_pressed(b1)) só é chamada quando o botão é clicado
    b1.grid(row=1, column=0)
    b2 = tkinter.Button(m, text=' ', font=('Arial', 60), width=4, height=2,command=lambda:button_pressed(b2))
    b2.grid(row=1, column=1)
    b3 = tkinter.Button(m, text=' ', font=('Arial', 60), width=4, height=2,command=lambda:button_pressed(b3))
    b3.grid(row=1, column=2)
    b4 = tkinter.Button(m, text=' ', font=('Arial', 60), width=4, height=2,command=lambda:button_pressed(b4))
    b4.grid(row=2, column=0)
    b5 = tkinter.Button(m, text=' ', font=('Arial', 60), width=4, height=2,command=lambda:button_pressed(b5))
    b5.grid(row=2, column=1)
    b6 = tkinter.Button(m, text=' ', font=('Arial', 60), width=4, height=2,command=lambda:button_pressed(b6))
    b6.grid(row=2, column=2)
    b7 = tkinter.Button(m, text=' ', font=('Arial', 60), width=4, height=2,command=lambda:button_pressed(b7))
    b7.grid(row=3, column=0)
    b8 = tkinter.Button(m, text=' ', font=('Arial', 60), width=4, height=2,command=lambda:button_pressed(b8))
    b8.grid(row=3, column=1)
    b9 = tkinter.Button(m, text=' ', font=('Arial', 60), width=4, height=2,command=lambda:button_pressed(b9))
    b9.grid(row=3, column=2)
    
    m.grid()

    m.mainloop()

def button_pressed(button):
    global is_x, is_o
    if is_x:
        button.config(text='X', state='disabled')
        is_x = False
        is_o = True
    elif is_o:
        button.config(text='O', state='disabled')
        is_o = False
        is_x = True




def check_result():
    pass

main()
    
