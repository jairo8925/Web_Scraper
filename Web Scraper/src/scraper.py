import requests
import string
import os

from bs4 import BeautifulSoup

website = "https://www.nature.com/nature/articles"


def main():

    saved_articles = []
    pages = int(input())
    article_type = input()
    for i in range(1, pages + 1):
        req = requests.get(website, params={'page': i})

        dir_name = 'Page_' + str(i)
        if not os.path.exists(dir_name):
            os.mkdir(dir_name)

        if req.status_code == 200:

            soup = BeautifulSoup(req.content, "html.parser")
            articles = soup.find_all('article')  # find all articles

            for article in articles:
                span_tags = article.find_all("span", {"class": "c-meta__type"})
                for span in span_tags:
                    # check article type
                    if span.text == article_type:

                        # get link of article
                        link = article.find('a').get('href')
                        r = requests.get("https://www.nature.com" + link)
                        soup = BeautifulSoup(r.content, "html.parser")

                        # format title
                        title = soup.find('meta', {"property": "og:title"}).get('content')  # get title of article
                        title = title.translate(str.maketrans('', '', string.punctuation))  # replace punctuation
                        title = title.replace(' ', '_')  # remove whitespace

                        # extract news body
                        body = soup.find('div', {"class": "c-article-body"})
                        if body is None:
                            body = soup.find('div', {"class": "article-item__body"})
                        if body is None:
                            body = soup.find('article')
                        body = body.text.strip()

                        # save article to .txt file
                        txt_file = title + '.txt'
                        filename = os.path.join(dir_name, txt_file)
                        file = open(filename, 'wb')
                        file.write(body.encode('utf-8'))
                        saved_articles.append(txt_file)
                        file.close()

        else:
            print("The URL returned " + str(req.status_code) + "!")

    print("Saved all articles.")


if __name__ == "__main__":
    main()