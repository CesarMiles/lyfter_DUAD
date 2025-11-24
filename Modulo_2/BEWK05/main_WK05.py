from flask import Flask
from api import get_methods, patch_methods, post_methods

app = Flask(__name__)

get_methods(app)
patch_methods(app)
post_methods(app)


app.run(host='localhost', debug=True)