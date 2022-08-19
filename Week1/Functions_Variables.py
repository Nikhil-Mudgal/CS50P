# print("hello, world!" # throws a message that the ( was never closed gives a syntax error

# print("Hello,World!") # here print is basically a function. 


# # Asking user for their name 
# usr_name = input("What's your name?: ").strip().title() # input naturally returns a str object and formats according to methods 

# # Splits the user's name into first name and last name
# first, last = usr_name.split(" ")

# # Say hello to the user
# print("Hello, ",first,sep="")

name = input("What's your name: ")
def main():
    hello() # takes the default value    
    hello(name) # takes the value entered by the user  

def hello(_name="world"):
    """Hello function pretty useless ngl

    Args:
        _name (str): Name to say hi to
    """
    print("Hi,",_name)

