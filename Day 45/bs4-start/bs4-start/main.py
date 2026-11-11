from bs4 import BeautifulSoup
import lxml

with open(file="./bs4-start/website.html") as data:
    contents = data.read()
    # print(contents)

soup = BeautifulSoup(contents, "html.parser")
# print(soup.title.string)

all_tags = soup.find_all(name="a")
# for text in all_tags:
#     # print(text.get_text())
#     print(text.get("href"))


heading = soup.find(name="h1", id="name")
# print(heading.string)
heading3 = soup.find(name="h3", class_="heading")
print(heading3)