"""
names =[]
for _ in range(3):  #could write for i in range (3): this runs 3 times just a python cryptic way
    names.append(input("whats your name ? "))

for name in sorted(names):
    print(f"hello, {name}")
"""
name = input("what's your name ? ")

file = open("names.txt","a")
file.write(f"{name}\n")
file.close()