# c.1.1: 9 - 3 --> 6
# c.1.2: 8 * 2.5 --> 20.0
# c.1.3: 9 / 2 --> 4.5
# c.1.4: 9 / -2 --> -4.5
# c.1.5: 9 % 2 --> 1
# c.1.6: 9 % - 2 --> -1
# c.1.7: -9 % 2 --> 1
# c.1.8: 9 / -2.0 --> -4.5
# c.1.9: 4 + 3 * 5 --> 19
# c.1.10: (4 + 3) * 5 --> 35

#c.2: what will variable x be after statement ex.?
# c.2.1: x = 100 --> 100
# c.2.2: x = x + 10 --> 110
# c.2.3: x += 20 --> 130
# c.2.4: x = x - 40 --> 90
# c.2.5: x -= 50 --> 40
# c.2.6: x *= 3 --> 120
# c.2.7: x /= 5 --> 24.0
# c.2.8: x %= 3 --> 0.0

# c.3: when x has an initial value of 3, Python first evaluates (x-x) for
# initial x, which gives the value 0. then it adds that 0 value to another
# initial x of 3, which results in a new x of 0+3, or just 3 again.

# c.4.1: 1j + 2.4j --> 3.4j
# c.4.2: 4j * 4j --> (-16+0j)
# c.4.3: (1+2j) / (3+4j) --> (0.44+0.08j)
# c.4.1: (1+2j) * (1+2j) --> (-3+4j)
# c.4.2: 1+2j * 1+2j --> 1+4j
# when there are parentheses, Python uses normal distributive properties to 
# multiply 1 by 1 and 1 by 2j and so on. when there are no parentheses, Python 
# will multiply the real numbers with real numbers and imginary numbers with 
# imaginary ones.

# c.5.1: cmath.sin(-1.0+2.0j) --> (-3.165778513216168+1.9596010414216063j)
# c.5.2: cmath.log(-1.0+3.4j) --> (1.2652585805200263+1.856847768512215j)
# c.5.3: cmath.exp(-cmath.pi * 1.0j) --> (-1-1.2246467991473532e-16j)
# when using "import math," to call a function again you must use math.func()
# in calling some function func(). however, when using "from math import *" you
# can simply call the function func(). this is problematic because if you import
# cmath, this library  has functions with the same names but different  
# properties, # so you will lose the original functions. all newly imported 
# functions from cmath will replace the ones from the math library.

# 6.1: "foo" + 'bar' --> 'foobar'
# 6.2: "foo" 'bar' --> 'foobar'
# 6.3: a = 'foo' 
     # b = "bar"
     # a + b --> 'foobar'
# 6.4: a = 'foo'
     # b = "bar"
     # a b --> Traceback (most recent call last):  Python Shell, prompt 40, 
     # line 1. Syntax Error: invalid syntax: <string>, line 1, pos 3
     
# 7: 'A\nB\nC'

# 8: '-'*80 --> 
#'--------------------------------------------------------------------------------'

# 9: "first line \nsecond line \nthird line"

# for 10.1 to 10.5, use the format function
# ex) "CS{} is the best!".format(1) --> "CS1 is the best"
# ex) "Hi my name is {} and I am {}".format("Sophie", "your TA")
#   --> Hi my name is Sophie and I am your TA
# 10.1:
x=3
y=12.5
print("The rabbit is {}.".format(x))
# 10.2:
print("The rabbit is {} years old.".format(x))
# 10.3:
print("{} is average.".format(y))
# 10.4:
print("{}*{}".format(x,y))
# 10.5:
print("{}*{} is {}.".format(x,y,x*y))

# 11:
num = input("Enter a number: ")
print(num)

# 12: 
def quadratic(a,b,c,x):
 return a*x*x + b*x + c

# 13:
def GC_content(dna):
 """Takes in a string of DNA and returns proportion of G or C in the string. 
 GC_content('stringDNA') --> floatA"""
 g = dna.count('G')
 c = dna.count('C')
 ret = (g+c)/len(dna)
 return ret