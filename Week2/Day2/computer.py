class Computer():

    def __init__(self):
        self.name = "Apple Computer" # public
        self.__max_price = 900 # private attribute

    def sell(self):            # public method
        print(f"Selling Price: {self.__max_price}")

    def __sell(self):          # private method
      print('This is private method')

    def set_max_price(self, price):
        self.__max_price = price

c = Computer()
# print(c.set_max_price(5000))
