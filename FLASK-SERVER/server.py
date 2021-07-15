from flask import Flask
app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello World!'


app.run(host='127.0.0.1', port=8080)
