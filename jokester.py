import tkinter
import random
winCounter = 1
def startInfiniteLoop():
    global winCounter
    otherFrame = tkinter.Toplevel()
    otherFrame.geometry("1750x500")
    tkinter.Label(otherFrame,text = str(winCounter)).pack()
    otherFrame.focus_force()
    root.focus_force()
    root.after(1, startInfiniteLoop)
    winCounter+=random.randrange(1,1000)

root = tkinter.Tk()
root.after(1, startInfiniteLoop)
root.mainloop()