from tkinter import *
import random
import math
    
def draw_line(canvas, start, end, color):
    '''Draws a colored line at the start and end point.'''
    (startx, starty) = start
    (endx, endy) = end
    line = canvas.create_line(startx, starty, endx, endy, color)
    return line
    
def draw_star(canvas, r, color):
    '''Draws a star of N lines of the same length.'''
    centerx = x0
    centery = y0
    num = (N - 1)/2
    add_angle = (2 * math.pi)/N
    angle = add_angle
    
    for i in range(0, num):
        x = (r * cos(angle)) + centerx
        y = (r * sin(angle)) + centery
        
        angle += add_angle
        
        x1 = (r * cos(angle)) + centerx 
        y1 = (r * sin(angle)) + centery
        
        start = (x, y)
        end = (x1, y1)
        
        draw_line(canvas, start, end, color)
    
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
        for star in lst:
            canvas.delete(star)
            
    if event.keysym == '<plus>':
        N = N + 2
        
    if event.keysym == '<minus>':
        if N > 5:
            N = N - 2
    

def button_handler(event):
    '''Handle left mouse button click events.'''
    # take in position of the mouse button click
    x0 = event.x
    y0 = event.y

if __name__ == '__main__':
    global x0, y0
    global lst
    global N
    
    global root
    root = Tk()
    root.geometry('800x800')
    global canvas
    canvas = Canvas(root, width=800, height=800)
    canvas.pack()
        
    # Generate initial random color
    global r
    r = random_color()
    
    N = random.randrange(5, step=2)

    # Bind events to handlers.
    root.bind('<Key>', key_handler)
    canvas.bind('<Button-1>', button_handler)
    
    # Generate circles
    draw_star(canvas, r, x0, y0)

    # Start it up.
    root.mainloop()

