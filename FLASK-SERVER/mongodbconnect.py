import pymongo

def mongodb_check():
    ip = 'localhost'
    port = 27017

    # Connect MongoDB
    connection = pymongo.MongoClient(ip, port)

    print(connection.list_database_names())