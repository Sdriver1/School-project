numbers = range(5)
print(numbers) # Output: range(0, 5)

for number in numbers:
    print(number) # Output: 0-4
    
numbers = range(5, 10) # 5 is start value and 10 is end value
for number in numbers:
    print(number) # Output: 5-9
    
numbers = range(5, 10, 2) # 5 is start value, 10 is end value, 2 is steps (so instead going up by 1, now 2)
for number in numbers:
    print(number) # Output: 5,7,9