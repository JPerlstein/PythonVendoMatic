# Jessica's VendoMatic
Beverage vending machine server built with Python and Flask.
 
Accepts: US quarters only (caveat: 1 coin at a time)

Item price: 2 quarters

Inventory: 3 beverages, 5 items each

Returns: unused coins after purchase

Provides: inventory queries & individual item queries

Uses: JSON and proper HTTP headers

Setup on macOS

Open Terminal and navigate to your project folder:
cd /path/to/vend-o-matic

Create and activate a virtual environment:
python3 -m venv venv
source venv/bin/activate

Install Flask:
pip install Flask

Running the Server

Start the server:

python3 app.py

You should see:

Starting Jessica's Vend-O-Matic server...
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)

Leave this terminal open as the server must be running in order to test.

Example Tests:
NOTE: You will need to insert coin twice in order to purchase item 

Open a new Terminal window and try out the following commands:

Inserting a coin:

curl -X PUT http://127.0.0.1:5000 -H "Content-Type: application/json" -d '{"coin":1}' -i

Purchasing a beverage (item 0):

curl -X PUT http://127.0.0.1:5000/inventory/0 -H "Content-Type: application/json" -i

Checking the inventory:

curl http://127.0.0.1:5000/inventory -i

Returning coins:

curl -X DELETE http://127.0.0.1:5000 -i

Keep in Mind:
1) Inventory resets when server is restarted
2) Extra coins are returned in X-Coins
3) Insufficient coins → 403 Forbidden
4) Out-of-stock → 404 Not Found
5) Only dependency: Flask
6) No re-implementation of HTTP or manual JSON concatenation Stopping the Server

To Exit:
Press CTRL + C in the terminal running the server

Setup on Windows

Open Command Prompt

Navigate to project folder
cd C:\path\to\vend-o-matic

Create a virtual environment:
python -m venv venv

Activate the virtual environment:
venv\Scripts\activate.bat

Install Flask:
pip install Flask
Running the Server (Windows)

Start the server:
python app.py

You should see:

Starting Jessica's Vend-O-Matic server...
 * Running on http://127.0.0.1:5000/

Testing on Windows

Open a new Command Prompt window and run:

NOTE: You will need to insert coin twice in order to purchase item 

Inserting a coin:

curl -X PUT http://127.0.0.1:5000 -H "Content-Type: application/json" -d "{\"coin\":1}" -i

Purchasing a beverage (item 0):

curl -X PUT http://127.0.0.1:5000/inventory/0 -H "Content-Type: application/json" -i

Checking inventory:

curl http://127.0.0.1:5000/inventory -i

Returning coins:

curl -X DELETE http://127.0.0.1:5000 -i

For Windows users:
1) Use venv\Scripts\activate instead of source venv/bin/activate
2) Use CTRL + C to stop the server
3) JSON in curl requires escaped quotes: \"
