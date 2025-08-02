import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

response = requests.get(URL)
webpage = response.text
soup = BeautifulSoup(webpage,"html.parser")
movies = soup.find_all(name="h3",class_="title")

movies_list = [ movie.getText() for movie in movies[::-1] ]

with open("movies.txt",mode="w",encoding="utf-8") as text_file :
    for movie in movies_list :
        text_file.write(f"{movie}\n")
   