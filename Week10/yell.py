def main():
    yell("This","is","CS50","fuck","you","MIT!!")


def yell(*words):
    upper_case = [word.upper() for word in words]
    print(*upper_case)


if __name__ == "__main__":
    main()