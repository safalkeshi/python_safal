def main():
    number = float(input("enter your total bill: "))
    tip = number * 0.15
    total = number +tip
 
    return tip, total
    
tip,total = main()

print(f"Total amount: ${tip:.2f}")
print(f"Total bill : ${total: .2f}")
