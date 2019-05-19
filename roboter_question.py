class QuestionRoboter():
    def question_name(self):
        print("Hello! I'm Roboter. What is your name?")

    def queston_restaurant(self, name):
        print('{}. Which restaurant do you like?'.format(name))

    def proposal_restaurant(self, restaurant_list):
        for i in range(1,len(restaurant_list)):
            print('My favorite restaurant is {}'.format(restaurant_list[i].get_restaurant()))
            print('Do you like this restaurant? [yes/no]')
            answer = input()
            if answer == 'yes':
                break
