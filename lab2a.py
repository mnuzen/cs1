# write docstrings for every function and describe what the function does
# what arguments rep, what return value reps

import random

# B.1:
def complement(dnaString):
 """Takes in a string of DNA and returns the respective complement in the form
 of a string. complement('dnaString') --> dnaCString"""
 ret = ""
 for c in dnaString:
  if c == "A":
   ret+="T"
  elif c == "T":
   ret+="A"
  elif c == "C":
   ret+= "G"
  elif c == "G":
   ret+= "C"
 return ret

# B.2:
def list_complement(dnaList):
 """Takes in a list of DNA characters and replaces that same list with 
 a list of complementary DNA characters. list_complement(dnaList) --> NA
 but dnaList becomes dnaCList (same variable name though)"""
 dnaLen = len(dnaList)
 i = 0
 while i < dnaLen: 
  if dnaList[i] == "A":
   dnaList[i] = "T"
  elif dnaList[i] == "T":
   dnaList[i] = "A"
  elif dnaList[i] == "C":
   dnaList[i] = "G"
  elif dnaList[i] == "G":
   dnaList[i] = "C"
  i+=1
  
# B.3:
def product(numList):
 """Takes in a list of numbers numList and returns a number that is the 
 product of all numbers in numList. product(numList) --> product"""
 ret = 1
 if len(numList) < 0:
  return ret
 else:
  for n in numList:
   ret = ret*n
 return ret

# B.4:
def factorial(m):
 """Takes in a non-negative integer m and returns a single integer that 
 represents the factorial of m. factorial(m) --> m!"""
 return product(list(range(1,m+1)))

# B.5:
def dice(m,n):
 """"Takes in an m-number sided dice and n number of dices. Returns the sum of 
 a random number generated from each dice, where the range goes from 1 to m.
 dice(m,n) --> i"""
 sum=0
 diceNum = list(range(1,n+1))
 for d in diceNum:
  sum+=random.choice(list(range(1,m+1)))
 return sum

# B.6:
def remove_all(numList, num):
 """Takes in a list of numbers and one number num. Removes all instances of num
 from the list without returning anything. remove_all(numList, num) --> NA
 but changes numList by removing all instances of num."""
 while(numList.count(num) > 0):
  numList.remove(num)
 
# B.7.1:
def remove_all2(numList, num):
 """Takes in a list of numbers and one number num. Removes all instances of num
 from the list without returning anything. remove_all(numList, num) --> NA
 but changes numList by removing all instances of num."""
 for n in list(range(0,numList.count(num))):
  numList.remove(num)

# B.7.2:
def remove_all3(numList, num):
 """Takes in a list of numbers and one number num. Removes all instances of num
 from the list without returning anything. remove_all(numList, num) --> NA
 but changes numList by removing all instances of num."""
 while(num in numList):
  numList.remove(num)
  
# B.8:
def any_in(list1,list2):
 """Takes in two lists and tests to see if there are any elements in One that
 are also in Two. any_in(list1,list2) --> boolean"""
 boo = False
 for n in list1:
  if n in list2:
   boo = True
 return boo

# C.1:
# a - an if statement requires a boolean expression, and the = sign denotes
# assignment, not checking whether or not two expressions are equivalent. To fix
# the statement, we change = to == to make a boolean expression.

# b - the argument that takes in a string should not have quotation marks around
# the variable name s representing the string. instead, the function should
# say: def add_suffix(s) so that the function isn't hard-coded to take in the 
# string 's' each time.

# c - the return statement should not have s in quotation marks; leaving s in 
# quotation means that "s-Caltech" will be printed instead. to fix this, we 
# should write "return s + '-Caltech'" instead.

# d - strings cannot be added to lists with concatenation. to add elements to a 
# list, we must use the append function: lst.append('bam')

# e - lst.reverse() does not have a return statement. thus simplying stating
# lst.reverse() doesn't assign anything to lst2. therefore, lst2 is currently
# instead we can just eliminate the extra variable and say: 
# lst.reverse()
# return lst.append(0)

# f - having list as the variable name in the parameter is not allowed. list is
# already a named used in the Python language and therefore is automatically 
# considered as the list object and not the name of a variable. an acceptable
# way to fix this would be to change list and str to something like lst and 
# string instead, so they aren't the same names as the object names in Python.

# C.2: the fact that a is assigned to 30 does not change the fact that when the 
# line "c = b + a" was run, variable a at the time held the value of 10. since 
# 10 + 20 is 30, c was then assigned 30. changing the value of a after the fact
# does not affect c.

# C.3: printing a result simply has the string appear on the screen, but 
# returning a result allows Python to take that result and use it in another way
# like putting it into another variable for future use, or using it directly
# in an equation. the second function doesn't produce a tangible result
# that the line with n could use.

# C.4: using input requires input from the console, i.e. you have to type in an
# input value, instead of just passing it through a function's parameters. 
# entering a value as an argument allows you to bypass waiting for an external
# input required with the second function.

# C.5: s[0].upper() returns only the uppercase version of s[0], which is only
# referring to the first character of the string s. IMMUTABLE????????????/

# C.6: you're not allowed to modify elements in a list while looping through 
# them. changing the value of an element in the list does not modify the actual 
# list. ?????????????????????????????????????????????????

