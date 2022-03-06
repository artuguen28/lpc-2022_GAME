from players import *
from ball import *
from config import *


# Controls time of power ups
def timer():
    global loop, seconds

    # Print can be enabled to check the seconds increasing up to 60
    # print(loop)
    if loop == 60:
        loop = 0
        seconds = seconds + 1

    # Seconds have relation with the powerup released by the bricks also the total power ups

    if seconds == 5:
        seconds = 0

    # Counting seconds every 60 game loop interactions
    loop = loop + 1


# Increase the size of the player paddle
def power_up_1():
    global loop, p1_active_1, p2_active_1, p1_active_time_1,\
        p2_active_time_1, paddle_1_height, paddle_2_height

    # Checking if powerup is at time limit

    if p1_active_1 is True or p2_active_1 is True:
        if p1_active_time_1 == 15:
            p1_active_time_1 = 0
            p1_active_1 = False

        if p2_active_time_1 == 15:
            p2_active_time_1 = 0
            p2_active_1 = False

    # Checking if Any powerup is active and counting the time it remains active
    if loop == 60:
        if p1_active_1 is True:
            p1_active_time_1 = p1_active_time_1 + 1

        if p2_active_1 is True:
            p2_active_time_1 = p2_active_time_1 + 1

    if p1_active_1 is False:
        paddle_1_height = 75
    if p2_active_1 is False:
        paddle_2_height = 75

    if p1_active_1 is True:
        paddle_1_height = 130
    if p2_active_1 is True:
        paddle_2_height = 130


# Makes enemy ball invisible (black)
def power_up_2():
    global loop, ball_1, ball_2, p1_active_2, p2_active_2,\
        p1_active_time_2, p2_active_time_2

    if p1_active_2 is True or p2_active_2 is True:
        if p1_active_time_2 == 7:
            p1_active_time_2 = 0
            p1_active_2 = False

        if p2_active_time_2 == 7:
            p2_active_time_2 = 0
            p2_active_2 = False

    if loop == 60:
        if p1_active_2 is True:
            p1_active_time_2 = p1_active_time_2 + 1

        if p2_active_2 is True:
            p2_active_time_2 = p2_active_time_2 + 1

    if p1_active_2 is True:
        ball_2 = Ball_2(colors["Black"], 14, 14)
    else:
        ball_2 = Ball_2(colors["Red_ball"], 14, 14)
    if p2_active_2 is True:
        ball_1 = Ball_1(colors["Black"], 14, 14)
    else:
        ball_1 = Ball_1(colors["Blue_ball"], 14, 14)


# Makes enemy paddle slower
def power_up_3():
    global loop, paddle_1_speed, paddle_2_speed, p1_active_3,\
        p2_active_3, p1_active_time_3, p2_active_time_3

    if p1_active_3 is True or p2_active_3 is True:
        if p1_active_time_3 == 10:
            p1_active_time_3 = 0
            p1_active_3 = False

        if p2_active_time_3 == 10:
            p2_active_time_3 = 0
            p2_active_3 = False

    if loop == 60:
        if p1_active_3 is True:
            p1_active_time_3 = p1_active_time_3 + 1

        if p2_active_3 is True:
            p2_active_time_3 = p2_active_time_3 + 1

    if p1_active_3 is True:
        paddle_2_speed = 5
    else:
        paddle_2_speed = 10
    if p2_active_3 is True:
        paddle_1_speed = 5
    else:
        paddle_1_speed = 10
