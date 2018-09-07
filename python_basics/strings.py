# unicode on python 3 and asci is python 2

'Hello World' == "Hello World" 

"hello".capitalize()
"hello".replace("e","a")
"hello".isalpha()
"123".isdigit() # usefull when converting 
"some,csv,vaules".split(",") # output ["some", "csv", "vaules"]


name = "Dave"
machine = "HAL"

"Hello {0}. I am {1}".format(name,machine) # 0 is postion in format function is name and {1} is machine

#string interpolation pthon 3.6

f"Nice to meet you {name}. I am {machine}" # f=format / r=raw / u=unicode 