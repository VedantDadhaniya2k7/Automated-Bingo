from tkinter import *
import random
from PIL import ImageTk, Image

# Initialize the window
win = Tk()
win.title("Housie Game Conductor")
win.iconbitmap("GameIcon.ico")

UsedNum = list()

# Define the Function to create a number
def GenNum():
    if len(UsedNum) != 100 :
        newnumcheck = False
        while not newnumcheck:
            newNum = str(random.randrange(0, 100)).replace("-", " ")
            if newNum not in UsedNum and newNum != 0:
                newnumcheck = True
        
        UsedNum.append(newNum)
        NumLbl = Label(win, text=newNum)
        NumLbl.grid(row=1, column=1, ipadx=105)
    else:
        NumLbl = Label(win, text="All numbers used")
        NumLbl.grid(row=1, column=1, ipadx=105)

# Define the function to show all used numbers
def ShowUsed():
    if len(UsedNum) != 0:
        Used = ""
        wordRowCount = 0
        for x in range(1, 101):
            if wordRowCount < 15 and x in UsedNum:
                if int(x) >= 10:
                    Used += str(x) + ", "
                elif int(x) < 10:
                    Used += "0"+ str(x) +", "
                wordRowCount += 1
            elif wordRowCount >= 15:
                Used += "\n" + str(x) + ", "
                wordRowCount = 1
    else:
        Used ="None"
    NewWindow = Toplevel()
    NewWindow.title("Numbers Used")
    UsedLbl = Label(NewWindow, text=Used, font=("Courier", 12)) 
    UsedLbl.grid(row=3, column=0, columnspan=3)

# Initialize the Game Conductor
Img = ImageTk.PhotoImage(Image.open("GameImg.png"))
GameImg = Label(win, image=Img)
GameImg.grid(row=0, column=0, columnspan=2)

NumBtn = Button(win, text="Create a new number", command=GenNum, font=("Courier", 10))
NumBtn.grid(row=1, column=0, ipadx=105)

ShowButton = Button(win, text="Show all used numbers", command=ShowUsed, font=("Courier", 10))
ShowButton.grid(row=2, column=0, columnspan=2)



win.mainloop()