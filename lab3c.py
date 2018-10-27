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
    f_str=""
    for char in main_string:
        if char in keys:
            f_str+=lsys[char]
        else:
            f_str+=char
    return f_str

def iterate(lsys, n):
    """Takes in an l-system dictionary and the number of times that system 
    should be repeated. Returns a string of n iterations."""
    l_str = lsys['start']
    for i in range(n):
        l_str = update(lsys,l_str)
    return l_str

def lsystemToDrawingCommands(draw, s):
    """ """
    keys = list(draw.keys())
    cmds = []
    for char in s:
        if char in keys:
            cmds.append(draw[char])
    return cmds

def bounds(cmds):
    '''<docstring>'''
    pass

def nextLocation(x, y, angle, cmd):
    '''<docstring>'''
    pass

def saveDrawing(filename, bounds, cmds):
    '''<docstring>'''
    pass

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

