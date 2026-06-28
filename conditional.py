x_str,y_str = input ('enter numbers ').split()
x, y = float(x_str) , float(y_str)
if x<y or x>y:
    print("x is not equal to y")
else:
    print("x is equal to y")