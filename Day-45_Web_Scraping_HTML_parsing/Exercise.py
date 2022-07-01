from bs4 import BeautifulSoup
import requests
texts = []
links = []
tags = []
response = requests.get("https://news.ycombinator.com/")
yc_webpage = response.text
soup = BeautifulSoup(yc_webpage, "html.parser")
text = soup.find_all("a", class_="titlelink")
for string in text:
    texts.append(string.getText())
    # print(string.getText())
link = soup.find_all("a", class_="titlelink")
for url in text:
    links.append(url.get("href"))
    # print(url.get("href"))
tag = soup.find_all("span", class_="rank")
for num in tag:
    tags.append(num.getText())
    # print(num.getText())

for num in range(len(tags)):
    print(f'{tags[num]}{texts[num]} : {links[num]}')

#
# with open("website.html") as file:
#     content = file.read()
#
# soup = BeautifulSoup(content, "html.parser")
# print(soup.title.string)
#
# anchor_tags = soup.find_all(name="a")
#
# for tag in anchor_tags:
#     print(tag.get("href"))
#
# h3 = soup.find_all("h3", class_="heading")
#
# url = soup.select_one(selector="p a")
# print(url)
#
# id = soup.select_one(selector="#name")
# print(id)
#
# headings = soup.select(".heading")
# print(headings)
