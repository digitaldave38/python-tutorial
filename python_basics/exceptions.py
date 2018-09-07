# execptions are events that stop program from executing

student = {
    "name": "Dave",
    "student_id": 15163,
    "feedback": None
}

try:
    name = student["name"]
except KeyError:
    print ("Error finding name")

print("This code executes!")
