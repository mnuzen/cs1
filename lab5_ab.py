# Part A
# 1.1:
import math

class Point:
    """Creates Point Objects that have three coordinates: x, y, z."""
    def __init__(self, x, y, z):
        """Initializes x, y, z."""
        self.x = x
        self.y = y
        self.z = z
    
    def distanceTo(self, new_point):
        """Returns distance between two points."""
        x = self.x
        y = self.y
        z = self.z
        return (math.sqrt((new_point.x - x)**2 + (new_point.y - y)**2 \
                          + (new_point.z - z)**2))
    
class Triangle:
    """Creates a triangle with three points."""
    def __init___(self, P1, P2, P3):
        """Initializes triangle."""
        self.p1 = P1
        self.p2 = P2
        self.p3 = P3
        
    def area(self):
        """Returns the area of a triangle."""
        p1 = self.p1
        p2 = self.p2
        p3 = self.p3        
        
        length1 = p1.distanceTo(p2)
        length2 = p2.distanceTo(p3)
        length3 = p3.distanceTo(p1)
        
        s = (length1 + length2 + length3) / 2
        area = sqrt(s * (s - length1) * (s - length2) * (s - length3))
        return area
    
class Averager:
    """Holds a list and returns averages, mins, maxs, etc."""
    def __init__(self):
        """Initializes the averager."""
        self.nums = []
        self.total = sum(self.nums)
        self.n = len(self.nums)
        
    def getTotal(self):
        """Returns total."""
        self.total = sum(self.nums)
        return self.total
        
    def getNums(self):
        """Returns num"""
        return self.nums[:]
    
    def append(self, num):
        """Adds to num"""
        self.nums.append(num)
    
    def extend(self, n_lst):
        """Extends list of numbers"""
        self.nums.extend(n_lst)
        
    def average(self):
        """Returns average"""
        self.total = sum(self.nums)
        self.n = len(self.nums)        
        try:
            return float(self.total / self.n)
        except ZeroDivisionError: #list is empty
            return 0.0
    
    def limits(self):
        """Returns limits"""
        self.n = len(self.nums)                
        if self.n != 0:
            max_n = max(self.nums)
            min_n = min(self.nums)
        else:
            max_n = 0
            min_n = 0
        return (min_n, max_n)
        
# Part B
# 1. The function needs to make sure that the input x is an integer.
# try: 
#     if x > 0:
#         return True
#     else:
#         return False
# except '>' not supported between instances of 'str' and 'int':
#     return "Input is not an integer."

# 2. Location already defines the return value, so you can just return location.
# Using "for i, item" is the same as using a nested loop, so instead, the loop 
# should read:
# for i in range(0,len(lst)):
#     if lst[i] == x:
#     found = True
#     location = i
# return location

# 3. The variable category should be initialized before being used. 
# def categorize(x):
# '''Return a string categorizing the number 'x', which should be
#    an integer.'''
#    if type(x) == int:
#        if x < 0:
#            category = 'negative'
#        if x == 0:
#            category = 'zero'
#        if x > 0 and x < 10:
#            category = 'small'
#        if x >= 10:
#            category = 'large'
#    else:
#        category = 'non-integer.'
#    return category

# 4. You can shorten the entire function by writing:
# def sum_list(lst):
# '''Returns the sum of the elements of a list of numbers.'''
#     answer = int()
#     for i in range(0,len(lst)):
#         answer += lst[i]
#     return answer