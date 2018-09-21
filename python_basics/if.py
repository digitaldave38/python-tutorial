"""If” uses an expression to evaluate whether a statement is True or False. If it is True, it executes what is inside the “if” statement. For example:
"""

if True:
  print("Hello Python If")

if 2 > 1:
  print("2 is greater than 1")

"""2 is greater than 1, so the “print” code is executed.

The “else” statement will be executed if the “if” expression is false."""

if 1 > 2:
  print("1 is greater than 2")
else:
  print("1 is not greater than 2")

"""1 is not greater than 2, so the code inside the “else” statement will be executed."""

"""you can use elif"""

if 1 > 2:
  print("1 is greater than 2")
elif 2 > 1:
  print("1 is not greater than 2")
else:
  print("1 is equal to 2")

  




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
