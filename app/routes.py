from flask import Flask


app = Flask(__name__)

@app.get('/')
def index():
    me = {
        'first_name': 'Dustin',
        'last_name': 'Jensen',
        'hobbies': 'Learing Python',
        'active': True
    }
    return me


@app.get('/about')
def about_me():
    return render_template('about.html')