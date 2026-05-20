'''

WEB : -- (www)
--> The world wide web is a collection of websites and web pages connected through the network where users can access these websites using web browser .

WEB BROWSER : 
--> A web browser is a software usd to access and display webpages 

WEB SERVER :
--> A web server stores websites files and sends webpage to users when they request through a browser ...

WEB APPLICATION :
-> A web application is a software that runs and sends inside a browser and allows user to interact with data and 


# -- 1)
from flask import Flask

app=Flask(__name__)
@app.route('/')
def home():
    return "wellcome to flask application "

if __name__=='__main__':
    app.run(debug=True)
'''

from flask import Flask
app = Flask(__name__)  
@app.route('/')
def home():
    return """
    <html>
    <head>
        <style>
            h1{
                color: black;
                background-color:white;
                text-align: center;
                padding: 100px;
                font-size: 40px;
            }
            body{
            display:flex;
             background-color: pink;
            justify-content:center;
            align-items:center
            }
        </style>
    </head>
    <body>
    
        <h1>Welcome to Flask Application</h1>
   
    </body>
    </html>
    """

if __name__ == '__main__':
    app.run(debug=True)






























