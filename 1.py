from tkinter import *


def add_label():
    Label(root, text="New label", padx='30', pady='20', fg='white',bg="gray").pack(side = BOTTOM, fill=X)


root = Tk()
root.geometry("300x500")

Label(root, text="Just test", padx='30', pady='0').pack(side = BOTTOM)
Button(root, text="Click me!", command=add_label).pack()
root.mainloop()