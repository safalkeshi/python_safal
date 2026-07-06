""""
with open("student.csv") as file:
    for line in file:
       name,house = line.rstrip().split(",")
       print(f"{name} lives in {house} ")

"""
students =[]
with open ("student.csv") as file:
    for line in file:
        name,house = line.rstrip().split(",")
        #using dictionary
        student ={"name": name,
                  "house":house}
        
        students.append(student)
""" normal 
def get_name(student):
    return student ["name"]
"""


#using lamdafunction 

for student in sorted (students, key =lambda student: student["name"] , reverse=True):
    print(f"{student['name']} is in {student['house']}")


""" without using dictionary
for student in sorted(students):
    print(student)
     students.append(f"{name} is in {house}")
"""

