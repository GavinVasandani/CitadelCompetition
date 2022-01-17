import pandas as pd


def read_headlines_from_csv(file: str):
    df = pd.read_csv(file)
    headlines = df['headline'].tolist()
    return headlines


def read_dates_from_csv(file: str):
    df = pd.read_csv(file)
    headlines = df['created_at'].tolist()
    return headlines

