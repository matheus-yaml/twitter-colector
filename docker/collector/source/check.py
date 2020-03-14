from pymongo import MongoClient

count = 0

while count < 3:
    print('trying to connect with database')
    try:
        print(MongoClient(host='mongodb', serverSelectionTimeoutMS=5000).server_info())
        break
    except:
        count = count + 1
        print('Database connection fail')