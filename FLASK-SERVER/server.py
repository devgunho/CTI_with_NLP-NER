from flask import Flask, render_template, request

import mongodbconnect

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if request.form.get('check_mongodb_btn') == 'check_mongodb':
            mongodbconnect.mongodb_check()
            pass
        elif request.form.get('action2') == 'VALUE2':
            pass
        else:
            pass
    elif request.method == 'GET':
        return render_template('index.html')

    return render_template("index.html")


app.run(host='127.0.0.1', port=8080)
