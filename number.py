while True:
  try:
    x = int(input("what's x "))
    break
  except ValueError:
    print("x isnt an integer")
    pass
print(f"x is {x}")