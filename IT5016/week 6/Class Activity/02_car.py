class Car:
    def __init__(self,color,model):
        self.color = color
        self.model = model

    def drive(self):
        print(f"The {self.color} {self.model} is driving.")

    def stop(self):
        print(f"The {self.color} {self.model} has stopped.")


car1 = Car("Red","Toyota")
car2 = Car("Blue", "Honda")

car1.drive()
car1.stop()