from tkinter import *
root = Tk()
root.geometry('800x600')
c = Canvas(root, width = 800, height = 600)
c.pack()

r = c.create_rectangle(0, 0, 50, 50, fill='red', outline='red')
# the rectangle's upper left hand corner is at 0, 0
# the rectangle's lower right hand corner is at 50, 50
g = c.create_rectangle(750, 0, 800, 50, fill='green', outline='green')
b = c.create_rectangle(0, 550, 50, 600, fill='blue', outline='blue')
y = c.create_rectangle(750, 550, 800, 600, fill='yellow', outline='yellow')

root.bind('<q>', quit)
root.mainloop()