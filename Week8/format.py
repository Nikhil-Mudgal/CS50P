import re 

# data to format is name of the user
 
name = input("What's your name? ").strip() # cleans leading and trailing white spaces
# if "," in name:
#     last,first=name.split(", ?") # this does not support regular expression 
#     name =  f"{first} {last}"
# print(f"hello, {name}")

if matches := re.search(r"^(\w+), *(\w+)$", name): # precise answer
    name = matches.group(2) + " " + matches.group(1)
print(f"hello, {name}")
