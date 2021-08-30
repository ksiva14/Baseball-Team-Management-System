#FrontEnd Imports
from tkinter import *
import tkinter.messagebox

#Backend Database Imports

class Player:

    def __init__(self, root):
        self.root = root
        self.root.title("Baseball Team Database Management System")
        self.root.geometry("1350x750+0+0")
        self.root.config(bg="cadet blue")

        PID = StringVar()
        FirstName = StringVar()
        LastName = StringVar()
        Age = StringVar()
        Position = StringVar()
        Batting_Avg = StringVar()
        ERA = StringVar()

        #MaineFram Using Widget
        MainFrame = Frame(self.root, bg="cadet blue")
        MainFrame.grid()

        TitFrame = Frame(MainFrame, bd=2, padx=54, pady=8, bg="Ghost White", relief = RIDGE)
        TitFrame.pack(side=TOP)

        self.lblTit = Label(TitFrame, font=('arial', 47, 'bold'), text="Baseball Team Management System", bg="Ghost White")
        self.lblTit.grid()

        ButtonFrame = Frame(MainFrame, bd=2 , width=1350, height=70, padx=18, pady=10, bg="Ghost White", relief=RIDGE)
        ButtonFrame.pack(side=BOTTOM)

        DataFrame = Frame(MainFrame, bd=1 , width=1300, height=400, padx=20, pady=20, bg="Ghost White", relief=RIDGE)
        ButtonFrame.pack(side=BOTTOM)


        

if __name__ == '__main__':
    root = Tk()
    application = Player(root)
    root.mainloop()
