from flask import render_template
import pymongo

ip = 'localhost'
port = 27017


def show_mongodb_list():

    # Connect MongoDB
    connection = pymongo.MongoClient(ip, port)

    mongodblist = connection.list_database_names()
    print("[*] MongoDB LIST:", mongodblist)
    return mongodblist
