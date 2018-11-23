from tkinter import *
import random
    
def draw_circle(canvas, color, x, y):
    '''Takes in a canvas, color, and a position in the form of a 
    tuple and creates a circle on given canvas. Generates random radius.'''
    global lst
    r = random.randint(10, 50)
    # create circle list
    circ = canvas.create_circle(x, y, r, fill=color, \
                                       outline=color)  
    lst.append(circ)
    return circ
    
def random_color():
    '''Generates a random color value in the format #RRGGBB as a string.'''
    r_color = "#"
    for i in range(0,6):
        r_color += random.choice('0123456789abcdef')
    return r_color

# Event handlers.

def key_handler(event):
    '''Handle key presses.'''
    if event.keysym == '<q>':
        root.bind('<q>', quit)
        
    if event.keysym == '<c>':
        color = random_color()
       
    if event.keysym == '<x>':
        # clear list of circles
        for circle in lst:
            canvas.delete(circle)

def button_handler(event):
    '''Handle left mouse button click events.'''
    # take in position of the mouse button click
    global x0, y0
    x0 = event.x
    y0 = event.y

if __name__ == '__main__':
    global root
    root = Tk()
    root.geometry('800x800')
    global canvas
    canvas = Canvas(root, width=800, height=800)
    canvas.pack()
        
    # Generate initial random color
    r = random_color()

    # Bind events to handlers.
    root.bind('<Key>', key_handler)
    canvas.bind('<Button-1>', button_handler)
    
    # Generate circles
    draw_circle(canvas, r, x0, y0)

    # Start it up.
    root.mainloop()

