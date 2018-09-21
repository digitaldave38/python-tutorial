
my_integers = [1, 2, 3, 4, 5]

my_integers = [5, 7, 1, 3, 4]
print(my_integers[0]) # 5
print(my_integers[1]) # 7
print(my_integers[4]) # 4



relatives_names = [
  "Toshiaki",
  "Juliana",
  "Yuji",
  "Bruno",
  "Kaio"
]

print(relatives_names[4]) # Kaio

#append
bookshelf = []
bookshelf.append("The Effective Engineer")
bookshelf.append("The 4 Hour Work Week")
print(bookshelf[0]) # The Effective Engineer
print(bookshelf[1]) # The 4 Hour Work Week



#lists


student_names = ["Mark","dave","Jessica","Isabell","Elaine"]

student_names[0]
student_names[-1]

student_names[0] = "James"

#list functions

student_names.append("Homer") # added to end of list 
"Mark" in student_names == True

len(student_names) # how many elements in list 
del student_names[2] # remove from list 

#list slicing 

student_names[1:] # skips first elepment from list 

