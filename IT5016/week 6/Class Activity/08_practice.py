# class Vehicle:
#     def __init__(self) -> None:
#         pass
#     def starting(self):
#         print(f"{self} started.")
#     def stopping(self):
#         print(f"{self} stopped.")

# class Car(Vehicle):
#     def Honk(self):
#         print(f"{self}! {self}!")



        
class Vehicle:
    def __init__(self) -> None:
        pass
    def start(self):
        print("Vehicle started.")
    def stop(self):
        print("Vehicle stopped.")

class Car(Vehicle):
    def honk(self):
        print("Honk! Honk!")

my_car = Car()
my_car.start()
my_car.honk()
my_car.stop()
