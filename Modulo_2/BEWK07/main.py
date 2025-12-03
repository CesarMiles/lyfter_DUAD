from flask import Flask
from api import RegisterUserAPI

app = Flask(__name__)

register_user =RegisterUserAPI.as_view('register_user_api')
app.add_url_rule('/register', view_func=register_user, methods=['POST'])


app.run(host='localhost', debug=True)