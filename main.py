from bs4 import BeautifulSoup
# import lxml   # lmxl parser
# soup = BeautifulSoup(contents, "lmxl")

with open("website.html", "r") as file:
    contents = file.read()

soup = BeautifulSoup(contents, "html.parser")
# print(soup.title)
# print(soup.title.string)

# print(soup.prettify())
# print(soup.p)

all_anchor_tags = soup.find_all(name="a")

for tag in all_anchor_tags:
    # print(tag.getText())
    print(tag.get("href"))

#heading = soup.find_all("h3")
#print(heading)

# h3_heading = soup.find_all(name="h3", class_="heading")
# print(h3_heading)

#name = soup.select_one(selector="#")
#print(name)

#headings = soup.select(".heading")
#print(headings)