from tkinter import *
from PIL import ImageTk, Image

class Koinex_GUI:
    coinPic = ""

    def bitCoin(self):
        global coinPic
        coinPic = "BTC.png"
        print "Entered BitCoin"
        # root.destroy()
        self.imageWindow(coinPic, "Bitcoin")

    def litCoin(self):
        global coinPic
        coinPic = "LTC.png"
        print "Entered LiteCoin"
        # root.destroy()
        self.imageWindow(coinPic, "Litcoin")

    def rippleCoin(self):
        global coinPic
        coinPic = "XRP.png"
        print "Entered RippleCoin"
        self.imageWindow(coinPic, "Ripplecoin")

    def imageWindow(self, coinPic, name):
        new = Toplevel()
        new.title("Output")
        new.geometry("760x760+0+0")
        new.resizable(width=True, height=True)
        label1 = Label(new, text="%s GRAPH" % name, font=("arial", 20, "bold"), fg="black")
        label1.place(x=10, y=200)
        label1.pack()
        img = Image.open(coinPic)
        img = img.resize((650, 650), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(img)
        panel = Label(new, image=img, width=600, height=600)
        # panel.pack()
        panel.place(x=50, y=50)
        new.mainloop()

    def main(self):
        root = Tk()
        root.title("CrytoCurrency")
        root.geometry("560x260+0+0")
        root.resizable(width=True, height=True)
        Button(root, text="Bitcoin", width=15, height=3, bg="lightblue", command=self.bitCoin).place(x=30, y=100)
        Button(root, text="Litcoin", width=15, height=3, bg="lightblue", command=self.litCoin).place(x=190, y=100)
        Button(root, text="Ripple", width=15, height=3, bg="lightblue", command=self.rippleCoin).place(x=350, y=100)
        root.mainloop()






















