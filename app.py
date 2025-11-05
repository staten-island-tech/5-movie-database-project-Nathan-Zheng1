import json
def database(y):
    movies = open("./movies.json", encoding="utf8")
    data = json.load(movies)
    for index, item in enumerate(data):
        print(index, ":" , item["title"])
    name = item["title"]
    date = item["year"]
    genre = item["genres"]
    description = item["extract"]
    user_input = input("Here is our list of movies! Please enter one of the following variables and we will search for it: genres, title, or year")
    if user_input is not "genres":
        print("Invalid Input")
        return
    if user_input == "genres":
        user_input = input("What genre are you looking for?")
        if genre is not user_input:
            print("Invalid Input")
            return
        if genre == [user_input]:
            print(item["title"])
    if user_input == "year":
        user_input = input("What year are you looking for?")
        x = int(user_input)
        if date == x:
            print(f"These movies were produced on {x}: {name}")
        elif date > x:
            print(f"These movies were produced after {x}: {name}")
        elif date < x:
            print(f"These movies were produced before {x}: {name}")
    if user_input == "title":
        user_input = input("Please type the specific title of a movie")
        for index, item in enumerate(data):
            if user_input == name:
                print(f"The movie '{name}' was produced on {date}, and falls into the genre(s) of {genre}. {description}")
database(0)