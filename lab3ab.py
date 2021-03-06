# A.1:
def list_reverse(lst):
    """Takes in a list and returns the reverse as a separate list, leaving 
    the original list intact. list_reverse(lst) -> lst2"""
    lst2 = lst[:]
    lst2.reverse()
    return lst2

# A.2:
def list_reverse2(lst):
    """Takes in a list and returns the reverse as a separate list, leaving 
    the original list intact. list_reverse(lst) -> lst2"""
    lst2 = []
    for i in range(len(lst)-1, -1, -1):
        lst2.append(lst[i])
    return lst2

# A.3:
def file_info(txtname):
    """Takes in the name of a text file and returns the number of lines, number
    of words, and number of characters. file_info(txt) -> 1,2,3"""
    f = open(txtname,'r')
    lcount = 0
    wcount = 0
    ccount = 0
    while True:
        line = f.readline()
        if line == "":
            break 
        lcount += 1
        wcount += len(line.split())
        ccount += len(line)
    f.close()
    return lcount, wcount, ccount

# A.4:
def file_info2(txtname):
    """Takes in a file and returns number of lines, words, and characters,
    except in the form of a dictionary."""
    nums = file_info(txtname)
    (lcount, wcount, ccount) = nums
    dic = {"lines": lcount, "words": wcount, "characters": ccount}
    return dic

# A.5:
def longest_line(txtname):
    """Takes in a file and returns the length of the longest file and the line
    itself in the form of a tuple. longest_line(txtname) -> (5,"hello")"""
    longest = ""
    f = open(txtname,'r')
    while True:
        line = f.readline()
        if line == "":
            break
        if len(line) > len(longest):
            longest = line        
    f.close()   
    return len(longest), longest

# A.6:
def sort_words(string):
    """Takes in a string and returns a list of sorted words within that string
    """
    lst = string.split()
    lst.sort()
    return lst

# A.7
# 11011010 = 218, because you begin with the right side and multiply 0 by 2^0.
# then you add 1*2^1, which is 2; and 1*2^3, which is 8; and 1*2^4, which is 16;
# and 1*2^6, which is 64; and 1*2^7, which is 128. 128+64+16+8+2=218.
# the largest eight digit binary number in decimal is 255, or 11111111 in binary

# A.8:
def binaryToDecimal(lst):
    """Takes in a list of numbers representing one binary number and returns
    the decimal value of that number"""
    sum = 0
    lst2 = list_reverse(lst)
    for i in range(len(lst)):
        sum += (lst2[i])*(2**i)
    return sum

# A.9 [Honor Roll]:
def decimalToBinary(integer):
    """Takes in an integer and converts it to a list represent its binary
    equivalent (the list does not have trailing zeros)."""
    lst = []
    while(integer > 0):
        lst.append(integer%2)
        integer = int(integer/2)
    lst2 = list_reverse(lst)
    return lst2
    
# B.2.1:
# 1) This function's name should be more specific than sc: it should be 
# sum of cubes, or something like that. 
# 2) There should be a space between # operators: a * a * a + b * b * b + 
# c * c * c. 
# 3) There should be spaces between the arguments: sc(a, b, c).

# B.2.2: 
# 1) The variables should be easier to read: sum_of_cubes or argument_a.
# 2) There are grammatical typos in commenting.
# 3) The return line should be shorter; less than 80 characters.
# 4) The comment should also have a space after the # and capitalize the R.

# B.2.3:
# 1) There shouldn't be comments preceding code.
# 2) There should be a line separating the two functions.
# 3) The indenting should be even between the two return statements.