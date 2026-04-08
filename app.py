# necessary Flask module imports 
from flask import Flask, request, jsonify, make_response

"""
Jessica's Vend-O-Matic Server

About: A beverage vending machine that uses Flask

Important Details:
1) only accepts quarters
2) item price: 2 quarters
3) inventory: 3 types of beverages, 5 items each
4) supports coin insertion, purchase, inventory check, and coin return

For Testing Please: 
Use curl commands to test coin insertion, purchase, inventory, and edge cases

"""

print("Starting Jessica's Vend-O-Matic server...")

# creating Flask app
app = Flask(__name__)

# keeping track of # of coins currently in machine
coins_inserted = 0

# inventory for each type of beverage
inventory = [5, 5, 5]

# route to insert coin
@app.route("/", methods=["PUT"])
def insert_coin():
    global coins_inserted
    # get JSON data from request
    data = request.get_json()
    # validating input, has to be single quarter
    if not data or data.get("coin") != 1:
        # if found to be invalid, bad request
        return "", 400

    coins_inserted += 1 # incrementing # of coins inserted

    # prepping response with 204 no content 
    response = make_response("", 204)
    # X Coins header shows # of coin inserted
    response.headers["X-Coins"] = coins_inserted
    # returning the response
    return response

# route to return ALL inserted coins
@app.route("/", methods=["DELETE"])
def return_coins():
    global coins_inserted

    # storing current coins to return
    coins = coins_inserted
    # resetting machine coin # to 0 
    coins_inserted = 0

    response = make_response("", 204)
    # showing coins returned
    response.headers["X-Coins"] = coins
    return response

# route to full inventory 
@app.route("/inventory", methods=["GET"])
def get_inventory():
  # return inventory list as JSON
    return jsonify(inventory), 200

# route to get single inventory item 
@app.route("/inventory/<int:item_id>", methods=["GET"])
def get_item(item_id):
    # validating item ID, needs to be 0, 1, 2 
    if item_id < 0 or item_id > 2:
        return "", 404
    # return quantity for this item 
    return jsonify(inventory[item_id]), 200

# route to purchase item 
@app.route("/inventory/<int:item_id>", methods=["PUT"])
def purchase(item_id):
    global coins_inserted
    # validate item ID
    if item_id < 0 or item_id > 2:
        response = make_response("", 404)
        response.headers["X-Coins"] = coins_inserted
        return response
    # check if item out of stock 
    if inventory[item_id] == 0:
        coins = coins_inserted
        coins_inserted = 0
        # responding w/404 not found & coins returned
        response = make_response("", 404)
        response.headers["X-Coins"] = coins
        return response
    # check if enough coins were inserted 
    if coins_inserted < 2:
      # not enough coins
        response = make_response("", 403)
        response.headers["X-Coins"] = coins_inserted
        return response
    # decrement inventory
    inventory[item_id] -= 1
    # calculating change to return to customer
    change = coins_inserted - 2
    # resetting machine coins 
    coins_inserted = 0
  
    # response with JSON displays quantity vended
    response = make_response(jsonify({"quantity": 1}), 200)
    response.headers["X-Coins"] = change
    response.headers["X-Inventory-Remaining"] = inventory[item_id]

    return response

# running server
if __name__ == "__main__":
    app.run(debug=True)