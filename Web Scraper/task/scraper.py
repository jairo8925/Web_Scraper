import requests
import json

from bs4 import BeautifulSoup


import requests
import string

from bs4 import BeautifulSoup


def main():
    saved_articles = []
    links = []
    r = requests.get("https://www.nature.com/nature/articles")
    if r.status_code == 200:
        page_content = r.content
        soup = BeautifulSoup(page_content, "html.parser")
        articles = soup.find_all('article')
        for a in articles:
            span_tags = a.find_all("span", {"class": "c-meta__type"})
            for t in span_tags:
                if t.text == "News":
                    link = a.find('a')
                    links.append(link.get('href'))
        # print(links)
        for a in links:
            r = requests.get("https://www.nature.com" + a)
            soup = BeautifulSoup(r.content, "html.parser")
            title = soup.find('title').text
            title = title.translate(str.maketrans('', '', string.punctuation))
            title = title.replace(' ', '_')
            body = soup.find('div', {"class": "c-article-body"})
            body = body.text.strip()
            # body = body.replace("\n", "")
            filename = title + ".txt"
            file = open(filename, "wb")
            file.write(body.encode('utf-8'))
            file.close()
            # print(title)
            # print(body)
            saved_articles.append(filename)
    else:
        print("The URL returned " + str(r.status_code) + "!")

    print(saved_articles)


if __name__ == "__main__":
    main()
