import requests
import string

from bs4 import BeautifulSoup

website = "https://www.nature.com/nature/articles"


def main():

    saved_articles = []
    req = requests.get(website)

    if req.status_code == 200:

        soup = BeautifulSoup(req.content, "html.parser")
        articles = soup.find_all('article')  # find all articles

        for article in articles:
            span_tags = article.find_all("span", {"class": "c-meta__type"})
            for span in span_tags:
                # check if article type is "News"
                if span.text == "News":

                    # get link of article
                    link = article.find('a').get('href')
                    r = requests.get("https://www.nature.com" + link)
                    soup = BeautifulSoup(r.content, "html.parser")

                    # format title
                    title = soup.find('title').text  # get title of article
                    title = title.translate(str.maketrans('', '', string.punctuation))  # remove punctuation
                    title = title.replace(' ', '_')  # replace whitespace w/ underscore

                    # extract news body
                    body = soup.find('div', {"class": "c-article-body"})
                    body = body.text.strip()

                    # save article to .txt file
                    filename = title + '.txt'
                    file = open(filename, 'wb')
                    file.write(body.encode('utf-8'))
                    saved_articles.append(filename)
                    file.close()

    else:
        print("The URL returned " + str(req.status_code) + "!")

    print(saved_articles)


if __name__ == "__main__":
    main()