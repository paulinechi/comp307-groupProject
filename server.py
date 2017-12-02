from flask import Flask, jsonify, request
from tinydb import TinyDB, Query
from pprint import pprint
import json

db = TinyDB('db.json')
users = db.table('users') #this is users table
restaurants = db.table('restaurants')
dishes = db.table('dishes')

app = Flask(__name__)

'''
DB functions

'''
# users functionality
def addUser(uname, pwd, email):
    users.insert({'username' : uname, 'password' : pwd, "email" : email})

def signIn(uname, pwd):
    User_query = Query()
    found_user = users.search(User_query.username == uname)[0]
    if found_user['password'] == pwd:
        print("Correct login!")
        return True
    else:
        print("Incorrect login!")
        return False

def returnAllUsers():
    return users.all()

# dishes functionality
def addDish(dish_name, dish_price, dish_pic, dish_ingredients):
    dishID = dishes.insert({'dish_name': dish_name, 'dish_price': dish_price, 'dish_pic':dish_pic, 'dish_ingredients': dish_ingredients})
    return dishID

def deleteDish(d_name):
    Dish_query = Query()
    dishes.remove(Dish_query.dish_name == d_name)

def editDish(d_name, d_price, d_ingredients):
    Dish_query = Query()
    dishes.update({'dish_price': d_price, 'dish_ingredients': d_ingredients}, Dish_query.dish_name == d_name)

def returnAllDishes():
    return dishes.all()

# restaurants functionality
def makeRestaurant(uname):
    restaurants.insert({'username': uname, 'menu' : []})

def editRestaurant(uname, owner_name, loc, cuisine_types, restaurant_img, r_name):
    # TODO menu or dishes as parameter as well
    Restaurant_query = Query()
    restaurants.update({'owner_name': owner_name, 'location': loc, 'cuisine_types': cuisine_types, 'restaurant_image': restaurant_img, 'restaurant_name': r_name}, Restaurant_query.username == uname)

def returnAllRestaurants():
    return restaurants.all()

def findChefs(cuisine_type, loc):
    Restaurant_query = Query()
    if cuisine_type == "Anything" and loc == "Anywhere":
        return returnAllRestaurants()
    elif cuisine_type == "Anything":
        return restaurants.search(Restaurant_query.location == loc)
    elif loc == "Anywhere":
        return restaurants.search(Restaurant_query.cuisine_types.any([cuisine_type]))
    else:
        return restaurants.search((Restaurant_query.location == loc) & (Restaurant_query.cuisine_types.any([cuisine_type])))

# called inside route_addDish()
def addDishToRestaurant(dishID, uname):
    Restaurant_query = Query()
    found_restaurant = restaurants.search(Restaurant_query.username == uname)[0]
    # print(found_restaurant)
    appended_menu = found_restaurant['menu']
    appended_menu.append(dishID)
    restaurants.update({'menu': appended_menu}, Restaurant_query.username == uname)


def returnRestaurantDishes(uname):
    Restaurant_query = Query()
    found_restaurant = restaurants.search(Restaurant_query.username == uname)[0]
    restaurant_menu = found_restaurant['menu']
    print(restaurant_menu)
    dishes_list = []
    for dish_number in restaurant_menu:
        dish = dishes.get(doc_id=dish_number)
        dishes_list.append(dish)
    return dishes_list

def fetchRestaurantProfile(uname):
    Restaurant_query = Query()
    found_restaurant = restaurants.search(Restaurant_query.username == uname)[0]
    dishes_list = returnRestaurantDishes(uname)
    found_restaurant['dishes'] = dishes_list
    return found_restaurant

# def addMenu(uname_list):
#     Restaurant_query = Query()
#     print(uname_list)
#     restaurants.update({'menu': []}, Restaurant_query.username == "Natsu")

'''
Actual Endpoints
'''

@app.route('/home', methods=['GET'])
def jay():
    return jsonify([{"dish_name" : "aloo", "price": 12}, {"dish_name" : "tikki", "price": 20}, {"dish_name" : "dahai", "price": 15}])

@app.route('/api/findChefs', methods=['POST'])
def route_findChefs():
    body = request.get_json()
    cuisine_type = body['cuisine_type']
    location = body['location']
    return jsonify({'result': findChefs(cuisine_type, location)})
    # return "Found chefs!"

@app.route('/api/retrieveDishes', methods=['GET'])
def route_retrieveDishes():

    return ""

@app.route('/api/addDish', methods=['POST'])
def route_addDish():
    body = request.get_json()
    d_name = body['dish_name']
    d_price = body['dish_price']
    d_pic = body['dish_pic']
    d_ingredients = body['dish_ingredients']
    uname = body['username']

    #TODO check return of object ID - done
    dishID = addDish(d_name, d_price, d_pic, d_ingredients)
    print(dishID)
    addDishToRestaurant(dishID, uname)
    return "Successfully added dish"

@app.route('/api/editDish', methods=['POST'])
def route_editDish():
    body = request.get_json()
    d_name = body['dish_name']
    d_price = body['dish_price']
    d_ingredients = body['dish_ingredients']

    editDish(d_name, d_price, d_ingredients)
    return "Successfully edited dish"

@app.route('/api/deleteDish', methods=['POST'])
def route_deleteDish():
    body = request.get_json()
    d_name = body['dish_name']

    deleteDish(d_name)
    return "Successfully deleted dish"


@app.route('/api/fetchRestoProfile', methods=['POST'])
def fetchRestoProfile():
    return ""

@app.route('/api/addUser', methods=['POST'])
def route_addUser():
    body = request.get_json() #the request object here is the request that this endpoint recieves (something that someone sent to this)
    r = request
    print(r)
    print("Hello")
    print(body)
    uname = body['username']
    pwd = body['password']
    email = body['email']
    addUser(uname, pwd, email)
    makeRestaurant(uname)
    return "Successfully added user"

@app.route('/api/editRestaurant', methods=['POST'])
def route_editRestaurant():
    body = request.get_json()
    uname = body['username']
    owner_name = body['owner_name']
    loc = body['location']
    cuisine_types = body['cuisine_types']
    r_img = body['restaurant_image']
    r_name = body['restaurant_name']

    editRestaurant(uname, owner_name, loc, cuisine_types, r_img, r_name)
    return "Successfully edited restaurant"

@app.route('/api/getRestaurantDishes', methods=['POST'])
def route_getRestaurantDishes():
    body = request.get_json()
    uname = body['username']
    dishes_list = returnRestaurantDishes(uname)
    return jsonify({'result': dishes_list})
    # return "Got dishes!"

@app.route('/api/signIn', methods=['POST'])
def route_signIn():
    body = request.get_json()
    uname = body['username']
    pwd = body['password']
    return jsonify({'result': signIn(uname, pwd)})


@app.route('/api/fetchRestaurantProfile', methods=['POST'])
def route_fetchProfile():
    body = request.get_json()
    uname = body['username']
    return jsonify({'result': fetchRestaurantProfile(uname)})

@app.route('/_add_numbers')
def add_numbers():
    a = request.args.get('a', 0, type=int)
    b = request.args.get('b', 0, type=int)
    return jsonify(result=a + b)

'''
Test Endpoints
'''

@app.route('/test/returnAllUsers', methods=['GET'])
def test_returnAllUsers():
    print("Returned!")
    print(returnAllUsers())
    # return jsonify({'result' : returnAllUsers()})
    d = {'result' : returnAllUsers()}
    print(d)
    return str(d)

@app.route('/test/returnAllDishes', methods=['GET'])
def test_returnAllDishes():
    return jsonify({'result': returnAllDishes()})

@app.route('/test/returnAllRestaurants', methods=['GET'])
def test_returnAllRestaurants():
    return jsonify({'result': returnAllRestaurants()})

# @app.route('/test/addMenu', methods=['POST'])
# def test_addMenu():
#     body = request.get_json()
#     uname_list = body['username_list']
#     addMenu(uname_list)
#     return "Added menu"


if __name__ == "__main__":
    app.run(debug=True)

