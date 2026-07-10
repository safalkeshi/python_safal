import re

email = input("email ? ").strip()

if re.search(r"^\w+@\w+\.com$",email,re.IGNORECASE ):
    print('valid')
else:
    print("invalid")


