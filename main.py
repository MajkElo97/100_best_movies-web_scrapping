import requests
from bs4 import BeautifulSoup
from pprint import pprint

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

response = requests.get(URL)
# print(response.encoding)
soup = BeautifulSoup(response.text, 'html.parser')
# print(soup.prettify())
movies = soup.find_all(name="h3", class_="title")
movies = [movie.getText() for movie in movies]
movies = [movie for movie in movies[::-1]]
# pprint(movies)

with open(file="movies.txt", mode="w", encoding='ISO-8859-1') as file:
    for movie in movies:
        file.write(f"{movie}\n")
