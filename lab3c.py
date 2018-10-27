'''
lab3c.py
Simple L-system simulator.
'''

# References: 
#   http://en.wikipedia.org/wiki/L-systems
#   http://www.kevs3d.co.uk/dev/lsystems/
# N.B. http://en.wikipedia.org/wiki/MU_puzzle for midterm?

import math

# ---------------------------------------------------------------------- 
# Example L-systems.
# ---------------------------------------------------------------------- 

# Koch snowflake.
koch = { 'start' : 'F++F++F', 
         'F'     : 'F-F++F-F' }
koch_draw = { 'F' : 'F 1', 
              '+' : 'R 60', 
              '-' : 'L 60' }

# Hilbert curve.
hilbert  = { 'start' : 'A', 
             'A'     : '-BF+AFA+FB-' , 
             'B'     : '+AF-BFB-FA+' }
hilbert_draw = { 'F' : 'F 1', 
                 '-' : 'L 90', 
                 '+' : 'R 90' }

# Sierpinski triangle.
sierpinski = { 'start' : 'F-G-G', 
               'F'     : 'F-G+F+G-F', 
               'G'     : 'GG' }
sierpinski_draw = { 'F' : 'F 1', 
                    'G' : 'F 1', 
                    '+' : 'L 120', 
                    '-' : 'R 120' }

# ---------------------------------------------------------------------- 
# L-systems functions.
# ---------------------------------------------------------------------- 

def update(lsys,l_str):
    """Takes in a dictionary and starting string; then replaces characters in 
    the string with corresponding strings in the dictionary."""
    keys = list(lsys.keys())
    main_string = l_str
    f_str = ""
    for char in main_string:
        if char in keys:
            f_str += lsys[char]
        else:
            f_str += char
    return f_str

def iterate(lsys, n):
    """Takes in an l-system dictionary and the number of times that system 
    should be repeated. Returns a string of n iterations."""
    l_str = lsys['start']
    for i in range(n):
        l_str = update(lsys,l_str)
    return l_str

def lsystemToDrawingCommands(draw, s):
    """Takes in a dictionary of drawing commands and returns the commands
    corresponding to the l-system string taken in."""
    keys = list(draw.keys())
    cmds = []
    for char in s:
        if char in keys:
            cmds.append(draw[char])
    return cmds

def bounds(cmds):
    """Takes in a list of commands and computes the maximum and minimum a turtle
    can travel with that list of commands."""
    xmin = float()
    ymin = float()
    xmax = float()
    ymax = float()
    x = 0
    y = 0
    angle = 0
    for cmd in cmds:
        z = nextLocation(x, y, angle, cmd)
        (x, y, angle) = z
        if x < xmin:
            xmin = x
        if x > xmax:
            xmax = x
        if y < ymin:
            ymin = y
        if y > ymax:
            ymax = y     
    return xmin, xmax, ymin, ymax

def nextLocation(x, y, angle, cmd):
    """Takes in current x, y, angle of the turtle and a new drawing command.
    Implements the drawing command returns new x, y, and angle."""
    cmds = cmd.split()
    angle = angle * (math.pi/180)
    if "L" in cmds:
        cmd_num = int(cmds[1]) * (math.pi/180)
        angle = angle + cmd_num
    elif "R" in cmds: 
        cmd_num = int(cmds[1]) * (math.pi/180)
        angle = angle - cmd_num
    else:
        x += math.cos(angle) * int(cmds[1])
        y += math.sin(angle) * int(cmds[1])
    return x, y, (angle / (math.pi/180)) % 360

def saveDrawing(filename, bounds, cmds):
    """Takes in a file, bounds, and a list of commands. Writes the bounds and
    commands onto separate into the file."""
    file = open(filename, 'w')
    bound = ""
    for b in bounds:
        bound += (str(b) + " ")
    file.write(str(bound))
    for cmd in cmds:
        file.write("\n" + cmd)
    file.close()

def makeDrawings(name, lsys, ldraw, imin, imax):
    '''Make a series of L-system drawings.'''
    print('Making drawings for {}...'.format(name))
    for i in range(imin, imax):
        l = iterate(lsys, i)
        cmds = lsystemToDrawingCommands(ldraw, l)
        b = bounds(cmds)
        saveDrawing('%s_%d' % (name, i), b, cmds)

def main():
    makeDrawings('koch', koch, koch_draw, 0, 6)
    makeDrawings('hilbert', hilbert, hilbert_draw, 1, 6)
    makeDrawings('sierpinski', sierpinski, sierpinski_draw, 0, 10)

