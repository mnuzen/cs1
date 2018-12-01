'''
This module simulates balls bouncing around a canvas.
'''

import math, random, time
from tkinter import *

class BouncingBall:
    '''Objects of this class represent balls which bounce on a canvas.'''

    def __init__(self, canvas, center, radius, color, direction, speed):
        '''
        Create a new ball with a given location, direction, color, and speed.

        Arguments:
          canvas:    the canvas the ball moves on
          center:    the center of the ball in (x, y) pixel coordinates
          radius:    the radius of the ball in pixels
          color:     the color of the ball
          direction: the initial direction the ball is moving
          speed:     the initial speed of the ball
        '''

        x, y = center
        x1 = x - radius
        y1 = y - radius
        x2 = x + radius
        y2 = y + radius
        self.handle = canvas.create_oval(x1, y1, x2, y2,
                        fill=color, outline=color)
        self.canvas = canvas
        self.xmax   = int(canvas.cget('width')) - 1
        self.ymax   = int(canvas.cget('height')) - 1
        self.center = center
        self.radius = radius
        self.color  = color
        self.direction = direction

        # The direction is represented as an angle in degrees
        # (range 0-360), which we convert to radians here.
        # The angle is with respect to the positive x axis,
        # going clockwise around the origin.
        if direction < 0.0 or direction > 360.0:
            raise ValueError('Invalid direction; must be in range [0.0, 360.0]')
        dir_radians = direction * math.pi / 180.0

        # Separate the direction into its x and y coordinates.
        # Flip the sign of the y coordinate because the y coordinate
        # grows downward, not upward.
        self.dirx = math.cos(dir_radians)
        self.diry = -math.sin(dir_radians)

        # Speed is represented as a single non-negative float.
        # Note that non-float speeds will behave poorly.
        if speed < 0.0: 
            raise ValueError('Invalid speed; must be positive')
        self.speed = speed

    def step(self):
        '''
        Move this ball in its current direction with its current speed.  
        Change direction if the edge of the canvas is reached.

        Arguments: none
        Return value: none
        '''

        # TODO: Add your code here. 
        # fix direction of ball movement 
        # make sure added balls still have effective speed and direction
        (x, y) = self.center
        vx = self.speed * self.dirx
        vy = self.speed * self.diry
    
        displacementx = self.displacement(x, vx, self.xmax)
        displacementy = self.displacement(y, vy, self.ymax)        
        
        canvas.move(self.handle, displacementx, displacementy)
            
        x += displacementx
        y += displacementy   
        
        self.center = (x, y)
        (x, y) = self.center
        
        if (x + self.radius > self.xmax) or (x + self.radius < 0):
            self.dirx = self.dirx * -1
        if (y + self.radius > self.ymax) or (y + self.radius < 0):
            self.diry = self.diry * -1
       
    def displacement(self, c, d, cmax):
        '''
        Compute the actual displacement along the x or y dimension,
        taking reflections off the edge into account.  
        
        Arguments:
          c:    the center of the ball (x or y coordinate)
          cmax: the largest value in that direction
          d:    the desired displacement in that direction

        Return value: the computed displacement
        '''

        # TODO: Add your code here. 
        displacement = d
           
        if (c + self.radius + d) > cmax:
            displacement = d - (cmax - c)
        if (c + self.radius + d) < 0:
            displacement = (d - c)
            
        return displacement
            
    def scale_speed(self, scale):
        '''
        Scale the speed of this object.
        
        Arguments: 
          scale: the speed scaling factor

        Return value: none
        '''

        # TODO: Add your code here. 
        self.speed = self.speed * scale

    def delete(self):
        '''
        Remove this object from the canvas.

        Arguments: none
        Return value: none
        '''

        self.canvas.delete(self.handle)

def random_color():
    '''Generates a random color value in the format #RRGGBB as a string.'''
    r_color = "#"
    for i in range(0,6):
        r_color += random.choice('0123456789abcdef')
    return r_color

def random_ball(canvas, rmin, rmax, smin, smax, xmax, ymax):
    '''
    Create and return a ball with a random color, starting position,
    size, direction, and velocity.
    rmin: minimum radius (pixels)
    rmax: maximum radius (pixels)
    smin: minimum speed
    smax: maximum speed
    xmax: maximum x dimension of canvas
    ymax: maximum y dimension of canvas
    '''

    # TODO: Add your code here.
    color = random_color()
    radius = random.randint(rmin, rmax)
    speed = random.randint(smin, smax)
    cx = random.randint(0, xmax)
    cy = random.randint(0, ymax)
    direction = random.randint(0, 360)
    
    return BouncingBall(canvas, (cx, cy), radius, color, direction, speed)

def key_handler(event):
    '''Handle key presses.'''
    global bouncing_balls
    global done
    key = event.keysym
    if key == 'q': 
        done = True
    elif key == 'plus':  # add a ball at a random location
        # TODO: Add your code here.   Use the random_ball function.
        bouncing_balls.append(random_ball(canvas, 10, 60, 5.0, 15.0, 800, 600))
    elif key == 'minus':  # remove a ball from the canvas if there are any
        # TODO: Add your code here.  Use the delete() method on balls.        
        bouncing_balls[0].delete()
    elif key == 'u':  # speed (u)p all bouncing_balls by factor of 1.2
        # TODO: Add your code here.   Use the scale_speed() method on balls.
        for ball in bouncing_balls:
            ball.scale_speed(1.2)
    elif key == 'd':  # slow (d)own all bouncing_balls by factor of 1.2
        # TODO: Add your code here.   Use the scale_speed() method on balls.
        for ball in bouncing_balls:
            ball.scale_speed(-1.2)        
    elif key == 'x':  # delete all bouncing_balls
        # TODO: Add your code here.   Use the delete() method on balls.
        # Adjust the global list of balls accordingly.        
        for ball in bouncing_balls:
            ball.delete()

if __name__ == '__main__':
    root = Tk()
    root.geometry('800x600')
    canvas = Canvas(root, width=800, height=600)
    canvas.pack()
    done = False

    # Bind events to handlers.
    root.bind('<Key>', key_handler)
    
    # Set up some bouncing balls.
    bouncing_balls = []
    for i in range(5):
        bouncing_balls.append(random_ball(canvas, 10, 60, 5.0, 15.0, 800, 600))

    # Start the event loop.
    while not done:
        time.sleep(0.001)  # add a slight delay to smooth out the simulation
        for ball in bouncing_balls:
            ball.step()
        root.update()