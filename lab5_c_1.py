from tkinter import *
import random

# Graphics commands.
# create global list

def draw_circle(canvas, color, pos_tup):
    ''' '''
    # choose a random diameter
    # draw a circle with global color?
    # center = mouse click
    # store circles in a list or something
    
def random_color():
    '''Generates a random color value in the format #RRGGBB as a string.'''
    r_color = "#"
    for i in range(0,6):
        r_color += random.choice('0123456789abcdef')
    return r_color

def random_size():
    '''Takes in integers, one bigger than the other, and returns
    another random  integer in between them.'''
    r = random.randint(10, 50)
    return r

# Event handlers.

def key_handler(event):
    '''Handle key presses.'''
    if event == '<q>':
        root.bind('<q>', quit)
        
    if event == '<c>':
        color = random_color()
       
    if event == '<x>':
        # clear list of circles

def button_handler(event):
    '''Handle left mouse button click events.'''
    # take in position of the mouse button click
    k

if __name__ == '__main__':
    root = Tk()
    root.geometry('800x800')
    canvas = Canvas(root, width=800, height=800)
    canvas.pack()

    # put in a random color

    # Bind events to handlers.
    root.bind('<Key>', key_handler)
    canvas.bind('<Button-1>', button_handler)

    # Start it up.
    root.mainloop()

