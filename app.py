# I am just testing the waters here of python so any code below is just practice of concepts which I will be going over

# Learning how to print to console
print("Hello World") 

# Learning how to set values
age = 16
price = 19.95
first_name = "Driver"
is_online = True

# Learning about input(), int(), and str()
name = input("What is your name? ")
print("Hello " + name)

birth_year = input("What is your birth year? ")
age = 2024 - int(birth_year)
print(age)

# Learning strings
course = 'Python is fun'
        # 012345
print(course.upper()) # Output: PYTHON IS FUN
print(course.lower()) # Ouput: python is fun
print(course.find('h')) # Output: 3
print(course.find('H')) # Output: -1 | Since there is no uppercase H
print(course.replace('fun', 'cool')) # Output: Python is cool | Replaces "fun" with "cool"
print('Python' in course) # Output: True | Because "Python" is in our variable 'course', it is true
print('Hello' in course) # Output: False | Because "Hello" is not in our variable 'course', it is false