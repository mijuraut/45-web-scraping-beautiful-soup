from bs4 import BeautifulSoup
# import lxml   # lmxl parser
# soup = BeautifulSoup(contents, "lmxl")

with open("website.html", "r") as file:
    contents = file.read()

soup = BeautifulSoup(contents, "html.parser")
# print(soup.title)
# print(soup.title.string)

print(soup.prettify())
print(soup.p)