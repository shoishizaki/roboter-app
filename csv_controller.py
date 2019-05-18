import csv

import pandas as pd

import restaurant

class CsvController():
    def __init__(self):
        self.restaurant_list = []

    def write_csv(self, restaurant, count):
        df = pd.DataFrame([
            [restaurant, count], ],
            columns=['name', 'count'])
        df.to_csv("ranking.csv", index=False)

    def read_csv(self):
        if len(self.restaurant_list) != 0:
            self.restaurant_list =[]

        with open('ranking.csv') as f:
            reader = csv.reader(f)
            l = [row for row in reader]

        for i in range(len(l)):
            r = restaurant.Restaurant(l[i][0], l[i][1])
            self.restaurant_list.append(r)

    def add_csv(self, restaurant, count):
        with open('ranking.csv', 'a') as f:
            print(restaurant, count, file=f)
