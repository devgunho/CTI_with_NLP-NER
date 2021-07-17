from flask import Flask, render_template, request

import mongodbconnect

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        print("methods: POST")
        if request.form.get("submit_a"):
            print("BTN a push!")
        elif request.form.get("submit_b"):
            print("BTN b push!")
    elif request.method == "GET":
        print("methods: GET")
    return render_template('index.html')


app.run(host='127.0.0.1', port=8080)
