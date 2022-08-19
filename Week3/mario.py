def main():
    # print_col(3) # abstraction to tell us to print some chunk of the GUI
    # print_rows(4)
    grid(3)

def print_col(height):
    print("#\n"*height,end="")


def print_rows(width):
    print("? "*width)


def grid(size):
    # for each row in square
    for _ in range(size):
        # for each brick in row print #
        print("#|"*size)
        
main()







