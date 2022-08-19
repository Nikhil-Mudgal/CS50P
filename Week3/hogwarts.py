## EARLY PROGRAM 

# students = ["Hermione","Harry","Ron","Draco"]

# houses  = ["Gryffindor","Gryffindor","Gryffindor","Slytherin"]

# student_houses = {
#     "Hermoine" : "Gryffindor",
#     "Ron" : "Gryffindor",
#     "Harry" : "Gryffindor",
#     "Draco" : "Slytherin"
# }

# print(student_houses["Hermoine"],
#       student_houses["Harry"],
#       student_houses["Ron"],
#       student_houses["Draco"])

# for student in student_houses:
#     print(student + " |",student_houses[student])


## CREATING A DATABASE USING DICT

students = [
    {
        "name":"Hermoine",
        "house":"Gryffindor",
        "patronus":"otter"
    },
    {
        "name":"Harry",
        "house":"Gryffindor",
        "patronus":"Stag"
    },
    {
        "name":"Ron",
        "house":"Gryffindor",
        "patronus":"Terrier"
    },
    {
        "name":"Draco",
        "house":"Slytherin",
        "patronus":None
    }
]

for student in students:
    print(student["name"] ,
          student["house"] ,
          student["patronus"],sep=" | ")

