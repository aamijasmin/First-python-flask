# To run flask application
# run this command 
# pytho3 -m flask --app main --debug run
from flask import Flask, render_template
import time

app = Flask(__name__)

user_1 = {
        "name":'jasmin',
        "phone":'6297063622',
        "add":'cooch behar',
        "married": "complicated"
        }

user_2 = {
        "name":'barun_sir',
        "phone":'7718374808',
        "add":'Siliguri',
        "married": "complicated"
        }

@app.route("/")
def home():
    n = user_2["name"]
    d = time.ctime(time.time())
    e = str(d)
    return render_template('home.html', d=e, n=n)
    # return f'<p><b>Local Time :</b>{time.ctime(time.time())}</p>'


@app.route("/contact")
def contacts():
    return {
            user_1["name"] : user_1["phone"],
            user_2["name"] : user_2["phone"]
            }


@app.route("/life")
def welcome_my_life():
    return "<h2> WELCOME J_IS WAITING FOR YR_L! </h2>"
@app.route("/html")
def html():
    
    return render_template('hello.html')
    # return "<h1>THIS IS MY 1ST HTML FILE"
