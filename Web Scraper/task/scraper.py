import requests
import json

from bs4 import BeautifulSoup


# def get_movie(url):
#     r = requests.get(url, headers={'Accept-Language': 'en-US,en;q=0.5'})
#
#     soup = BeautifulSoup(r.text, "html.parser")
#     movie_info = json.loads("".join(soup.find("script", {"type": "application/ld+json"}).contents))
#     movie = {}
#     if movie_info["@type"] == "Movie" or movie_info["@type"] == "TVSeries":
#         movie["title"] = movie_info["name"]
#         movie["description"] = movie_info["description"]
#         print(movie)
#     else:
#         print("Invalid movie page!")
#
#
# user_input = input()
# if "https://www.imdb.com/title/" not in user_input:
#     print("Invalid movie page!")
# else:
#     get_movie(user_input)

user_input = input()
file = open('source.html', 'wb')
try:
    r = requests.get(user_input)
    if r.status_code == 200:
        page_content = r.content
        file.write(page_content)
        print("Content saved.")
    else:
        print("The URL returned " + str(r.status_code) + "!")
finally:
    file.close()
