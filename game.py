from config import loop, seconds
from ball import *
from players import *

# Controls time of power ups

def timer():
    global loop, seconds, p1_active_1, p2_active_1, p1_active_time_1, p2_active_time_1

    # Counting seconds every 60 game loop interactions
    loop = loop + 1

    # Print can be enabled to check the seconds increasing up to 60
    # print(loop)
    if loop == 60:
        loop = 0
        seconds = seconds + 1

    # Checking if Any powerup is active and counting the time it remains active

        if p1_active_1 == True:
            p1_active_time_1 = p1_active_time_1 + 1

        if p2_active_1 == True:
            p2_active_time_1 = p2_active_time_1 + 1

    # Seconds have relation with the powerup released by the bricks also the total power ups

    if seconds == 5:
        seconds = 0

    # Checking if the Powerup is at time limit

    if p1_active_1 == True or p2_active_1 == True:
        if p1_active_time_1 == 15:
            p1_active_time_1 == 0
            p1_active_1 == False

        if p2_active_time_1 == 15:
            p2_active_time_1 == 0
            p2_active_1 == False


# Increase the size of the player paddle
def power_up_1():
    global p1_active_1, p2_active_1, paddle_1_height, paddle_2_height

    if p1_active_1 == True:
        paddle_1_height = 130
    if p2_active_1 == True:
        paddle_2_height = 130

    if p1_active_1 == False:
        paddle_1_height = 75
    if p2_active_1 == False:
        paddle_2_height = 75
