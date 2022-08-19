class Student():

    def __init__(self,name,house): # python automatically calls this 
        self.name = name 
        self.house = house


    def __str__(self): 
        return f"{self.name} is from {self.house}"


    @classmethod
    def get(cls):
        name = input("Name: ")
        house = input("House: ")
        return cls(name,house) # creates an object of the current class 


def main():
    student = Student.get() # unpacks sequence of values 
    print(student)


if __name__ == "__main__":
    main()