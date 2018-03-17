from tkinter import *

class Koinex_GUI:
    def getCoin(self):
        root = Tk()
        root.title("First GUI")
        root.geometry("560x560+0+0")
        heading = Label(root, text="CrytoCurrency", font=("arial", 40, "bold"), fg="steelblue").pack()

        label1 = Label(root, text="Enter the Name of the Coin", font=("arial", 20, "bold"), fg="black").place(x=10,y=200)
        name = StringVar()
        entry_box = Entry(root, textvariable=name, width=25, bg="white").place(x=380, y=210)
        work = Button(root, text="Submit", width=15, height=5, bg="lightblue").place(x=250, y=300)
        root.mainloop()
        return name.get()





