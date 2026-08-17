def numberchecker(number):
    if number % 2 ==0 :
        print(f"This {number} is even")
    else :
        print(f"this {number} is odd.")

def main():
    number = int(input("Enter your number"))
    numberchecker(number)


main()