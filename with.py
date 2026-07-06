"""
name = input("whats your name ? ")
with open ("names.txt","a") as file:
    file.write(f"{name}\n")
"""
"""
with open("names.txt","r")as file:
    lines = file.readlines()
for line in lines:
        print("hello ,",line)
"""
#### to sort data 
"""
names=[]
with open ("names.txt")as file:
    for line in file:
        names.append(line.rstrip())

for name in sorted(names, True ## it reverse from last to first):
    print(f"hello ,{name}")
"""
#another way less code

with open("names.txt")as file:
    for line in sorted(file):
        print("hello ,",line.rstrip())