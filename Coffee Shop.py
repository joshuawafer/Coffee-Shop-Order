class CoffeeShopOrder:
    """Represents an order from a coffee shop with multiple attributes"""

    #List of options to help with error handling so unavailable options can not be selected
    drinks_menu = {"latte", "cappuccino", "americano","espresso","mocha"}
    size_options = {1,2,3}
    milk_types = {0,1,4}
    milk_options = {"oat","whole", "soy", "almond"}
    temp_options = {0,1}


    def __init__(self, drink_type: str, size: int, milk_option: str,  order_id: str,milk_type: int, customer_name: str, extra_shots: int = 0, temperature: int = 0, ):
        if drink_type.lower() not in self.drinks_menu:
             raise ValueError(F"Sorry, that is not on our menu. Please look at our menu and decide what you would like {CoffeeShopOrder.drinks_menu}")
        if size  not in self.size_options:
            raise ValueError(F"Sorry that size is not available, please select from our size options {CoffeeShopOrder.size_options}")
        if milk_type not in self.milk_types:
            raise ValueError(F"Sorry that milk type is not available, please select from our milk types {CoffeeShopOrder.milk_types}")
        if milk_option.lower() not in self.milk_options:
            raise ValueError(F"Sorry we do not have that milk option, please select from our available milk options {CoffeeShopOrder.milk_options}")
        if temperature not in self.temp_options:                raise ValueError(F"Sorry please select one of our two temp options {CoffeeShopOrder.temp_options}")
        #Error Handling

        self.__drink_type = drink_type
        self.__size = size
        self.__milk_type = milk_type
        self.__milk_option = milk_option
        self.__order_id = order_id
        self.__customer_name = customer_name
        self._extra_shots = extra_shots
        self._temperature = temperature
    def get_drink_type(self):
        return self.__drink_type
    def get_size(self):
        return self.__size
    def get_milk_type(self):
        return self.__milk_type
    def get_milk_option(self):
        return self.__milk_option
    def get_order_ID(self):
        return self.__order_id

    #Using getters for proper encapsulation



    def drink_type_price(self):
        """Sets price of each drink by matching name in order and assigning value to price"""
        drink = self.__drink_type.lower()
        if drink == "latte":
          return 2.00
        elif drink == "cappuccino":
            return 2.20
        elif drink == "americano":
            return 1.80
        elif drink == "espresso":
            return 1.50
        elif drink == "mocha":
            return 2.50
        else:
            return 0




    def overall_price(self):
        """Equation for pricing"""
        base_price = self.drink_type_price()
        return (base_price * self.__size) + (self._extra_shots * 0.5)








    def add_shot(self,):
        """Adds a shot when called"""
        self._extra_shots = self._extra_shots + 1

    def temp_ID(self):

        """Changes temperature from intergers to strings to show up better in summary"""
        match self._temperature:
            case 0:
                return("Hot")
            case 1:
                return("Iced")
    def make_iced(self):
        """Change the order from hot to iced"""
        if self._temperature < 1:
            self._temperature +=1

    def size_ID(self):
        """Matches integer to name for size for clearer reading in summary"""
        match self.__size:
            case 1:
                return "Small"
            case 2:
                return "Medium"
            case 3:
                return "Large"






    def change_size(self,new_size:int):
        """Changes size when called, contains error handling if size asked for is unavailable"""
        if new_size not in self.size_options:
            raise ValueError(F"Sorry that size is not available, please select from our size options {CoffeeShopOrder.size_options}")
        self.__size = new_size

    def milk_ID(self):
        """Matches integer to name for milk type for clearer reading in summary"""
        match self.__milk_type:
            case 1:
                return( "Semi-Skimmed")
            case 4:
                return(  "Full Fat")
            case 0:
                return( "Skinny")



    def summary(self):
        """Summary of order"""
        total = self.overall_price()
        return ( f"Order # {self.get_order_ID()}, for {self.__customer_name}, {self.size_ID()} {self.temp_ID()} {self.get_drink_type()} with {self.milk_ID()} milk containing {self._extra_shots} extra shots. Your total for today is {total}")



Order1 = CoffeeShopOrder("LATTE", 1, "Whole","12345",0,"Jimmy")

print(Order1.summary())

Order1.add_shot()
Order1.add_shot()

CoffeeShopOrder.make_iced(Order1)
CoffeeShopOrder.change_size(Order1,3)


print(CoffeeShopOrder.summary(Order1))
order = CoffeeShopOrder("Latte", 2,"Oat", "101", 1, "Sam")
order.add_shot()
print(CoffeeShopOrder.summary(order))
order.add_shot()
order.make_iced()
order.change_size(3)
print(order.summary())
# 1. A small Americano with no extra shots
order1 = CoffeeShopOrder("Americano",1, "Whole","201",4,"Alex")
print("Price of order 1:", order1.overall_price())

#A medium Latte with one extra shot
order2 = CoffeeShopOrder("Latte",2,"Oat","202",1,"Jordan"
)
order2.add_shot()
print("Price of order 2:", order2.overall_price())
#A large Mocha with two extra shots
order3 = CoffeeShopOrder("Mocha",3,"Soy","203",4,"Pike")
order3.add_shot()
order3.add_shot()
print("Price of order 3:", order3.overall_price())
#testing using examples