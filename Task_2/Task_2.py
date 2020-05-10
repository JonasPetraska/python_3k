from pymongo import MongoClient
import json

mongoClient = MongoClient()
database = mongoClient.database['python_3k_task2']
restaurants = database['restaurants']

#https://pymongo.readthedocs.io/en/stable/
#https://pymongo.readthedocs.io/en/stable/examples/index.html

def first():
    result = restaurants.find();
    print('Number of records returned: ', restaurants.count_documents({}))
    for record in result:
        print(record)

def second():
    result = restaurants.find({}, {'restaurant_id' : 1, 'name': 1, 'borough': 1, 'cuisine': 1})
    print('Number of records returned: ', restaurants.count_documents({}))
    for record in result:
        print(record)

def third():
    result = restaurants.find({},{"_id": 0, 'restaurant_id' : 1, 'name' : 1, 'borough': 1, 'cuisine': 1})
    print('Number of records returned: ', restaurants.count_documents({}))
    for record in result:
        print(record)

def fourth():
    query = {'borough': "Bronx"}
    result = restaurants.find(query)
    print('Number of records returned: ', restaurants.count_documents(query))
    for record in result:
        print(record)

def fifth():
    query = {'grades': {'$elemMatch': {'score': {'$gte': 80, '$lte': 100 }}}}
    result = restaurants.find(query)
    print('Number of records returned: ', restaurants.count_documents(query))
    for record in result:
        print(record)

#Examples
if __name__ == '__main__':

    #Seed data from json file
    #Run to seed database, if it's empty
    if restaurants.count_documents({}) == 0:
        with open('./Task_2/restaurants.json') as f:
            file_data = json.load(f)
        restaurants.insert_many(file_data)

    print("First task: \n")
    first()

    print("Second task: \n")
    second()

    print("Third task: \n")
    third()

    print("Fourth task: \n")
    fourth()

    print("Fifth task: \n")
    fifth()

    #Close client
    mongoClient.close()
