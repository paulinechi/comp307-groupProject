class Dish:

    def __init__(self, name, picture_location, ingredients, price):
        self.name = name
        self.picture_location = picture_location
        self.ingredients = ingredients
        self.price = price

    # for name
    def change_name(self, new_name):
        self.name = new_name

    def get_name(self):
        return self.name

    # for picture
    def change_picture(self, new_picture):
        self.picture_location = new_picture

    def get_picture(self):
        return self.picture_location

    # for price
    def change_price(self, new_price):
        self.price = new_price

    def get_price(self):
        return self.price

    # for ingredients

