"""
i =3
while i!=0:
    print ("meow")
    i = i-1
"""

""""
for x in [0,1,2]:
    print("woof")
"""

"""
for _ in range(3):
    print("hello")

"""

#print("meow\n"*3, end="")

def main():
    number =get_number()
    meow(number)

def get_number():
    while True:
        n = int(input("whats n?"))
        if n>0:
            break
        return n 
    """"
    """
while True:
    n = int(input("whats n"))
    if n >0 :
        break
    
"""


"""
def meow(n):
  for _ in range(n):
    print("meow")

main()