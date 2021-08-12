import pygame
import math
import os

#參數設定
PLAYER_WIDTH = 28*3  #玩家圖示大小
PLAYER_HEIGHT = 30*3

#玩家圖示
figure_1 = pygame.transform.scale(pygame.image.load("images/agent1.png"), (PLAYER_WIDTH, PLAYER_HEIGHT))
figure_2 = pygame.transform.scale(pygame.image.load("images/agent2.png"), (PLAYER_WIDTH, PLAYER_HEIGHT))
figure_3 = pygame.transform.scale(pygame.image.load("images/agent3.png"), (PLAYER_WIDTH, PLAYER_HEIGHT))
figure_4 = pygame.transform.scale(pygame.image.load("images/agent4.png"), (PLAYER_WIDTH, PLAYER_HEIGHT))
figure_5 = pygame.transform.scale(pygame.image.load("images/agent5.png"), (PLAYER_WIDTH, PLAYER_HEIGHT))
figure_6 = pygame.transform.scale(pygame.image.load("images/agent6.png"), (PLAYER_WIDTH, PLAYER_HEIGHT))
figure_7 = pygame.transform.scale(pygame.image.load("images/agent7.png"), (PLAYER_WIDTH, PLAYER_HEIGHT))
figure_8 = pygame.transform.scale(pygame.image.load("images/agent8.png"), (PLAYER_WIDTH, PLAYER_HEIGHT))
figure_9 = pygame.transform.scale(pygame.image.load("images/agent9.png"), (PLAYER_WIDTH, PLAYER_HEIGHT))
figure_10 = pygame.transform.scale(pygame.image.load("images/agent10.png"), (PLAYER_WIDTH, PLAYER_HEIGHT))
figure_11 = pygame.transform.scale(pygame.image.load("images/agent11.png"), (PLAYER_WIDTH, PLAYER_HEIGHT))
figure_12 = pygame.transform.scale(pygame.image.load("images/agent12.png"), (PLAYER_WIDTH, PLAYER_HEIGHT))
figure_13 = pygame.transform.scale(pygame.image.load("images/agent13.png"), (PLAYER_WIDTH, PLAYER_HEIGHT))
figure_14 = pygame.transform.scale(pygame.image.load("images/agent14.png"), (PLAYER_WIDTH, PLAYER_HEIGHT))
figure_15 = pygame.transform.scale(pygame.image.load("images/agent15.png"), (PLAYER_WIDTH, PLAYER_HEIGHT))
figure_16 = pygame.transform.scale(pygame.image.load("images/agent16.png"), (PLAYER_WIDTH, PLAYER_HEIGHT))

figure = [figure_1, figure_2, figure_3, figure_4, figure_5, figure_6, figure_7, figure_8,
        figure_9, figure_10, figure_11, figure_12, figure_13, figure_14, figure_15, figure_16]
fg_images = figure_1

#NPC picture
doctor_image = pygame.transform.scale(pygame.image.load("images/doctor.png"), (84, 84))
enemy_image = pygame.transform.scale(pygame.image.load("images/enemy.png"), (84, 90))
mario_image = pygame.transform.scale(pygame.image.load("images/mario.png"), (84, 90))

#PROPS pictuse
alcohol_image = pygame.transform.scale(pygame.image.load("images/alcohol.png"), (61, 61))
rapid_test_image = pygame.transform.scale(pygame.image.load("images/rapid_test.png"), (61, 61))

#dialog picture
dialog_image=pygame.transform.scale(pygame.image.load("images/talk_bg.png"),(475,150))

#backpack picture
backpack_image = pygame.transform.scale(pygame.image.load("images/backpack.png"), (380, 380))

#game over picture
game_over_image = pygame.transform.scale(pygame.image.load("images/game_over.jpg"), (380, 380))