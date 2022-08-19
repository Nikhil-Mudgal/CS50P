import re

email = input("What's your email? ").strip()    

## re.search
if re.search(r"^(\w|\.)+@(\w+\.)*\w+\.(edu|com)$",email,flags=re.IGNORECASE):
    print("Valid")
else:
    print("Invalid")


