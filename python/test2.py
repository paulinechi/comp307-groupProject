import json
from Seller import Seller
from Dish import Dish

def main():
    # jsonData = '{"name": "Frank", "age": 39}'
    # jsonToPython = json.loads(jsonData)
    # print jsonToPython['name']
    # pythonDictionary = {'name':'Bob', 'age':44, 'isEmployed':True}
    # dictionaryToJson = json.dumps(pythonDictionary)
    # print(dictionaryToJson)
    jack = Seller("Jack", "jack@resto.com")
    jack.set_location("Hawaii")
    jack.set_restaurant_name("Pizzeria Volcano")
    print(jack.get_email())
    seller_name = getattr(jack, 'name')
    print(seller_name)
    setattr(jack, '_location', "Jamaica")
    print(jack.get_location())


def testing_method():
    ss = Seller("jack24*", "Jack Hoske", "jack_pizza@resto.com")

    ss.set_name("Paula Uburyi")
    print(ss.get_name())

    ss.set_username("paula_uburyi_1860")
    print(ss.get_username())

    ss.set_email("paula@uburyi_soups.com")
    print(ss.get_email())

    ss.set_location("Jersey")
    print(ss.get_location())

    first_dish = Dish("Vegetable soup", "./veg_soup.jpg", ["Carrots", "Tomatoes", "Onions"], 4.15)
    ss.add_dish(first_dish)
    print(ss.get_menu()[0].get_name())

testing_method()
