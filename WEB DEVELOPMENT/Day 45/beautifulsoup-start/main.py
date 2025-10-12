from bs4 import BeautifulSoup
import requests
response = requests.get("https://news.ycombinator.com/news")
webpage = response.text
soup = BeautifulSoup(webpage,"html.parser")
article = soup.find_all(name="span",class_="titleline")

article_names = []
article_links =  []
article_votes = [int(votes.getText().split()[0]) for votes in soup.find_all(class_="score",name="span")]
for content in article:
    article_names.append(content.a.get_text())
    article_links.append(content.a.get("href"))
    
print(article_names)
print(article_links)
print(article_votes)
print(article_names[article_votes.index(max(article_votes))],article_links[article_votes.index(max(article_votes))])