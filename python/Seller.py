class Seller:
    __location = ""
    __restaurant_name = ""
    __menu = []
    __subscribers = []

    def __init__(self, username, name, email):
        self.username = username
        self.name = name
        self.email = email

    # for name
    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    # for username
    def set_username(self, username):
        self.username = username

    def get_username(self):
        return self.username

    # for email
    def set_email(self, email):
        self.email = email

    def get_email(self):
        return self.email

    # for location
    def set_location(self, location):
        self.__location = location

    def get_location(self):
        return self.__location

    # for restaurant name
    def set_restaurant_name(self, resto_name):
        self.__restaurant_name = resto_name

    def get_restaurant_name(self):
        return self.__restaurant_name

    # for menu
    def add_dish(self, dish):
        self.__menu.append(dish)

    def remove_dish(self, dish):
        self.__menu.remove(dish)

    def get_dish(self, dish_name):
        return self.__menu[dish_name]

    def get_menu(self):
        return self.__menu
