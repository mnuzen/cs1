import random

# 4.B.1:
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

# 4.B.2:
def random_position(max_x, max_y):
    """Takes in two integers greater than zero and returns a tuple of two 
    random x y values between 0 and the max x or y respectively."""
    
    assert max_x >= 0, "Input x is not greater than 0."
    assert max_y >= 0, "Input y is not greater than 0."
    
    retx = random.randint(0, max_x)
    rety = random.randint(0, max_y)
    ret = (retx, rety)
    
    return ret

# 4.B.3:
def random_color():
    """Generates a random color value in the format #RRGGBB as a string."""
    r_color = "#"
    for i in range(0,6):
        r_color += random.choice('0123456789abcdef')
    return r_color

# 4.B.4:
def count_values(dic):
    """Takes in a dictionary and returns the number of distinct values in it."""
    lst_v = list(dic.values())
    lst_r = lst_v
    for v in lst_v:
        if lst_v.count(v) != 1:
            for i in range(0,lst_v.count(v)-1):
                lst_r.remove(v)
    return len(lst_r)

# 4.B.5:
def remove_value(dic, val):
    """Takes in a dictionary and removes all instances of value val."""
    lst_keys = list(dic.keys())
    remove = []
    for key in lst_keys:
        if dic[key] == val:
            remove.append(key)
    for r in remove:
        del dic[r]
        
# 4.B.6:

def split_dict(dic):
    """Takes in a dictionary and returns a tuple of two dictionaries sorted by
    keys: one for the first half of the alphabet and one for the second half."""
    dic_am = {}
    dic_nz = {}
    lst_keys = list(dic.keys())
    for key in lst_keys:
        if key[0].lower() >= "a" and key[0].lower() <= "m":
            dic_am[key] = dic[key]
        elif key[0].lower() >= "n" and key[0].lower() <= "z":
            dic_nz[key] = dic[key]        
    return (dic_am, dic_nz)

# 4.B.7:

def count_duplicates(dic):
    """Takes in a dictionary and returns the number of values that appear more 
    than once."""
    vals = list(dic.values())
    lst_vals = []
    count = 0
    for v in vals:
        if vals.count(v) >= 2:
            if v not in lst_vals:
                lst_vals.append(v)
    return len(lst_vals)