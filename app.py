
import json
def database(date):
    movies = open("./movies.json", encoding="utf8")
    data = json.load(movies)
    for index, item in enumerate(data):
        print(index, ":" , item["title"])
    user_input = input("Here is our list of movies! Please enter one of the following variables and we will search for it: genres, title, or year")
    if user_input == "genres":
        user_input = input("What genre are you looking for?")
        if user_input == "comedy":
            for index, item in enumerate(data):
                if item["genres"] == ["Comedy"]:
                    print(index, ":" , item["title"])
                    user_input = input("Is this the movie you are looking for? If so, please type its title word for word, if not, please click enter to select the next.")
                    for index, item in enumerate(data):
                        if item["title"] == user_input:
                            print(f"{item["title"]} was made in {item["year"]}, and falls under the {item["genres"]} genre")
        elif user_input == "drama":
            for index, item in enumerate(data):
                if item["genres"] == ["Drama"]:
                    print(index, ":" , item["title"])
                    user_input = input("Is this the movie you are looking for? If so, please type its title word for word, if not, please click enter to select the next.")
                    for index, item in enumerate(data):
                        if item["title"] == user_input:
                            print(f"{item["title"]} was made in {item["year"]}, and falls under the {item["genres"]} genre")
        elif user_input == "Romance":
            for index, item in enumerate(data):
                if item["genres"] == ["Romance"]:
                    print(index, ":" , item["title"])
                    user_input = input("Is this the movie you are looking for? If so, please type its title word for word, if not, please click enter to select the next.")
                    for index, item in enumerate(data):
                        if item["title"] == user_input:
                            print(f"{item["title"]} was made in {item["year"]}, and falls under the {item["genres"]} genre")
        elif user_input == "Animated":
            for index, item in enumerate(data):
                if item["genres"] == ["Animated"]:
                    print(index, ":" , item["title"])
                    user_input = input("Is this the movie you are looking for? If so, please type its title word for word, if not, please click enter to select the next.")
                    for index, item in enumerate(data):
                        if item["title"] == user_input:
                            print(f"{item["title"]} was made in {item["year"]}, and falls under the {item["genres"]} genre")
        elif user_input == "Action":
            for index, item in enumerate(data):
                if item["genres"] == ["Action"]:
                    print(index, ":" , item["title"])
                    user_input = input("Is this the movie you are looking for? If so, please type its title word for word, if not, please click enter to select the next.")
                    for index, item in enumerate(data):
                        if item["title"] == user_input:
                            print(f"{item["title"]} was made in {item["year"]}, and falls under the {item["genres"]} genre")
        elif user_input == "Science Fiction":
            for index, item in enumerate(data):
                if item["genres"] == ["Science Fiction"]:
                    print(index, ":" , item["title"])
                    user_input = input("Is this the movie you are looking for? If so, please type its title word for word, if not, please click enter to select the next.")
                    for index, item in enumerate(data):
                        if item["title"] == user_input:
                            print(f"{item["title"]} was made in {item["year"]}, and falls under the {item["genres"]} genre")
        elif user_input == "Thriller":
            for index, item in enumerate(data):
                if item["genres"] == ["Thriller"]:
                    print(index, ":" , item["title"])
                    user_input = input("Is this the movie you are looking for? If so, please type its title word for word, if not, please click enter to select the next.")
                    for index, item in enumerate(data):
                        if item["title"] == user_input:
                            print(f"{item["title"]} was made in {item["year"]}, and falls under the {item["genres"]} genre")
        elif user_input == "Horror":
            for index, item in enumerate(data):
                if item["genres"] == ["Horror"]:
                    print(index, ":" , item["title"])
                    user_input = input("Is this the movie you are looking for? If so, please type its title word for word, if not, please click enter to select the next.")
                    for index, item in enumerate(data):
                        if item["title"] == user_input:
                            print(f"{item["title"]} was made in {item["year"]}, and falls under the {item["genres"]} genre")
        elif user_input == "Superhero":
            for index, item in enumerate(data):
                if item["genres"] == ["Superhero"]:
                    print(index, ":" , item["title"])
                    user_input = input("Is this the movie you are looking for? If so, please type its title word for word, if not, please click enter to select the next.")
                    for index, item in enumerate(data):
                        if item["title"] == user_input:
                            print(f"{item["title"]} was made in {item["year"]}, and falls under the {item["genres"]} genre")
        elif user_input == "Fantasy":
            for index, item in enumerate(data):
                if item["genres"] == ["Fantasy"]:
                    print(index, ":" , item["title"])
                    user_input = input("Is this the movie you are looking for? If so, please type its title word for word, if not, please click enter to select the next.")
                    for index, item in enumerate(data):
                        if item["title"] == user_input:
                            print(f"{item["title"]} was made in {item["year"]}, and falls under the {item["genres"]} genre")
        elif user_input == "Biography":
            for index, item in enumerate(data):
                if item["genres"] == ["Biography"]:
                    print(index, ":" , item["title"])
                    user_input = input("Is this the movie you are looking for? If so, please type its title word for word, if not, please click enter to select the next.")
                    for index, item in enumerate(data):
                        if item["title"] == user_input:
                            print(f"{item["title"]} was made in {item["year"]}, and falls under the {item["genres"]} genre")
        elif user_input == "Crime":
            for index, item in enumerate(data):
                if item["genres"] == ["Crime"]:
                    print(index, ":" , item["title"])
                    user_input = input("Is this the movie you are looking for? If so, please type its title word for word, if not, please click enter to select the next.")
                    for index, item in enumerate(data):
                        if item["title"] == user_input:
                            print(f"{item["title"]} was made in {item["year"]}, and falls under the {item["genres"]} genre")
        elif user_input == "Spy":
            for index, item in enumerate(data):
                if item["genres"] == ["Spy"]:
                    print(index, ":" , item["title"])
                    user_input = input("Is this the movie you are looking for? If so, please type its title word for word, if not, please click enter to select the next.")
                    for index, item in enumerate(data):
                        if item["title"] == user_input:
                            print(f"{item["title"]} was made in {item["year"]}, and falls under the {item["genres"]} genre")
    if user_input == "year":
        for index, item in enumerate(data):
            if item["year"] == date:
                print(f"These movies were created on {date}: {item["title"]}")
            elif item["year"] > date:
                print(f"These movies were produced after {date}: {item["title"]}")
            elif item["year"] < date:
                print(f"These movies were produced before {date}: {item["title"]}")
    if user_input == "title":
        user_input = input("What movie are you looking for?")
        if item["title"] == user_input:
            print(f"This movie was created on {item["year"]} and falls under the {item["genre"]} category")
database(2020) #searching for the date must be entered here