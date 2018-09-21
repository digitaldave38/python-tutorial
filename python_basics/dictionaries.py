#dictonaries keys and vaules.


student = {
    "name": "Dave",
    "student_id": 15163,
    "feedback": None
}

#list of dictionaries


all_students = [
    {"name": "John", "student_id": 15163},
    {"name": "Mark", "student_id": 15164},
    {"name": "Paul", "student_id": 15165}
]

student.keys()
student.values()


dictionary_example = {
  "key1": "value1",
  "key2": "value2",
  "key3": "value3"
}

dictionary_tk = {
  "name": "Leandro",
  "nickname": "Tk",
  "nationality": "Brazilian"
}

print("My name is %s" %(dictionary_tk["name"])) # My name is Leandro
print("But you can call me %s" %(dictionary_tk["nickname"])) # But you can call me Tk
print("And by the way I'm %s" %(dictionary_tk["nationality"])) # And by the way I'm Brazilian

