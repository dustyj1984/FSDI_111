from flask import Flask, render_template



app = Flask(__name__)

@app.get('/')
def index():
    me = {
        'first_name': 'Dustin',
        'last_name': 'Jensen',
        'hobbies': 'Learing Anything New',
        'active': True
    }
    return me


@app.get('/about')
def about_me():
    return render_template('index.html')