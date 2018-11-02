from tkinter import *

def draw_square(canvas, color, width, pos_tup):
    """Takes in a canvas, color, squre width and a position in the form of a 
    tuple and creates a square on given canvas."""
    half = width/2
    x = 0
    y = 0
    (x, y) = pos_tup
    x1 = x - half
    y1 = y - half
    x2 = x + half
    y2 = y + half
    return canvas.create_rectangle(x1, y1, x2, y2, fill=color, \
                                       outline=color)    
   
if __name__ == '__main__':
    root = Tk()
    root.geometry('800x800')
    c = Canvas(root, width = 800, height = 800)
    c.pack()
    
    draw_square(c, 'red', 100, (50,50))
    draw_square(c, 'green', 100, (750,50))
    draw_square(c, 'blue', 100, (50,750))
    draw_square(c, 'yellow', 100, (750,750)) 
    
    root.bind('<q>', quit)
    root.mainloop()    
