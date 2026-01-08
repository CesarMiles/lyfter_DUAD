from flask import Flask
from user_module import user_api_methods
from product_module import product_api_methods
from purchase_module import purchase_api_methods


app = Flask(__name__)

user_api_methods(app)
product_api_methods(app)
purchase_api_methods(app)


app.run(host='localhost', debug=True)