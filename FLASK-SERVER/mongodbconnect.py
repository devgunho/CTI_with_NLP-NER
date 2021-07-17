from flask import render_template
import pymongo


def show_mongodb_list():
    ip = 'localhost'
    port = 27017

    # Connect MongoDB
    connection = pymongo.MongoClient(ip, port)


    mongodblist = connection.list_database_names()
    print("[*] MongoDB LIST:", mongodblist)
