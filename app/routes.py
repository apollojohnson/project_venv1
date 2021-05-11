from app import app
from flask import render_template

@app.route('/')
def index():
    context = {
       'title': 'HOME',
       'items': ['apple', 'banana', 'orange', 'pear', 'watermelon', 'grapefruit', 'grapes'],
       'user': {
            'id': 2,
            'username': 'Brian'
        }  
    }
    return render_template('index.html', **context)


@app.route('/top_5')
def top_5():
    title = 'Top Five'
    return render_template('top_5.html', title=title)