from tkinter import *
import tkinter.messagebox

root = Tk()
root.title("Tic Tac Toe")

click = True
flag=0

def checker(buttons):
    global click,flag
    if buttons["text"] == " " and click == True:
        buttons["text"] = "X"
        click = False
        flag+=1
    elif buttons["text"] == " " and click == False:
        buttons["text"] = "O"
        click = True
        flag+=1

    # Check if X wins
    if (button1['text'] == 'X' and button2['text'] == 'X' and button3['text'] == 'X' or
        button4['text'] == 'X' and button5['text'] == 'X' and button6['text'] == 'X' or
        button7['text'] == 'X' and button8['text'] == 'X' and button9['text'] == 'X' or
        button1['text'] == 'X' and button5['text'] == 'X' and button9['text'] == 'X' or
        button3['text'] == 'X' and button5['text'] == 'X' and button7['text'] == 'X' or
        button1['text'] == 'X' and button4['text'] == 'X' and button7['text'] == 'X' or
        button2['text'] == 'X' and button5['text'] == 'X' and button8['text'] == 'X' or
        button7['text'] == 'X' and button6['text'] == 'X' and button9['text'] == 'X'):
        tkinter.messagebox.showinfo("CONGRATS", "X WINS!!")
        root.destroy()

    # Check if O wins
    elif (button1['text'] == 'O' and button2['text'] == 'O' and button3['text'] == 'O' or
        button4['text'] == 'O' and button5['text'] == 'O' and button6['text'] == 'O' or
        button7['text'] == 'O' and button8['text'] == 'O' and button9['text'] == 'O' or
        button1['text'] == 'O' and button5['text'] == 'O' and button9['text'] == 'O' or
        button3['text'] == 'O' and button5['text'] == 'O' and button7['text'] == 'O' or
        button1['text'] == 'O' and button4['text'] == 'O' and button7['text'] == 'O' or
        button2['text'] == 'O' and button5['text'] == 'O' and button8['text'] == 'O' or
        button7['text'] == 'O' and button6['text'] == 'O' and button9['text'] == 'O'):
        tkinter.messagebox.showinfo("CONGRATS!", "O WINS!!")
        root.destroy()

    # Check for Tie
    elif (flag==9):
        tkinter.messagebox.showinfo("TIE!!","It's a TIE!")
        root.destroy()

buttons = StringVar()

button1 = Button(root, borderwidth= 10, text=" ", font=('Times 30 bold'), bg='maroon', fg='orange', height=4, width=8, command=lambda: checker(button1))
button1.grid(row=1, column=0, sticky=S+N+E+W)

button2 = Button(root, borderwidth= 10, text=" ", font=('Times 30 bold'), bg='maroon', fg='orange',height=4, width=8, command=lambda: checker(button2))
button2.grid(row=1, column=1, sticky=S+N+E+W)

button3 = Button(root, borderwidth= 10, text=" ", font=('Times 30 bold'), bg='maroon', fg='orange', height=4, width=8, command=lambda: checker(button3))
button3.grid(row=1, column=2, sticky=S+N+E+W)

button4 = Button(root, borderwidth= 10, text=" ", font=('Times 30 bold'), bg='maroon', fg='orange',height=4, width=8, command=lambda: checker(button4))
button4.grid(row=2, column=0, sticky=S+N+E+W)

button5 = Button(root, borderwidth= 10, text=" ", font=('Times 30 bold'), bg='maroon', fg='orange',height=4, width=8, command=lambda: checker(button5))
button5.grid(row=2, column=1, sticky=S+N+E+W)

button6 = Button(root, borderwidth= 10, text=" ", font=('Times 30 bold'), bg='maroon', fg='orange',height=4, width=8, command=lambda: checker(button6))
button6.grid(row=2, column=2, sticky=S+N+E+W)

button7 = Button(root, borderwidth= 10, text=" ", font=('Times 30 bold'), bg='maroon', fg='orange',height=4, width=8, command=lambda: checker(button7))
button7.grid(row=3, column=0, sticky=S+N+E+W)

button8 = Button(root, borderwidth= 10, text=" ", font=('Times 30 bold'), bg='maroon', fg='orange',height=4, width=8, command=lambda: checker(button8))
button8.grid(row=3, column=1, sticky=S+N+E+W)

button9 = Button(root, borderwidth= 10, text=" ", font=('Times 30 bold'), bg='maroon', fg='orange',height=4, width=8, command=lambda: checker(button9))
button9.grid(row=3, column=2, sticky=S+N+E+W)

root.mainloop()