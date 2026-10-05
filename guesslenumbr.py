import tkinter as tk 
import random
from tkinter import messagebox
screen=tk.Tk()
screen.title("guess le number")
screen.configure(bg= "white")
screen.geometry("600x600")


compnum= random.randint(1, 20)

def guessednum():
    global compchoice, souls
    if souls> 0:
        souls= souls-1
        l3.config(text= "Attempts left: " + str(souls))
        usernum= int(e1.get())
        if usernum > compnum:
            hint= "go lower"
        elif usernum < compnum:
            hint= "go higher"
        else:
            hint = "you WONN!!!"
        messagebox.showinfo(souls, hint)
    else:
        messagebox.showinfo(souls, "you ran out of attempts, new game! the number was" + str(compnum))
        screen.destroy()







a= ("Arial", 12)

l1= tk.Label(text= "It is thinking of a number between 1-20, User must take a guess. User has 4 attempts", width= 65, height= 3, bg= "white", fg= "black", font=a)
l1.place(x=10, y= 50)
l2=tk.Label(text= "User must take a guess", width= 20, height= 2, bg= "white", fg= "black", font = a)
l2.place(x= 10, y=150)

e1= tk.Entry(width= 15, bg= "white")
e1.place(x= 250, y= 160)

b1= tk.Button(text= "Guess..?", width= 15, height= 3, bg= "green", fg= "black", command = guessednum)
b1.place(x= 200, y= 250)

souls= 4

l3=tk.Label(text= "Attempts left: " + str(souls), width= 20, height= 2, bg= "white", fg= "red")
l3.place(x= 310, y= 310)

screen.mainloop()