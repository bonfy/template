# coding:utf-8
from flask import Flask

app = Flask(__name__)

@app.route('/')
def main():
    return 'hello world'

if __name__ == "__main__":
    app.run(port=8080, debug=True)
