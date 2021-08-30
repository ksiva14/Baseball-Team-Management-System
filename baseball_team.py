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

        DataFrame = Frame(MainFrame, bd=1 , width=1300, height=400, padx=20, pady=20, bg="cadet blue", relief=RIDGE)
        DataFrame.pack(side=BOTTOM)

        DataFrameL = LabelFrame(DataFrame, bd=1 , width=1000, height=600, padx=20, bg="Ghost White", relief=RIDGE, font=('arial', 20, 'bold'), text='Player Info\n')
        DataFrameL.pack(side=LEFT)

        DataFrameR = LabelFrame(DataFrame, bd=1 , width=450, height=300, padx=31, pady=3,  bg="Ghost White", relief=RIDGE, font=('arial', 20, 'bold'), text='Player Detail')
        DataFrameR.pack(side=RIGHT)

        #Labels and Entry
        self.lblpid = Label(DataFrameL, font=('arial', 17, 'bold'), text="Player ID:", padx=2, pady=2,bg="Ghost White")
        self.lblpid.grid(row=0, column=0, sticky=W)
        self.txtpid = Entry(DataFrameL, font=('arial', 17, 'bold'), textvariable=PID, width=39)
        self.txtpid.grid(row=0, column=1)

        self.lblfname = Label(DataFrameL, font=('arial', 17, 'bold'), text="Firstname:", padx=2, pady=2,bg="Ghost White")
        self.lblfname.grid(row=1, column=0, sticky=W)
        self.txtfname = Entry(DataFrameL, font=('arial', 17, 'bold'), textvariable=FirstName, width=39)
        self.txtfname.grid(row=1, column=1)

        self.lbllname = Label(DataFrameL, font=('arial', 17, 'bold'), text="Lastname:", padx=2, pady=2,bg="Ghost White")
        self.lbllname.grid(row=2, column=0, sticky=W)
        self.txtlname = Entry(DataFrameL, font=('arial', 17, 'bold'), textvariable=LastName, width=39)
        self.txtlname.grid(row=2, column=1)

        self.lblage = Label(DataFrameL, font=('arial', 17, 'bold'), text="Age:", padx=2, pady=2,bg="Ghost White")
        self.lblage.grid(row=3, column=0, sticky=W)
        self.txtage = Entry(DataFrameL, font=('arial', 17, 'bold'), textvariable=Age, width=39)
        self.txtage.grid(row=3, column=1)

        self.lblpos = Label(DataFrameL, font=('arial', 17, 'bold'), text="Position:", padx=2, pady=2,bg="Ghost White")
        self.lblpos.grid(row=4, column=0, sticky=W)
        self.txtpos = Entry(DataFrameL, font=('arial', 17, 'bold'), textvariable=Position, width=39)
        self.txtpos.grid(row=4, column=1)

        self.lblbavg = Label(DataFrameL, font=('arial', 17, 'bold'), text="Batting Average:", padx=2, pady=2,bg="Ghost White")
        self.lblbavg.grid(row=5, column=0, sticky=W)
        self.txtbavg = Entry(DataFrameL, font=('arial', 17, 'bold'), textvariable=Batting_Avg, width=39)
        self.txtbavg.grid(row=5, column=1)

        self.lblera = Label(DataFrameL, font=('arial', 17, 'bold'), text="ERA:", padx=2, pady=2,bg="Ghost White")
        self.lblera.grid(row=6, column=0, sticky=W)
        self.txtera = Entry(DataFrameL, font=('arial', 17, 'bold'), textvariable=ERA, width=39)
        self.txtera.grid(row=6, column=1)

        #Button Widget and Scroll Bar
        scrollbar = Scrollbar(DataFrameR)
        scrollbar.grid(row=0, column=1, sticky='ns')

        playerList = Listbox(DataFrameR, width=41, height=16, font=('arial', 12, 'bold'), yscrollcommand=scrollbar.set)
        playerList.grid(row=0, column=0, padx=8)
        scrollbar.config(command=playerList.yview)

        #Button Widgets
        self.btnAdd = Button(ButtonFrame, text="Add Player", font=('arial', 20, 'bold'), height=1, width=10, bd=4)
        self.btnAdd.grid(row=0, column=0)

        self.btnDisp = Button(ButtonFrame, text="Display", font=('arial', 20, 'bold'), height=1, width=10, bd=4)
        self.btnDisp.grid(row=0, column=1)

        self.btnClear = Button(ButtonFrame, text="Clear", font=('arial', 20, 'bold'), height=1, width=10, bd=4)
        self.btnClear.grid(row=0, column=2)

        self.btnDelete = Button(ButtonFrame, text="Delete", font=('arial', 20, 'bold'), height=1, width=10, bd=4)
        self.btnDelete.grid(row=0, column=3)

        self.btnSearch = Button(ButtonFrame, text="Search", font=('arial', 20, 'bold'), height=1, width=10, bd=4)
        self.btnSearch.grid(row=0, column=4)

        self.btnUpdate = Button(ButtonFrame, text="Update", font=('arial', 20, 'bold'), height=1, width=10, bd=4)
        self.btnUpdate.grid(row=0, column=5)

        self.btnExit = Button(ButtonFrame, text="Exit", font=('arial', 20, 'bold'), height=1, width=10, bd=4)
        self.btnExit.grid(row=0, column=6)




        

if __name__ == '__main__':
    root = Tk()
    application = Player(root)
    root.mainloop()
