from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

analyzer = SentimentIntensityAnalyzer()
titles = ["This is a good course", "This course sucks!", "Fuck this course", "I fucking hate this course so much!!!!",
          "This is an awesome course", "The instructor is so cool!", "The instructor is so cool!!!!",
          "The instructor is so COOL!", "Machine learning makes me :)", "His antics had me ROFL", "The movie SUX"]
print(type(titles))

for title in titles:
    print(title)
    print(analyzer.polarity_scores(title))
    if analyzer.polarity_scores(title)['compound'] >= 0.5:
        print('Very positive sentiment')
    elif 0.5 > analyzer.polarity_scores(title)['compound'] > 0:
        print('Moderately positive sentiment')
    elif analyzer.polarity_scores(title)['compound'] == 0:
        print('Neutral sentiment')
    elif 0 > analyzer.polarity_scores(title)['compound'] > -0.5:
        print('Moderately negative sentiment')
    else:
        print('Very negative sentiment')
