from tkinter import *
from tkinter import filedialog
import sys

def GetFile():
    filename = filedialog.asksaveasfilename(initialdir="~", filetypes=(("Text File", "*.txt"),("All Files", "*.*")))
    return filename

def WriteFile(file, con):
    with open(file, 'a') as sf:
        sf.write(con)
        sf.close()
    sys.exit(0)
d = GetFile()


root = Tk()
root.geometry("500x500")
root.title("no see write")

entVar = StringVar()

Ent = Entry(root, textvariable=entVar, font=("Arial", 20), show="*")
Ent.place(x=100, y=100)

EntBut = Button(root, text="Submit and Write", font=("Arial", 20), command=lambda: WriteFile(d, entVar.get()+"\n"))
EntBut.place(x=100, y=200)

root.mainloop()
