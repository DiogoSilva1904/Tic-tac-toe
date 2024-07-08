# Tic-Tac-Toe game in Python

import tkinter
import random

is_x = False
is_o = False
vez_x="Vez do X"
vez_o="Vez do O"
m = tkinter.Tk()
num_jogadas = 0

def main():
    global is_x, is_o
    m.title('Tic-Tac-Toe')
    m.geometry('700x700')
    
    x = "X começa"
    o = "O começa"
    random_num = random.randint(0, 1)
    if(random_num == 0):
        tkinter.Label(m, text=x, font=('Arial', 20)).grid(row=0 ,column=1)
        is_x = True
    else:
        tkinter.Label(m, text=o, font=('Arial', 20)).grid(row=0, column=1)
        is_o = True

    b1 = tkinter.Button(m, text=' ', font=('Arial', 60), width=4, height=2,command=lambda:button_pressed(b1,[b1,b2,b3,b4,b5,b6,b7,b8,b9]))#button_pressed(b1)) só é chamada quando o botão é clicado
    b1.grid(row=1, column=0)
    b2 = tkinter.Button(m, text=' ', font=('Arial', 60), width=4, height=2,command=lambda:button_pressed(b2,[b1,b2,b3,b4,b5,b6,b7,b8,b9]))
    b2.grid(row=1, column=1)
    b3 = tkinter.Button(m, text=' ', font=('Arial', 60), width=4, height=2,command=lambda:button_pressed(b3,[b1,b2,b3,b4,b5,b6,b7,b8,b9]))
    b3.grid(row=1, column=2)
    b4 = tkinter.Button(m, text=' ', font=('Arial', 60), width=4, height=2,command=lambda:button_pressed(b4,[b1,b2,b3,b4,b5,b6,b7,b8,b9]))
    b4.grid(row=2, column=0)
    b5 = tkinter.Button(m, text=' ', font=('Arial', 60), width=4, height=2,command=lambda:button_pressed(b5,[b1,b2,b3,b4,b5,b6,b7,b8,b9]))
    b5.grid(row=2, column=1)
    b6 = tkinter.Button(m, text=' ', font=('Arial', 60), width=4, height=2,command=lambda:button_pressed(b6,[b1,b2,b3,b4,b5,b6,b7,b8,b9]))
    b6.grid(row=2, column=2)
    b7 = tkinter.Button(m, text=' ', font=('Arial', 60), width=4, height=2,command=lambda:button_pressed(b7,[b1,b2,b3,b4,b5,b6,b7,b8,b9]))
    b7.grid(row=3, column=0)
    b8 = tkinter.Button(m, text=' ', font=('Arial', 60), width=4, height=2,command=lambda:button_pressed(b8,[b1,b2,b3,b4,b5,b6,b7,b8,b9]))
    b8.grid(row=3, column=1)
    b9 = tkinter.Button(m, text=' ', font=('Arial', 60), width=4, height=2,command=lambda:button_pressed(b9,[b1,b2,b3,b4,b5,b6,b7,b8,b9]))
    b9.grid(row=3, column=2)
    
    m.grid()

    m.mainloop()

def button_pressed(button,buttons):
    global is_x, is_o, num_jogadas
    if is_x:
        button.config(text='X', state='disabled')
        is_x = False
        is_o = True
        tkinter.Label(m, text=vez_o, font=('Arial', 20)).grid(row=0 ,column=1)
        check_result(buttons)
        num_jogadas += 1
    elif is_o:
        button.config(text='O', state='disabled')
        is_o = False
        is_x = True
        tkinter.Label(m, text=vez_x, font=('Arial', 20)).grid(row=0 ,column=1)
        num_jogadas += 1
        check_result(buttons)

def check_result(buttons):#buttons=[b1,b2,b3,b4,b5,b6,b7,b8,b9]
    if buttons[0]['text'] == buttons[1]['text'] == buttons[2]['text'] == "X" or buttons[3]['text'] == buttons[4]['text'] == buttons[5]['text'] == "X" or buttons[6]['text'] == buttons[7]['text'] == buttons[8]['text'] == "X" or buttons[0]['text'] == buttons[3]['text'] == buttons[6]['text'] == "X" or buttons[1]['text'] == buttons[4]['text'] == buttons[7]['text'] == "X" or buttons[2]['text'] == buttons[5]['text'] == buttons[8]['text'] == "X" or buttons[0]['text'] == buttons[4]['text'] == buttons[8]['text'] == "X" or buttons[2]['text'] == buttons[4]['text'] == buttons[6]['text'] == "X":
        #print("x ganhou")
        for i in range(9):
            buttons[i].config(state='disabled')
        tkinter.Label(m, text="X ganhou", font=('Arial', 20)).grid(row=0 ,column=1)
        #m.destroy()
    elif buttons[0]['text'] == buttons[1]['text'] == buttons[2]['text'] == "O" or buttons[3]['text'] == buttons[4]['text'] == buttons[5]['text'] == "O" or buttons[6]['text'] == buttons[7]['text'] == buttons[8]['text'] == "O" or buttons[0]['text'] == buttons[3]['text'] == buttons[6]['text'] == "O" or buttons[1]['text'] == buttons[4]['text'] == buttons[7]['text'] == "O" or buttons[2]['text'] == buttons[5]['text'] == buttons[8]['text'] == "O" or buttons[0]['text'] == buttons[4]['text'] == buttons[8]['text'] == "O" or buttons[2]['text'] == buttons[4]['text'] == buttons[6]['text'] == "O":
        #print("o ganhou")
        for i in range(9):
            buttons[i].config(state='disabled')
        tkinter.Label(m, text="O ganhou", font=('Arial', 20)).grid(row=0 ,column=1)
        #m.after(400000, m.destroy)
    elif num_jogadas == 9:
        #print("Empate")
        for i in range(9):
            buttons[i].config(state='disabled')
        tkinter.Label(m, text="Empate", font=('Arial', 20)).grid(row=0 ,column=1)
        #m.after(400000, m.destroy)
    



main()
    
