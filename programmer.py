class Programmer:
    company = "Microsoft"

    def __init__(self, name, product):
        self.name = name
        self.product = product

    def gitinfo(self):
        print(
            f"The name of the programmet is {self.name}. And he is working on {self.product}.")


harry = Programmer("Hary", "Dif")
harry.gitinfo()
