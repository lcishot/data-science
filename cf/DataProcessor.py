# -*- coding: utf-8 -*-
import csv
import pandas as pd
import numpy as np


class DataProcessor:
    def __init__(self):
        return

    @staticmethod
    def process_rating_data1(raw_data_filename=None):
        with open(raw_data_filename) as csvFile:
            reader = csv.DictReader(csvFile)
            for row in reader:
                print(row['userId'], row['rating'], reader.line_num)

    @staticmethod
    def process_rating_data2(raw_data_filename=None):
        # df = pd.read_csv(raw_data_filename, header=['userId', 'movieId', 'rating', 'timestamp'])
        return pd.read_csv(raw_data_filename)


if __name__ == "__main__":
    print "hello python"
    df = DataProcessor.process_rating_data2("../resources/ratings.csv")
    print df.head()
