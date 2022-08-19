def main():
    x = int(input("Enter x: "))
    if is_even(x):
        print("even")
    else:
        print("Odd")

def is_even(num):
    return num % 2 == 0 # fucking elegent :) 

main()