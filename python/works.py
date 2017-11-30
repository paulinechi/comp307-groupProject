import json
from pprint import pprint

def main():
    f = open("./sellers.json", "r+")
    json_data = json.load(f)
    json_data["sellers"][0]["seller_name"] = "Jack"
    item1 = json_data["sellers"][0]["menu"][0]
    # item1["item_name"] = "Chicken"
    item1["item_price"] = 5.25
    first_seller_menu = json_data["sellers"][0]["menu"]
    # del first_seller_menu[0]
    menu_length = len(first_seller_menu)
    added_item = {"item_id": menu_length + 1, "item_name": "Poutine", "item_picture": "", "item_ingredients": ["Fries", "Gravy"],"item_price": "6.75"}
    first_seller_menu.append(added_item)
    # print first_seller_menu[0]["item_name"]

    f.seek(0)
    f.write(json.dumps(json_data, indent=4))
    f.close()

main()