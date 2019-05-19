import os

import roboter

def main():
    robot = roboter.Roboter()
    if os.path.exists("ranking.csv") == False:
        robot.say_roboter_first()

    else:
        robot.say_roboter_second_and_subsequent_times()


main()
