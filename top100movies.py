import json
import requests
from bs4 import BeautifulSoup


url = "https://www.empireonline.com/movies/features/best-movies-2/"

soup = BeautifulSoup(requests.get(url).content, "html.parser")
data = json.loads(soup.select_one("#__NEXT_DATA__").contents[0])

# uncomment this to print all data:
# print(json.dumps(data, indent=4))


def find_articles(data):
    counter = 50
    if isinstance(data, dict):  # isinstance checks if data is of type dict
        for key, value in data.items():
            if key.startswith("ImageMeta:"):
                yield value["titleText"]
            else:
                try:
                    yield from find_articles(value)
                except Exception:
                    pass
    elif isinstance(data, list):
        for i in data:
            yield from find_articles(i)


def reversed_iterator(iter):
    return reversed(list(iter))

orig = find_articles(data)
reversed = reversed_iterator(orig)

with open("top100movies.txt", "w") as file:
    print("Top 100 movies of all time", file=file)
    print("--------------------------", file=file)
    for row in reversed:
        print(row, file=file)


