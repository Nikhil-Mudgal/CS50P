def main():
    n = int(input("Whats n? "))
    for s in sheep(n):
        print(s)        


def sheep(n):
    for i in range(n):
        yield "sheep " * i  # generates little amount of dat at a time. 

if __name__ == "__main__":
    main()