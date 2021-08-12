import pygame
import math
import os
from pictures import *

# 基本參數設定
bg_x = 0  # 背景圖座標
bg_y = 0
WIN_WIDTH = 500  # 視窗大小
WIN_HEIGHT = 500
WHITE = (255, 255, 255)

# NPC talk sentence
talk_sentense = ["Hi!", "I am Doctor Huang.", "Nice to meet you~", "Can you help me find alcohol?",
                 "It is in Lobby. Try to find it.", "Thanks! Try to talk to others. Good luck."]
talk_sentense_2 = ["hello!", "I'm Nurse Chen.",
                   "I can't find rapid test. Can you help me?", "Maybe you can find it in Door.", "You did a good job!"]
talk_sentense_3 = ["I'm Mario.", "Achieve this challenge then find Enemy.",
                   "Enter (Y) to start game, or (N) to leave.", "Great! Try to find Enemy."]
talk_sentense_4 = ["Hey!", "I'm Enemy Jack.", "Do you want to play a game with me?",
                   "Enter (Y) to start, or enter (N) to leave.", "Excellent! Try talk to others."]

# PROPS talk sentence
alcohol_sentence = ["You get a alcohol.", "Please check your backpack."]
rapid_test_sentence = ["You get a rapid test.", "Please check your backpack."]

# 按鍵設定
keydict = {"up": pygame.K_UP, "down": pygame.K_DOWN,
           "left": pygame.K_LEFT, "right": pygame.K_RIGHT}


def keyPressed(keyCheck=""):
    global keydict
    keys = pygame.key.get_pressed()
    if sum(keys) > 0:
        if keyCheck == "" or keys[keydict[keyCheck.lower()]]:
            return True
    return False


class Figure:
    def __init__(self):
        pass

    def clock():
        current_time = pygame.time.get_ticks()
        return current_time
