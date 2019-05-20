import csv_controller
import roboter_question

class Roboter():
    def say_roboter_first(self):
        csv = csv_controller.CsvController()
        question = roboter_question.QuestionRoboter()

        question.question_name()

        name = input('name:')

        question.queston_restaurant(name)

        restaurant = input('restaurant-name:')
        count = 1

        csv.write_csv(restaurant, count)

        print('{}. Thank you.'.format(name))
        print('Have a good day! See you.')

    def say_roboter_second_and_subsequent_times(self):
        csv = csv_controller.CsvController()
        question = roboter_question.QuestionRoboter()
        csv.read_csv()

        question.question_name()

        name = input('name:')

        question.proposal_restaurant(csv.restaurant_list)

        question.queston_restaurant(name)

        restaurant = input('restaurant-name:')
        count = 1

        csv.add_csv(restaurant, count, csv.restaurant_list)

        print('{}. Thank you.'.format(name))
        print('Have a good day! See you.')