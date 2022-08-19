import random

class Hat:
    houses = ["Gryffindor","Hufflepuff","Slytherin","Ravenclaw"] # variable inside of the class , class varaible
    # the above object houses is associated with the class and then is called a class variables 
    @classmethod   
    def sort(cls,name):
        print(name,"is in", random.choice(cls.houses))


def main():
    Hat.sort("Harry")

def get_house():
    pass


if __name__ == "__main__":
    main()