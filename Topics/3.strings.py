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
