number = 5
if number ==5:
    print("Number is 5")
else:
    print("Number is NOT 5")

# truthy vaule

text = "Python"
if text:
    print("text is defined and truthy")

number = 5 
if number:
    print("Number")

python_course = True
if python_course: 
    print("This is a python course")

aliens_found = None
if aliens_found:
    print("This will NOT execute")

#falsy 

number - 5 
if number !=5:
    print("This will not execute")

python_course = True
if not python_course:
    print("This will also not execute")

#Multiple if conditions

number = 3
python_course = True
if number == 3 and python_course:
    print("this will execute")


if number == 17 or python_course:
    print("This will also execute")

#Ternary if statements

a = 1 
b = 2

"bigger" if a > b else "smaller"
