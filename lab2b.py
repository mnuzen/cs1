import random

# random.choices() --> v helpful
# .choices(list,k=# of thigns u want from a list)

# D.1:
def make_random_code():
 """Returns a four character string composed of random letters from the 
 following selection: R,G,B,Y,O,W"""
 lst = ['R','G','B','Y','O','W']
 lstRan = random.choices(lst,k=4)
 string=""
 for l in lstRan:
  string+=l
 return string

# D.2:
def count_exact_matches(str1,str2):
 """Takes in two strings and returns a value that represents the number of 
 elements in str1 that are in the same location as in str2."""
 match=0
 for i in range(0,4):
  if str1[i]==str2[i]:
   match+=1
 return match

# D.3:
def count_letter_matches(str1,str2):
 """Takes in two strings and returns the number of elements in str1 that are 
 also found within str2."""
 count=0
 lst1 = list(str1)
 lst2 = list(str2)
 #  make it only check once uniquely
 for l in lst1:
  if l in lst2:
   count+=1
   lst2.remove(l)
 return count  

# D.4:
def compare_codes(code,guess):
 """Takes in two strings and returns a string that represents the number of 
 correct guesses and locations, correct guesses, and misses."""
 bpeg=count_exact_matches(code,guess)
 wpeg=count_letter_matches(code,guess)-bpeg
 bnpeg=4-(bpeg+wpeg)
 b=("b"*bpeg)+("w"*wpeg)+("-"*bnpeg)
 return b
 
 
# D.5:
def run_game():
 """Returns """
 print("New game.")
 scode = make_random_code
 count=0
 rstr=""
 while(rstr!="bbbb"):
  guess = input("Enter your guess: ")
  rstr = compare_code(scode,guess)
  print("Result: " + rstr)
  count+=1
  if rstr=="bbbb":
   break
 print("Congratulations! You cracked the code in " + count + " moves!")
  
