from bs4 import BeautifulSoup
import requests


response = requests.get(url="https://news.ycombinator.com/news")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")

article_texts = []
article_links = []


articles = soup.find_all("span", class_="titleline")
# print(articles)
for article in articles:
    article_link = article.find("a").get("href")
    article_links.append(article_link)
    article_text = article.find("a").getText()
    article_texts.append(article_text)

article_upvotes = soup.find_all("span", class_="score")

scores = [int(upvote.getText().split()[0]) for upvote in article_upvotes]

# print(article_texts)
# print(article_links)
# print(scores)
highest_upvote = 0
for score in scores:
    if score > highest_upvote:
        highest_upvote = score
# print(highest_upvote)

real_index = scores.index(highest_upvote)
heading = article_texts[real_index]
link = article_links[real_index]
print(f"The highest upvotes is {highest_upvote}, with the headline {heading}\nUse this link to access the page {link}")
