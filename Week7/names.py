name = input("What is your name? ")

# for _ in range(3):
#     names.append(input("What's your name? ")) # append is to add inside the list     

# for name in sorted(names):
#     print(f"hello, {name}")

# saving the names in a file

# old way 
# file = open("names.txt","a")
# file.write(f"{name}\n")
# file.close()
    
# better way 

with open("names.txt","a") as file:
    file.write(f"{name}\n")
