from tkinter import *
from tkinter import messagebox

root= Tk()
root.title('TIC-TAC-TOE----Furkan')

count = 0
check = True

def disable_buttons():
    b1.config(state=DISABLED)
    b2.config(state=DISABLED)
    b3.config(state=DISABLED)
    b4.config(state=DISABLED)
    b5.config(state=DISABLED)
    b6.config(state=DISABLED)
    b7.config(state=DISABLED)
    b8.config(state=DISABLED)
    b9.config(state=DISABLED)

def won():
    global winner
    winner = False

    if b1["text"] == "X" and b2["text"] == "X" and b3["text"] == "X":
        b1.config(bg="red")
        b2.config(bg="red")
        b3.config(bg="red")
        winner = True
        messagebox.showinfo("Game","X wins!")
        disable_buttons()
    elif b4["text"] == "X" and b5["text"] == "X" and b6["text"] == "X":
        b4.config(bg="red")
        b5.config(bg="red")
        b6.config(bg="red")
        winner = True
        messagebox.showinfo("Game","X wins!")
        disable_buttons()
    elif b7["text"] == "X" and b8["text"] == "X" and b9["text"] == "X":
        b7.config(bg="red")
        b8.config(bg="red")
        b9.config(bg="red")
        winner = True
        messagebox.showinfo("Game","X wins!")
        disable_buttons()
    elif b1["text"] == "X" and b4["text"] == "X" and b7["text"] == "X":
        b1.config(bg="red")
        b4.config(bg="red")
        b7.config(bg="red")
        winner = True
        messagebox.showinfo("Game","X wins!")
        disable_buttons()
    elif b2["text"] == "X" and b5["text"] == "X" and b8["text"] == "X":
        b2.config(bg="red")
        b5.config(bg="red")
        b8.config(bg="red")
        winner = True
        messagebox.showinfo("Game","X wins!")
        disable_buttons()
    elif b3["text"] == "X" and b6["text"] == "X" and b9["text"] == "X":
        b3.config(bg="red")
        b6.config(bg="red")
        b9.config(bg="red")
        winner = True
        messagebox.showinfo("Game","X wins!")
        disable_buttons()
    elif b1["text"] == "X" and b5["text"] == "X" and b9["text"] == "X":
        b1.config(bg="red")
        b5.config(bg="red")
        b9.config(bg="red")
        winner = True
        messagebox.showinfo("Game","X wins!")
        disable_buttons()
    elif b3["text"] == "X" and b5["text"] == "X" and b7["text"] == "X":
        b3.config(bg="red")
        b5.config(bg="red")
        b7.config(bg="red")
        winner = True
        messagebox.showinfo("Game","X wins!")
        disable_buttons()
    elif b1["text"] == "O" and b2["text"] == "O" and b3["text"] == "O":
        b1.config(bg="blue")
        b2.config(bg="blue")
        b3.config(bg="blue")
        winner = True
        messagebox.showinfo("Game","O wins!")
        disable_buttons()
    elif b4["text"] == "O" and b5["text"] == "O" and b6["text"] == "O":
        b4.config(bg="blue")
        b5.config(bg="blue")
        b6.config(bg="blue")
        winner = True
        messagebox.showinfo("Game","O wins!")
        disable_buttons()
    elif b7["text"] == "O" and b8["text"] == "O" and b9["text"] == "O":
        b7.config(bg="blue")
        b8.config(bg="blue")
        b9.config(bg="blue")
        winner = True
        messagebox.showinfo("Game","O wins!")
        disable_buttons()
    elif b1["text"] == "O" and b4["text"] == "O" and b7["text"] == "O":
        b1.config(bg="blue")
        b4.config(bg="blue")
        b7.config(bg="blue")
        winner = True
        messagebox.showinfo("Game","O wins!")
        disable_buttons()
    elif b2["text"] == "O" and b5["text"] == "O" and b8["text"] == "O":
        b2.config(bg="blue")
        b5.config(bg="blue")
        b8.config(bg="blue")
        winner = True
        messagebox.showinfo("Game","O wins!")
        disable_buttons()
    elif b3["text"] == "O" and b6["text"] == "O" and b9["text"] == "O":
        b3.config(bg="blue")
        b6.config(bg="blue")
        b9.config(bg="blue")
        winner = True
        messagebox.showinfo("Game","O wins!")
        disable_buttons()
    elif b1["text"] == "O" and b5["text"] == "O" and b9["text"] == "O":
        b1.config(bg="blue")
        b5.config(bg="blue")
        b9.config(bg="blue")
        winner = True
        messagebox.showinfo("Game","O wins!")
        disable_buttons()
    elif b3["text"] == "O" and b5["text"] == "O" and b7["text"] == "O":
        b3.config(bg="blue")
        b5.config(bg="blue")
        b7.config(bg="blue")
        winner = True
        messagebox.showinfo("Game","O wins!")
        disable_buttons()
    if count == 9 and winner == False:
        messagebox.showinfo("Game","Its a draw!")
        disable_buttons()

def checker(b):
    global count,check
    
    if b["text"] == "" and check == True:
        b["text"] = "X"
        count=count + 1
        check = False
        won()
    elif b["text"] == "" and check == False:
        b["text"] = "O"
        count = count + 1
        check = True
        won()
    else:
        messagebox.showinfo("Tic Tac Toe","It is already clicked,choose another box")


b1=Button(root,width=15,font=('Times 16 bold'),height=7,command=lambda:checker(b1))
b1.grid(row=1,column=1)

b2=Button(root,width=15,height=7,font=('Times 16 bold'),command=lambda:checker(b2))
b2.grid(row=1,column=2)
b3=Button(root,width=15,height=7,font=('Times 16 bold'),command=lambda: checker(b3))
b3.grid(row=1,column=3)
b4=Button(root,width=15,height=7,font=('Times 16 bold'),command=lambda: checker(b4))
b4.grid(row=2,column=1)
b5=Button(root,width=15,height=7,font=('Times 16 bold'),command=lambda: checker(b5))
b5.grid(row=2,column=2)
b6=Button(root,width=15,height=7,font=('Times 16 bold'),command=lambda: checker(b6))
b6.grid(row=2,column=3)
b7=Button(root,width=15,height=7,font=('Times 16 bold'),command=lambda: checker(b7))
b7.grid(row=3,column=1)
b8=Button(root,width=15,height=7,font=('Times 16 bold'),command=lambda: checker(b8))
b8.grid(row=3,column=2)
b9=Button(root,width=15,height=7,font=('Times 16 bold'),command=lambda: checker(b9))
b9.grid(row=3,column=3)


root.mainloop()
