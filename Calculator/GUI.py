from tkinter import *
import time

root = Tk()
root.geometry("500x250")
root.title("Calculator")
root.configure(bg = "#202020")

def myClick():
    myLabel = Label(root, text="Button pressed " + input.get(), bg="#181818", fg = "#ff3")
    myLabel.grid(row = 1, column = 0, pady = 10, sticky = "W")

#create label
myLabel = Label(root, text = "Hello")
myLabel2 = Label(root, text = "World")

#Let it appear on the screen
# myLabel.grid(row = 0, column = 0)
# myLabel2.grid(row = 0, column = 1)


#create input fields
input = Entry(root, width = 50, bg = "#181818", fg = "#ff3", insertbackground='#ff3', border = False)
input.grid(row = 1, column = 5, padx = 20, sticky = "W")

#create a button
myButton = Button(root, text="Click me!", command = myClick, bg = "#181818", fg = "#ff3")
myButton.grid(row = 0, column = 0, sticky = "W")

#event loop

if __name__ == "__main__":
    root.mainloop()
