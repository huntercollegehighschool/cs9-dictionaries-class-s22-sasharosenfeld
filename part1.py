'''
Write a function that takes in three numbers a, b, and c, and creates a dictionary where all the keys are numbers between a and b, and the values are the square of the keys. Using this dictionary, output whether c is a SQUARE of a value between a and b, inclusive.

For this, you should use the separate function squares_dict to ouput the dictionary, so you can use the squares_dict function in part 3.

E.g.: if a = 3, b = 5, c = 16, 3*3 = 9 <= 16 <= 5*5 = 25, so output True

if a = 6, b = 10, c = 101, 6*6 = 36 <= 101 </= 10*10 = 100, so output False
'''

def squares_dict(a, b):
  sd = {}
  for i in range(a, b+1):
    sd[i] = i**2
  return sd[i]

def squares(a, b, c):
  sq_dict = squares_dict(a, b)
  if c in sq_dict.values():
    return True
  else: 
    return False



#empty_dict = {} --> empty eictionary
#fruit_colors["apple"] = "red" --> add key-value pairs to dictionary
#fruit_colors["banana"] = "yellow"
#pint(fruit_colors["apple"]) --> prints "red"