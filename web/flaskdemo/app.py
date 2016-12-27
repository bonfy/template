# coding:utf-8

from flask import Flask, jsonify
from models import *

app = Flask(__name__)

@app.before_request
def before_request():
    # create db if needed and connect
    initialize_db()

@app.teardown_request
def teardown_request(exception):
    # close the db connection
    db.close()

@app.route('/')
def home():
    return 'hello world'

@app.route('/posts')
def get_posts():
    posts = Post.select()
    data = [dict(title=p.title,date=p.date) for p in posts]
    return jsonify(data)

if __name__ == '__main__':
    app.run(port=5000, debug=True)
