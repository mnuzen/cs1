from tkinter import *
import random

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
   
def random_color():
    """Generates a random color value in the format #RRGGBB as a string."""
    r_color = "#"
    for i in range(0,6):
        r_color += random.choice('0123456789abcdef')
    return r_color

def random_size(num1, num2):
    """Takes in two even integers, one bigger than the other, and returns
    another random even integer in between them."""
    
    assert num1 >= 0 and num2 >= 0, "Numbers must be non-negative."
    assert num1%2 == 0 and num2%2 == 0, "Integers must be even numbers."
    assert num1 < num2, "First number must be smaller than second."
    r = random.randint(num1, num2)
    if r%2 != 0:
        r -= 1
    assert r%2 == 0, "Output number is not even."
    return r

def random_position(max_x, max_y):
    """Takes in two integers greater than zero and returns a tuple of two 
    random x y values between 0 and the max x or y respectively."""
    
    assert max_x >= 0, "Input x is not greater than 0."
    assert max_y >= 0, "Input y is not greater than 0."
    retx = random.randint(0, max_x)
    rety = random.randint(0, max_y)
    ret = (retx, rety)
    return ret
   
if __name__ == '__main__':
    root = Tk()
    root.geometry('800x800')
    c = Canvas(root, width = 800, height = 800)
    c.pack()
    
    for i in range(0,50):
        color = random_color()
        size = random_size(20,150)
        pos = random_position(800,800)
        draw_square(c, color, size, pos)
        
    root.bind('<q>', quit)
    root.mainloop()    
