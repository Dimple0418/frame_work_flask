# ROUTING,URL_FOR(),REDIRECTS AND  URL CONVERTRS
'''
@ means decorator line

# url_for()
-----------
--->This flask function used to dynamically generate urls for routes in flask
--->This avoids hardcoding for URLs
---> Automatically updates URLs if route changes

syntax---> url_for('function_name')

# Dynamic Routing 
---------------------
URL --> http://127.0.0.1:5000
--> The dynamic routing means passing values through the url,flask allows URLs to accept variables..

'''
'''
#1) 

from flask import Flask,url_for 
day02=Flask(__name__)

@day02.route('/')

def home():
    return "home page"

@day02.route('/about')
def about():
    return url_for('home')

if __name__=='__main__':
    day02.run(debug=True)

#2
from flask import Flask
day02=Flask(__name__)
name="Dimple"

@day02.route('/')
def home():
    return f"Welcome {name}"

@day02.route('/student/<name>')
def student(name):
    return f"Welcome {name}"

if __name__=='__main__':
    day02.run(debug=True)

#3
from flask import Flask
day02=Flask(__name__)


@day02.route('/student/<name>')
def student(name):
    return f"Welcome {name}"

if __name__=='__main__':
    day02.run(debug=True)


#4
from flask import Flask ,url_for,redirect
day02=Flask(__name__)

@day02.route('/')
def home():
    return redirect(url_for('login'))

@day02.route('/login')
def login():
    return "login page"

if __name__=='__main__':
    day02.run(debug=True)

#5
from flask import Flask, redirect, url_for
app = Flask(__name__)

@app.route('/profile/<username>')
def profile(username):
    return f"welcome {username}"

@app.route('/')
def home():
    return redirect(url_for('profile',username = 'Dimple'))
if __name__ == '__main__':
    app.run(debug=True)

#6

from flask import Flask

app = Flask(__name__)

@app.route('/profile')
def profile():
    return "Welcome Dimple"

if __name__ == '__main__':
    app.run(debug=True)


'''

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)







    