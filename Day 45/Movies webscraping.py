import requests
from bs4 import BeautifulSoup


response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
movie_site = response.text

soup = BeautifulSoup(movie_site, "html.parser")
# print(soup.title.getText().split("|")[0])

all_movies = soup.find_all(name="h3", class_="title")
tiltles = [movie.getText() for movie in all_movies]
tiltles.reverse()
for title in tiltles:
    print(title)