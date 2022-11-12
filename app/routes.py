from flask import Flask


app = Flask(__name__)

@app.get('/')
def index():
    me = {
        'first_name': 'John',
        'last_name': 'Doe',
        'hobbies': 'DIY Stuff',
        'active': True
    }
    return me


@app.get('/about')
def about_me():
    return render_template('about.html')