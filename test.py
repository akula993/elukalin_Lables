import time
# pip install pandas
import pandas as pd


def count_records():
    data = pd.read_csv('netflix_titles.csv')
    print("Всего фильмов:", data.shape[0])


if __name__ == "__main__":
    count_records()
    time.sleep(5)