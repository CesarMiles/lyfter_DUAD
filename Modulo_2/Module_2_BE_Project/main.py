from flask import Flask
from user_module import user_api_methods


app = Flask(__name__)

user_api_methods(app)



app.run(host='localhost', debug=True)