# Web Scraper

A Python program that takes a website address and parses its data to be saved to a text file. Sends an HTTP request to the website and uses BeautifulSoup to parse its data. Specifically, this program scrapes articles from https://www.nature.com/nature/articles and saves each one in a separate .txt file. 

### <a href="https://github.com/jairo8925/Multilingual_Online_Translator">The multilingual online translator can be found here</a>

To start, provide the number of pages to specify the number of pages on which the program should look for the articles. 
Next, provide the type of article that the program should look for (eg. News, Correspondence, Research Highlight). After
the program is done, the articles will be saved in the directories Page_1 to Page_N (N corresponds to page number), depending on
what page an article was found in.
