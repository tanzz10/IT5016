class Person():
    #constructor
    def __init__(self,name,gender):
        self.name = name
        self.age = 10
        self.gender = gender

    def speaks(self):
        print(f"What does {self.name} say?: ")


#object
person1 = Person("Rashid", "male")
person2 = Person("Kanchan", "female")

person1.speaks()



