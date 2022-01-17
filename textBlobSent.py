from textblob import TextBlob


def get_subjectivity(text):
    return TextBlob(text).sentiment[1]


def get_polarity(text):
    return TextBlob(text).sentiment[0]
