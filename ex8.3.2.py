mariah_dict = {
    "first_name": "Mariah",
    "last_name": "Carey",
    "birth_date": "27.03.1970",
    "hobbies": ["Sing", "Compose", "Act"]
}

user_input = int(input("Enter a number between 1 and 7: "))

if user_input == 1:
    print(mariah_dict["last_name"])
elif user_input == 2:
    print(mariah_dict["birth_date"][3:5])
elif user_input == 3:
    print(len(mariah_dict["hobbies"]))
elif user_input == 4:
    print(mariah_dict["hobbies"][-1])
elif user_input == 5:
    mariah_dict["hobbies"].append("Cooking")
    print(mariah_dict["hobbies"])
elif user_input == 6:
    birth_date_tuple = tuple(map(int, mariah_dict["birth_date"].split(".")))
    print(birth_date_tuple)
elif user_input == 7:
    birth_year = int(mariah_dict["birth_date"][-4:])
    current_year = 2023 # set the current year manually
    age = current_year - birth_year
    mariah_dict["age"] = age
    print(mariah_dict)
