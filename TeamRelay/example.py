food = {"asparagus": {"type": "veggie", "PLU": 3079},
		"pistachio": {"type": "nut", "PLU": 4941},
		"avocado": {"type": "fruit", "PLU": 3354}
		}

for food_name, food_info in food.items():
	print("{} is a {}".format(food_name, food_info["type"]))
