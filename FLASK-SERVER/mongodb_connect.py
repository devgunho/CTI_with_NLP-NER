import pymongo

ip = 'localhost'
port = 27017


def show_mongodb_list():

    # Connect MongoDB
    connection = pymongo.MongoClient(ip, port)
    try:
        mongodblist = connection.list_database_names()
        print("[*] MongoDB LIST:", mongodblist)
        return mongodblist
    except:
        print("[-] Connection ERROR!")

def run_mongodb():
    show_mongodb_list()

if __name__ == "__main__":
    run_mongodb()
