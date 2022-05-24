class Train:
    def __init__(self,name,fare,seats):
        self.name=name
        self.fare=fare
        self.seats=seats
    def status(self):
        print(f"The name of the train is {self.name}.")
        print(f"Seats available in this train are {self.seats}")
    def price(self):
        print(f"The price of one ticket is {self.fare}.")
    def bookticket(self):
        if(self.seats>0):
            print(f"Your ticket number is {self.seats}")
            self.seats=self.seats-1
        else:
            print("Sorry.")

a=Train("Meghan",90,1)
a.status()
a.price()
a.bookticket()
a.bookticket()
a.bookticket()
a.bookticket()


