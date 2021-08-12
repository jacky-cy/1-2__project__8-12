import pygame
import math
import os
from settings import *

props_picked = None

class PROPS:
    def __init__(self, image, name, x, y, pos_change_x, pos_change_y):
        self.image = image
        self.name = name
        self.rect = self.image.get_rect()
        self.rect.center = (x + pos_change_x, y + pos_change_y)
        self.words = talk_sentense
        self.x = x
        self.y = y
        self.range = 100
        pass

    def draw(self, win):
        win.blit(self.image , (self.x, self.y))

    def distance(self):
        props_x, props_y = self.rect.center
        player_x = WIN_WIDTH/2 - PLAYER_WIDTH/2
        player_y = WIN_HEIGHT/2 - PLAYER_HEIGHT/2
        distance = math.sqrt((props_x-player_x)**2+(props_y-player_y)**2)
        if distance <= self.range:
            return True
        else:
            return False

    @classmethod
    def Alcohol(cls, x, y, pos_change_x, pos_change_y):
        al = cls(alcohol_image, "Alcohol", x, y, pos_change_x, pos_change_y)
        al.words = alcohol_sentence
        return al

    @classmethod
    def RapidTest(cls, x, y, pos_change_x, pos_change_y):
        rt = cls(rapid_test_image, "Rapid Test", x, y, pos_change_x, pos_change_y)
        rt.words = rapid_test_sentence
        return rt


class PROPS_Group:
    def __init__(self):
        self.pos_change_x = 0
        self.pos_change_y = 0
        self.props_list = []
        self.selected = None
        self.picked = False
        self.alcohol_picked = False
        self.rapidtest_picked = False
        self.alcohol_start = False
        self.rapidtest_start = False
        self.start = False
        self.sentence = 0
        pass

    def update(self):
        global props_picked
        if self.start == True:
            props_picked = self.selected
        self.props_list = [PROPS.Alcohol(1200, 270, self.pos_change_x, self.pos_change_y),
                           PROPS.RapidTest(430, 580, self.pos_change_x, self.pos_change_y)]

    def is_selected(self):
        for props in self.props_list:
            if props.distance() == True:
                self.selected = props
                return self.selected
        return None

    def which_is_picked(self):
        if self.is_selected()!= None:
            if self.selected.name == "Alcohol":
                self.picked = self.alcohol_picked
                self.start = self.alcohol_start
            elif self.selected.name == "Rapid Test":
                self.picked = self.rapidtest_picked
                self.start = self.rapidtest_start
        else:
            return None

    def open_dialog(self):
        self.which_is_picked()
        if self.is_selected()!= None and self.picked == False and self.start == True:
            if self.sentence < len(self.selected.words)-1:
                self.sentence += 1
                return True
            elif self.sentence == len(self.selected.words)-1:
                self.sentence += 1
                if self.selected.name == "Alcohol":
                    self.alcohol_picked = True
                elif self.selected.name == "Rapid Test":
                    self.rapidtest_picked = True
                return True
            else:
                self.sentence = 0
                return False
        if self.is_selected() != None and self.picked == True:
            if self.sentence == 0:
                self.sentence +=1
                return True
            else:
                self.sentence = 0
                return False
        else:
            return False

    def dialog_sentence(self, win):
        if self.selected != None:
            if self.sentence <= len(self.selected.words) and self.picked == False:
                font = pygame.font.Font(None, 22)
                text_surface = font.render(self.selected.words[self.sentence-1], True, WHITE)
                win.blit(text_surface, (160, 40))
            elif self.picked == True:
                font = pygame.font.Font(None, 22)
                text_surface = font.render("You have picked it.", True, WHITE)
                win.blit(text_surface, (160, 40))

    def draw_dialog(self, win):
        if self.selected != None:
            win.blit(dialog_image, (10, 10))
            win.blit(self.selected.image, (50, 40))
            font = pygame.font.Font(None, 22)
            text_name = font.render(self.selected.name, True, WHITE)
            win.blit(text_name, (60, 127))

    def draw_PROPS(self, win):
        #for props in self.props_list:   #最終版
        #    props.draw(win)
        self.props_list[1].draw(win)


class Backpack:
    def __init__(self):
        self.props_list = []
        self.props_num = 0
        self.props_new = None
        pass

    def add_props(self):
        global props_picked
        if props_picked != None and self.props_list != []:
            repeat = 0
            for i in self.props_list:
                if props_picked.name == i.name:
                    repeat += 1
            if repeat == 0:
                self.props_list.append(props_picked)
                self.props_num += 1
        elif props_picked != None and self.props_list == []:
            self.props_list.append(props_picked)
            self.props_num += 1


    def draw(self, win):
        win.blit(backpack_image, (60, 60))
        if self.props_list != []:
            for i in range(self.props_num):
                if i <= 3:
                    win.blit(self.props_list[i].image, (130 + i * 90, 200))
                else:
                    win.blit(self.props_list[i-3].image, (130 + (i-3) * 90, 290))