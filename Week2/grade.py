score = int(input("Score: "))


if score >= 90: 
    print("A")
elif score >= 80: # elif unables us to do this we cannot use "if" here
    print("B")
elif score >= 70:
    print("C")
elif score >= 60:
    print("D")
else:
    print("F")