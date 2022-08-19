names = [] # createed a list just to gather the data 

with open("names.txt","r") as file:
    for line in file: # using the sort here is also acceptable 
        names.append(line.rstrip()) # appending the names to the new names list 

for name in sorted(names, reverse=True): # sorting them
    print(f"hello, {name}") 

 





