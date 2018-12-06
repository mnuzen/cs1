# Part A: Exercises

# 1.

def union(setA, setB):
    '''Takes in two sets and returns their union as another set.'''
    setR = set()
    for a in setA:
        setR.add(a)
    for b in setB:
        setR.add(b)
    return setR

def intersection(setA, setB):
    '''Takes in two sets and returns their intersection as another set.'''
    setR = set()
    for a in setA:
        if a in setB:
            setR.add(a)
    return setR

def difference(setA, setB):
    '''Takes in two sets and returns the difference of the two sets as another
    set.'''
    setR = set()
    for a in setA:
        if a not in setB:
            setR.add(a)
    return setR

def mySum(*nums):
    '''Takes in a random number of arguments and returns their sum.'''
    ret = 0
    try: 
        for num in nums:
            ret += int(num)
            if num <= 0:
                raise ValueError("Arguments must be greater than 0.")
        return ret            
    except ValueError:
        raise TypeError("Arguments must be integers.")
        
def myNewSum(*nums):
    '''Takes in a single list of positive integers and returns the sum of the list.'''
    ret = 0
    try:
        for num in nums:
            ret += int(num)
            if num <= 0:
                raise ValueError("Arguments must be greater than 0.")
            for n in nums:
                if type(num) != int:
                    raise TypeError("All arguments must be integers.")
        return ret
    except ValueError:
        raise TypeError("Arguments must be integers.")

def myOpReduce(lst, **kwargs):
    '''Takes in a list of integers and a keyword argument called op.'''
    ret = 0
    try:
        if op == "+":
            for l in lst:
                ret += int(l)
            return ret
        elif op == "*":
            for l in lst:
                ret *= int(l)
            return ret
        elif op == "max":
            ret = max(lst)
            return ret
        elif type(op) != str:
            raise TypeError("Op needs to be a string.")
        else:
            raise ValueError("You must have a valid keyword argument.")
    
# Part B: Pitfalls: Exception Handling

# 1. 
# The code should be able to distinguish between which key value does not
# exist. Right now, the code only tells you that some key does not exist. To fix
# this, the code should be written as:
# try: 
#     d1 = dict[key1]
# except KeyError:
#     raise KeyError("Key1 does not exist.")
# try: 
#     d2 = dict[key2]
# except KeyError:
#     raise KeyError("Key2 does not exist.")
# return d1 + d2

# 2.
# After except KeyError: the line should read:
# raise KeyError('key not found!', file=sys.stderr)
# rather than just simplying printing out the error. 

# 3. 
# The KeyError needs to include some message, like:
# raise KeyError('key not found!', file=sys.stderr)

# 4.
# The KeyError should include a message and should also be raised as a KeyError:
#  try:
#       val1 = dict[key1]
#   except KeyError:   
#       raise KeyError("Key1 not found.")
#   try:
#       val2 = dict[key2]
#   except KeyError:
#       raise KeyError("Key2 not found.")
#   return val1 + val2

# 5.
# Raising an error and the error message should occur on the same line:
# if n < 0:
#       raise ValueError('n must be >= 0', file=sys.stderr)

# 6. 
# Raising an error should come before printint an error:
# if n < 0:
#       raise ValueError('n must be >= 0', file=sys.stderr)

# 7.
# The errors raised should be indicative of what kind of errors were thrown.
#     if type(x) is not float:
#        raise TypeError('x must be a float')
#     elif x <= 0.0:
#        raise ValueError('x must be > 0.0')