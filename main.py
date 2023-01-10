

from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")

titleline_tags = soup.find_all(class_="titleline")
# print(titleline_tags.contents[0])    #<a href="https://lisp-journey.gitlab.io/blog/these-years-in-common-lisp-2022-in-review/">Years in Common Lisp: 2022 in review</a>

texts = []
links = []

for titleline_tag in titleline_tags:
    text = titleline_tag.contents[0].getText()
    texts.append(text)
    link = titleline_tag.contents[0].get('href')
    links.append(link)

#article_link = titleline_tag.contents[0].get('href')
#print(f"article link: {article_link}")

print(texts)
print(links)

article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(class_="score")]

high_score_index = 0
high_score = 0
for x in range(len(article_upvotes)):
    if article_upvotes[x] > high_score:
        high_score = article_upvotes[x]
        high_score_index = x

print(f"The title: {texts[high_score_index]}")
print(f"The link: {links[high_score_index]}")














# import lxml   # lmxl parser
# soup = BeautifulSoup(contents, "lmxl")

#with open("website.html", "r") as file:
#    contents = file.read()

#soup = BeautifulSoup(contents, "html.parser")
# print(soup.title)
# print(soup.title.string)

# print(soup.prettify())
# print(soup.p)

#all_anchor_tags = soup.find_all(name="a")

#for tag in all_anchor_tags:
    # print(tag.getText())
    # print(tag.get("href"))

#heading = soup.find_all("h3")
#print(heading)

# h3_heading = soup.find_all(name="h3", class_="heading")
# print(h3_heading)

#name = soup.select_one(selector="#")
#print(name)

#headings = soup.select(".heading")
#print(headings)

