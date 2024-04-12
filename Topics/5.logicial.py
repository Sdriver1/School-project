# Learning Logicial Operators
price = 10

# And operator | Both statements need to match to be True
print(price > 5 and price < 20) # Output: True
print(price > 15 and price < 20) # Output: False

# or operator | At least 1 statement needs to match to be True
print(price > 15 or price < 20) # Output: True

# not operator | Inverses true and False boolean 
print(not price > 15) # Output: True
print(not price > 5) # Output: False