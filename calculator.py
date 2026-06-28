# x =int(input ("whats x ?"))
# y= int(input("whats y ?"))
# print(x+y)

def main():
    x,y =input("enter 2 numbers").split()
    sum(x,y)
    diff(x,y)
    multiply(x,y)
 

def sum(x,y):
    sum = int(x)+int (y)
    print(f"the sum is {sum}")

def diff(x,y):
    diff=int(x)-int(y)
    print(f"the diff is {diff}")
 

def multiply(x,y):
    mul =int(x)* int(y)
    print(f"this is {mul}")

main()
    
# z = float(input("z"))
# a = float(input("a"))
# sum =(int(round(z +a)))
# print(f"{sum:.2f}")
