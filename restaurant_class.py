class Restaurant:
    def __init__(self, restaurant_name, restaurant_type):
        self.restaurant_name = restaurant_name
        self.restaurant_type = restaurant_type

    def describe_restaurant(self):
        print("The name of the restaurant is " + self.restaurant_name + ".")
        print("It serves " + self.restaurant_type + " food.\n")

    def open_restaurant(self):
        print(self.restaurant_name + " is now open for business!")
