name = ["John", "Bob", "Mary", "Sam"]
print(name) # Output: ['John', 'Bob', 'Mary', 'Sam']
print(name[0]) # Output: John | 0 is the first or beginning of list
print(name[-1]) # Output: Sam | -1 is the last or end of list
print(name[-2]) # Output: Mary | -2 is the 2nd last or second from end of list

# Changing Values
name[0] = "Jon" # Since John is 0, this will change "John" to "Jon"
print(name) # Output: ['Jon', 'Bob', 'Mary', 'Sam']

# Range
print(name[0:3]) # Output: ['Jon', 'Bob', 'Mary'] | 0 is start or "start index" and 3 is "end index", but the code excludes the end index

# List Methods
# append | Adds value at the end of list
numbers = [1, 2, 3, 4, 5]
numbers.append(6) # Output: [1, 2, 3, 4, 5, 6]
print(numbers)

# insert | Insert value into list
numbers = [1, 2, 3, 4, 5]
numbers.insert(0, -1) # Output: [-1, 1, 2, 3, 4, 5]
print(numbers)

# remove | Removes value from list
numbers = [1, 2, 3, 4, 5]
numbers.remove(3) # Output: [1, 2, 4, 5]
print(numbers)

# clears | Clears all values from list
numbers = [1, 2, 3, 4, 5]
numbers.clear() # Output: []
print(numbers)

# in operator | Checks to see if values are in the list (Boolean)
numbers = [1, 2, 3, 4, 5]
print(1 in numbers) # Output: True
print(0 in numbers) # Output: False

#len | Check how many values are in a list
numbers = [1, 2, 3, 4, 5]
print(len(numbers)) # Output: 5