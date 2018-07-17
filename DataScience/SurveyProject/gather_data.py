# IMPORT LIBRARIES
import json
import os

def fix_data(file_name):
    with open(file_name, "r") as f:
        a = "".join(f.readlines())
        fixed_data = ",".join(a.split(']['))
    with open(file_name, "w") as f:
        f.write(json.dumps(fixed_data))

def save_data(file_name, data):
    f = open(file_name, "r+")
    old_data = json.load(f) # return a list of data that was already in data.json
    old_data.extend(data) # combine old data with the new data
    f.write(json.dumps(old_data))
    f.close()

questions = {
    "name": "What is your name? ",
    "age": "What is your age? ",
    "homestate": "What is your home state? "
    }
data = [] # 'data' is a list of dictionaries, where each dictionary
            # represents the set of responses corresponding to a user

# Keep gathering data from users until input is NO
while True:
    single_response = {} # dictionary of a single user's responses

                        # NOTE: we want single_response to be cleared (aka
                        # empty) before asking the questions to not interfere
                        # with our user's data

    # Ask all the questions in our dictionary of questions
    for q_type, q in questions.items():
        single_response[q_type] = input(q)
    data.append(single_response)
    print("Thank you for taking the survey, {}!".format(single_response["name"].title()))
    if input("Take the survey again? YES/ NO ") in {"yes", "YES", "Y", "y", "Yes"}:
        continue
    else:
        print("Generating report. . .")
        break

# # IF FILE EXISTS, JUST APPEND TO OLD DATA
# if os.path.isfile("data.json"):
#     f = open("data.json", "r+")
#     #m = json.dumps(f)
#     old_data = json.load(f) # return a list of data that was already in data.json
#     for d in old_data:
#         print(d)
#     #old_data.extend(data) # combine old data with the new data
#     f.write(json.dumps(data))
#     f.close()
#
# # FILE DOES NOT EXIST SO CREATE NEW FILE
# else:
with open("data.json", "w") as f:
    f.write(json.dumps(data))
