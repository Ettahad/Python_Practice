class calculator:
    def __init__(self,number):
        self.number=number
    def square(self):
        print(f"The squar of {self.number} is {self.number ** 23}.")
    @staticmethod
    def greet():
        print("Hello Sir.")



a=calculator(7)
a.square()

a.greet()
