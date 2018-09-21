"""In Python, we can iterate in different forms. I’ll talk about two: while and for.

While Looping: while the statement is True, the code inside the block will be executed. So, this code will print the number from 1 to 10."""

num = 1

while num <= 10:
    print(num)
    num += 1


"""The while loop needs a “loop condition.” If it stays True, it continues iterating. In this example, when num is 11 the loop condition equals False
"""

loop_condition = True

while loop_condition:
    print("Loop Condition keeps: %s" %(loop_condition))
    loop_condition = False

"""The loop condition is True so it keeps iterating — until we set it to False.
For Looping: you apply the variable “num” to the block, and the “for” statement will iterate it for you. This code will print the same as while code: from 1 to 10.
"""

for i in range(1, 11):
  print(i)

"""The range starts with 1 and goes until the 11th element (10 is the 10th element)."""



#  iterable objects

student_names = ["Mark","dave","Jessica","Isabell","Elaine"]

for name in student_names:
    print("Student name is {0}".format(name))

x = 0 
for index in range(20):
    x +=20
    print("The vaule of X is {0}".format(x))

