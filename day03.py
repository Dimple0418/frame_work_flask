'''
URL converters
------------------
1.IntConverter
------------------



'''

#1 - int converter
'''
from flask import Flask,redirect,url_for
app=Flask(__name__)

@app.route('/marks/<int:score>')
def marks(score):
    return f"marks ={score}"

@app.route('/')
def home():
    return redirect(url_for('marks',score=100))

if __name__=='__main__':
    app.run(debug=True)


#2- float converter

from flask import Flask,redirect,url_for
app=Flask(__name__)

@app.route('/price/<float:bill>')
def price(bill):
    return f"price ={bill}"

@app.route('/')
def home():
    return redirect(url_for('price',bill=667.80))

if __name__=='__main__':
    app.run(debug=True)


#3 

from flask import Flask,redirect,url_for
app=Flask(__name__)

@app.route('/user/<uuid:user_id>')
def user(user_id):
    return f"User Id ={user_id}"

@app.route('/')
def home():
    return redirect(url_for('user',user_id="123e4567-e89b-12d3-a456-426614174000"))

if __name__=='__main__':
    app.run(debug=True)
'''

'''
HHTP REQUEST METHODS
---------------------
This HTTP requests methods are used for communication between  a client (browser/app) and a server in web development and APIs.

1. GET request
----------------



#1-- GET method

from flask import Flask
app=Flask(__name__)

@app.route('/',methods=['GET'])
def home():
    return "THIS IS GET REQUEST"


if __name__=='__main__':
    app.run(debug=True)


#2 - eg
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "WELCOME"

@app.route('/home', methods=['GET'])
def home():
    return "THIS IS GET REQUEST"

if __name__ == '__main__':
    app.run(debug=True)

'''
#3 --  POST method

# from flask import Flask, request
# app = Flask(__name__)

# @app.route('/', methods=['POST'])
# def submit():
#     name = request.form.get('name')
#     return f"Welcome{name}"

# if __name__ == '__main__':
#     app.run(debug=True)


# from flask import Flask, request

# app = Flask(__name__)

# @app.route('/', methods=['POST'])
# def submit():

#     name = request.form.get('name')

#     return f"Welcome {name}"

# if __name__ == '__main__':
#     app.run(debug=True)


