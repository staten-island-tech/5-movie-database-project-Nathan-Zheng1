
import json
movies = open("./movies.json", encoding="utf8")
data = json.load(movies)
for index, item in enumerate(data):
    print(index, ":" , item["title"])
user_input = input("Here is our list of movies! Please enter one of the following variables and we will search for it: genres, title, or year")
if user_input == "genres":
    user_input = input("What genre are you looking for?")
    if user_input == "comedy":
        for index, item in enumerate(data):
            if item["genres"] == "Comedy":
                print(f"All the movies listed fall under the genre of comedy: {item["title"]}")
                user_input = input("Are any of these movies the one you are looking for? If so, please type its title word for word.")
                for index, item in enumerate(data):
                    if item["title"] == user_input:
                        print(f"{item["title"]} was made in {item["year"]}, and falls under the {item["genres"]} genre")
if user_input == "year":
    user_input = input("Please enter a year you would like us to search for:")
    for index, item in enumerate(movies):
        if item["year"] == user_input:
            print(f"These movies were created on {user_input}: {item["title"]}")
        if item["year"] < user_input:
            print(f"These movies were created before {user_input}: {item["title"]}")
        if item["year"] > user_input:
            print(f"These movies were produced after {user_input}: {item["title"]}")

