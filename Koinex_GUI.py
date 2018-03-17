from tkinter import *
import

class Koinex_GUI:
    def basicLayout(self):
        root = Tk()
        root.title("First GUI")
        root.geometry("560x560+0+0")

        Label(root, text="CrytoCurrency", font=("arial", 40, "bold"), fg="steelblue").pack()
        Label(root, text="Enter the Name of the Coin", font=("arial", 20, "bold"), fg="black").place(x=10, y=200)

        name = StringVar()
        Entry(root, textvariable=name, width=25, bg="white").place(x=380, y=210)
        Button(root, text="Submit", width=15, height=5, bg="lightblue", command=printFunc).place(x=250, y=300)

        root.mainloop()




