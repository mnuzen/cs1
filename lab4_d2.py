from tkinter import *

def draw_square(canvas, color, width, pos_tup):
    """ """
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
    """all other code
    call draw 4x i guess"""
    root = Tk()
    root.geometry('800x600')
    c = Canvas(root, width = 800, height = 600)
    c.pack()
    
    draw_square(c, 'red', 50, (25,25))
    draw_square(c, 'green', 50, (775,25))
    draw_square(c, 'blue', 50, (25,575))
    draw_square(c, 'yellow', 50, (775,575)) 
    
    root.bind('<q>', quit)
    root.mainloop()    
