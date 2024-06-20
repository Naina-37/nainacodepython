class Restaurant:
    def __init__(self, name, location, cuisine):
        self.name = name
        self.location = location
        self.cuisine = cuisine

    def show(self):
        print("Restaurant :")
        print("Name:", self.name)
        print("Location:", self.location)
        print("Cuisine:", self.cuisine)
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

class Menu:
    def __init__(self, restaurant_name, items, prices):
        self.restaurant_name = restaurant_name
        self.items = items
        self.prices = prices

    def show(self):
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("Menu for", self.restaurant_name)
        for item, price in zip(self.items, self.prices):
            print(item, "Rs.",price)
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

class Dish:
    def __init__(self, name, ingredients, price):
        self.name = name
        self.ingredients = ingredients
        self.price = price

    def show(self):
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("Dish :")
        print("Name:", self.name)
        print("Ingredients:", ", ".join(self.ingredients))
        print("Price: rs.", self.price)
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

# Creating a Restaurant object
restaurant1 = Restaurant("Foodie", "INDIA", "Italian")
restaurant1.show()

# Creating Dish objects
dish1 = Dish("Pizza", ["icecream", "sweets", "Cheese"], 300)
dish2 = Dish("Pasta", ["Pasta", "Sauce", "Noodles"], 200)

# Displaying Dish details
dish1.show()
dish2.show()

# Creating a Menu object with the dishes
menu1 = Menu("Foodie", ["Pizza", "Pasta"], [300, 200])
menu1.show()