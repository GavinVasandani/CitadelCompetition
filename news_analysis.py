import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from textBlobSent import get_subjectivity, get_polarity

from helper import read_headlines_from_csv, read_dates_from_csv

# url_list = []
date_time = read_dates_from_csv('Copy of packages.csv')
# news_text = []
headlines = read_headlines_from_csv('Copy of packages.csv')


def main():
    # for i in range(1, 5):  # parameters of range function to determine how many pages to go through from 1 to n
    #     # gets the list of all the unique URLs in the webpage, specifically all websites sourced by oilprice.com website is stored in url_list
    #     url = 'https://oilprice.com/Energy/Crude-Oil/Page-{}.html'.format(i)  # sources through each page
    #     request = requests.get(url)  # creates connection to website
    #     soup = BeautifulSoup(request.text, "html.parser")
    #     for links in soup.find_all('div', {
    #         'class': 'categoryArticle'}):  # finds the class: xxxx in the HTML code and measures the xxx information
    #         for info in links.find_all('a'):
    #             if info.get('hrf') not in url_list:
    #                 url_list.append(info.get('href'))
    #
    # print(url_list)  # outputs URL
    #
    # for www in url_list:  # www is a variable which goes over URL_list
    #     headlines.append(www.split("/")[-1].replace('-',
    #                                                 ' '))  # www.split() isn't a website URL it says to split() variable www which is the website URL so that we can replace dashes and later apply sentiment analysis
    #     request = requests.get(www)
    #     soup = BeautifulSoup(request.text, "html.parser")
    #
    #     for dates in soup.find_all('span', {
    #         'class': 'article_byline'}):  # accesses HTML code and looks what occurs after class: variable in order to get date and author of article
    #         print(dates.text)  # outputs list with all dates and authors
    #         date_time.append(dates.text.split('-')[
    #                              -1])  # splits the date and author line and adds dashes, this is then added to the date_time list
    #
    #     temp = []  # creates list to temporarily store all information on the page
    #     for news in soup.find_all(
    #             'p'):  # goes through the HTML code of each web page and looks for <p> which is where paragraphs are stored
    #         temp.append(news.text)  # adds each paragraph's text into the list temp
    #
    #     for last_sentence in reversed(temp):
    #         # goes through the temp list which has all page content and puts it in reverse order.
    #         # it looks for the term 'by' from bottom to top as it usually occurs at the top and indicates that at that point we should stop going through the text.
    #         if last_sentence.split(" ")[0] == "By" and last_sentence.split(" ")[-1] == "Oilprice.com":
    #             break
    #         elif last_sentence.split(" ")[0] == "By":
    #             break
    #
    #     joined_text = ' '.join(temp[temp.index("More Info") + 1:temp.index(last_sentence)])
    #     news_text.append(joined_text)

    news_df = pd.DataFrame({'Date': date_time, 'Headline': headlines})
    news_df.dropna(inplace=True)

    analyzer = SentimentIntensityAnalyzer()  # calls VADER sentiment analysis

    def comp_score(text):
        return analyzer.polarity_scores(text)["compound"]  # returns the "compound" sentiment for the text

    news_df["sentiment"] = news_df["Headline"].apply(comp_score)
    news_df["subjectivity"] = news_df["Headline"].apply(get_subjectivity)
    news_df["polarity"] = news_df["Headline"].apply(get_polarity)
    # print(news_df)

    news_df.to_csv('headline_analysis.csv', index=False)


if __name__ == '__main__':
    main()
