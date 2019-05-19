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
        with open('ranking.csv') as f:
            reader = csv.reader(f)
            l = [row for row in reader]

        for i in range(len(l)):
            r = restaurant.Restaurant(l[i][0], l[i][1])
            self.restaurant_list.append(r)

    def add_csv(self, restaurant, count, restaurant_list):
        for i in range(1, len(restaurant_list)):
            if restaurant_list[i].get_restaurant() == restaurant:
                restaurant_list[i].set_count(int(restaurant_list[i].get_count())+1)
                df = pd.read_csv('ranking.csv')
                df_new = df.drop(i-1)
                df_new.to_csv("ranking.csv", index=False)
                w = pd.DataFrame([[restaurant, restaurant_list[i].get_count()]])
                w.to_csv("ranking.csv", index=False, mode='a', header=False)
                break

        else:
            w = pd.DataFrame([[restaurant, count]])
            w.to_csv("ranking.csv", index=False, mode='a', header=False)
