class Wizard:
    def __init__(self,name):
        if not name:
            raise ValueError("Invalid Name")
        self.name = name
    
    def __str__(self):
        return f"{self.name}"

class Student(Wizard):
    def __init__(self,name,house):
        super().__init__(name)# ref to the super class of the child class which in our case is Wizard
        self.house = house 
    


class Professor(Wizard):
    def __init__(self,name,subject):
        super().__init__(name)
        self.subject = subject




def main():
    print(Student("Harry","Gryffindor"))
    print(Professor("Severus","Defence Against the Dark Arts"))
    print(Wizard("Albus"))

if __name__ == "__main__":
    main()