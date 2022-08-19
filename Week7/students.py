import csv

# with open("students.csv") as file:
#     for line in sorted(file):
#         names,house=line.rstrip().split(",") # better is create 2 names for the individual part
#         print(f"Name:- {names}, house:- {house}")

students = []

# with open("students.csv") as file:
#     for line in file:
#         name, home = line.rstrip().split(",")
#         student = {"name" : name,
#                    "home" : home}
#         students.append(student) # creates a list of dictionary 

with open("students.csv") as file:
    for row in csv.DictReader(file):
        students.append({"name":row["name"],"home":row["home"],"house":row["house"]}) # we do not need to create a dict calling and appending is same as we are
                                                                                      # dict reading  


# def get_name(student):
#     return student["name"]

# using a lambda function (anonymous function) instead of the get_name function


for student in sorted(students,key= lambda student: student["name"]): # this is basically a method reference we are not using parenthesis here
    print(f"{student['name']} is from {student['home']} and is in {student['house']}")


