import json
def database(y):
    movies = open("./movies.json", encoding="utf8")
    data = json.load(movies)
    for index, item in enumerate(data):
        print(index, ":" , item["title"])
    user_input = input("Here is our list of movies! Please enter one of the following variables and we will search for it: genres, title, or year")
    if user_input == "genres":
        user_input = input("What genre are you looking for?")
        for item in data:
            if item["genres"] == [user_input]:
                print(item["title"])
    if user_input == "year":
        user_input = input("What year are you looking for?")
        x = int(user_input)
        for index, item in enumerate(data):
            if item["year"] == x:
                print(f"These movies were produced on {x}: {item["title"]}")
            elif item["year"] > x:
                print(f"These movies were produced after {x}: {item["title"]}")
            elif item["year"] < x:
                print(f"These movies were produced before {x}: {item["title"]}")
    if user_input == "title":
        user_input = input("Please type the specific title of a movie")
        for index, item in enumerate(data):
            if user_input == item["title"]:
                print(f"The movie '{item["title"]}' was produced on {item["year"]}, and falls into the genre(s) of {item["genres"]}.")
database(0)