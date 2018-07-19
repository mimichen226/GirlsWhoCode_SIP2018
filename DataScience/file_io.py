import json
import os

data = [{"name": "MIMI", "age": 22, "fave_food": ["pizza", "boba", "chocolate"]}]

# IF FILE EXISTS, JUST APPEND TO OLD DATA
if os.path.isfile("data.json"):
    # WHAT TO DO WHEN YOU HAVE NEW DATA BUT YOU ALREADY HAVE A DATA.JSON FILE
    data2 = [{"name": "sandy", "age": 20, "fave_food": ["pizza", "boba", "chocolate"]}]
    f = open("data.json", "r+")
    old_data = json.load(f) # return a list of data that was already in data.json
    old_data.extend(data2) # combine old data with the new data
    f.write(json.dumps(old_data))
    f.close()

# FILE DOES NOT EXIST SO CREATE NEW FILE
else:
    # Create a file called data.json, with the write permission
    f = open("data.json", "w")
    # Turn data (list of dictionaries) into a json object
    json_obj = json.dumps(data)
    # Write the json object to our file
    f.write(json_obj)
    # Close our file
    f.close()
