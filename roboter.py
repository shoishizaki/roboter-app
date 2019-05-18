import csv_controller

class Roboter():
    def say_roboter_first(self):
        csv = csv_controller.CsvController()
        print("Hello! I'm Roboter. What is your name?")
        name = input('name:')
        print('{}. Which restaurant do you like?'.format(name))
        restaurant = input('restaurant-name:')
        count = 1
        csv.write_csv(restaurant, count)
        print('{}. Thank you.'.format(name))
        print('Have a good day! See you.')

    def say_roboter_second(self):
        csv = csv_controller.CsvController()
        csv.read_csv()
        print("Hello! I'm Roboter. What is your name?")
        name = input('name:')
        print('My favorite restaurant is {}'.format(csv.restaurant_list[1].get_restaurant()))
        print('Do you like this restaurant? [yes/no]')
        answer = input()
        print('{}. Which restaurant do you like?'.format(name))
        restaurant = input('restaurant-name:')
        count = 1
        csv.add_csv(restaurant, count)
        print('{}. Thank you.'.format(name))
        print('Have a good day! See you.')