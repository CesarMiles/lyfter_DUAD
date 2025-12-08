from flask import Flask
from user_api import user_api_methods
from product_api import product_api_methods

app = Flask(__name__)

user_api_methods(app)
product_api_methods(app)


app.run(host='localhost', debug=True)