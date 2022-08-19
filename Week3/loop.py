# WHILE LOOP 
# finger=0

# while finger!=5:
#     print("meow")
#     finger+=1  

# FOR LOOP

# for i in [0,1,2]: # list are expressed within square brackets.
#     print("meow")

# FOR LOOP USING RANGE and '_' character for variable 

# for _ in range(3): # GOOD APPROACH 
#     print("meow")

# ONE LINER 

# print("meow\n"*3,end="")

# TAKING INPUT FROM THE USER 

# while True:
#     n = int(input("Whats n? "))
#     if n > 0:
#         break

# for _ in range(n):
#     print("meow")

def main():
    n = get_num()
    meow(n)

def meow(n):
    for _ in range(n):
        print("meow")
def get_num():
    while True:
        n = int(input("What's n? "))
        if n > 0:
            return n
    
main()

