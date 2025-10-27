
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
                            break
    if user_input == "year":
        for index, item in enumerate(data):
            if item["year"] == date:
                print(f"These movies were created on {date}: {item["title"]}")
            user_input = input("Would you like to see the movies created before this year?")
            if user_input == "yes":
                print(f"The movies produced before {date} are: {item["title"]}")
database(1980) #searching for the date must be entered here