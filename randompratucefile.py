class Dish:
    def __init__(self, item, rating):
        self.item = item
        self.rating = rating

    def show(self):
        print("                          DISH                     ")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("Item:", self.item, "Rating:" ,self.rating)

# Create an instance of Dish
dish1 = Dish("food", 4.5)
# Call the show method to display the details
dish1.show()

