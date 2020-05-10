from pymongo import MongoClient
import json

mongoClient = MongoClient()
database = mongoClient.database['python_3k_task2']
restaurants = database['restaurants']

def first():
    query = restaurants.find();
    for record in query:
        print(record)


#Examples
if __name__ == '__main__':

    #Seed data from json file
    #Run on first startup
    #with open('./Task_2/restaurants.json') as f:
    #    file_data = json.load(f)

    #restaurants.insert_many(file_data)

    print("First task: \n")
    first()





    mongoClient.close()
