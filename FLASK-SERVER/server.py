from flask import Flask, render_template, request

import run_crawling
import run_mongodb
import run_ner

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        print("[+] Methods: POST")
        if request.form.get("mongo_check"):
            print("[+] MongoDB Connection Check btn. pushed!")
            run_mongodb.run()
        if request.form.get("crawling_start"):
            print("[+] Start Crawling btn. pushed!")
            run_crawling.run()
        elif request.form.get("ner_train_start"):
            print("[+] Named Entity Recognition using BERT training Start btn. pushed!")
            run_ner.ner_main()
    elif request.method == "GET":
        print("[+] Methods: GET")
    return render_template('index.html')


app.run(host='127.0.0.1', port=9999)
