class QuestionRoboter():
    def question_name(self):
        print("Hello! I'm Roboter. What is your name?")

    def queston_restaurant(self, name):
        print('{}. Which restaurant do you like?'.format(name))

    def proposal_restaurant(self, restaurant_list):
        restaurant_ranking_list = []
        for i in range(1,len(restaurant_list)):
            key = restaurant_list[i].get_restaurant()
            value = restaurant_list[i].get_count()
            ls = [key, value]
            restaurant_ranking_list.append(ls)

        restaurant_ranking_list.sort(key=lambda x: x[1], reverse=True)

        for i in range(len(restaurant_ranking_list)):
            print('My favorite restaurant is {}'.format(restaurant_ranking_list[i][0]))
            print('Do you like this restaurant? [yes/no]')
            answer = input()
            if answer.lower() == 'yes' or answer.lower() == 'y':
                break