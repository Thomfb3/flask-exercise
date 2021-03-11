from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    html = """
    <html>
        <body>
            <h1>Flask Greet</h1>
            <p>This is the flask greet home page</p>
            <p><a href='/welcome' >Go to the "Welcome" page</a></p>
            <p><a href='/welcome/home' >Go to the "Welcome/home" page</a></p>
            <p><a href='/welcome/back'>Go to the "Welcome/back" page</a></p>
        </body>
    </html>
    """
    return html

@app.route('/welcome')
def welcome():
    return "welcome"

@app.route('/welcome/home')
def welcome_home():
    return "welcome home"

@app.route('/welcome/back')
def welcome_back():
    return "welcome back"



