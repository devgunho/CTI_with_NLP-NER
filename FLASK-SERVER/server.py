from flask import Flask, render_template, request

import mongodb_connect

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        print("[+] methods: POST")
        if request.form.get("mongo_check"):
            print("[+] MongoDB Connection Check btn. pushed!")
            mongodb_connect.show_mongodb_list()
        elif request.form.get("submit_b"):
            print("BTN b push!")
    elif request.method == "GET":
        print("[+] methods: GET")
    return render_template('index.html')


app.run(host='127.0.0.1', port=8080)
