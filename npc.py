import pygame
import math
import os
from settings import *
from backpack import *
import sys
import os

# current_path = os.path.dirname(os.path.abspath(__file__))
# sys.path.append(os.path.join(current_path, "shooting"))
# sys.path.append(os.path.join(current_path + '/shooting', 'img'))


class NPC:
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
        win.blit(self.image, (self.x, self.y))

    def distance(self):
        npc_x, npc_y = self.rect.center
        player_x = WIN_WIDTH / 2 - PLAYER_WIDTH / 2
        player_y = WIN_HEIGHT / 2 - PLAYER_HEIGHT / 2
        distance = math.sqrt((npc_x - player_x)**2 + (npc_y - player_y)**2)
        if distance <= self.range:
            return True
        else:
            return False

    @classmethod
    def Doctor(cls, x, y, pos_change_x, pos_change_y):
        dt = cls(doctor_image, "Doctor", x, y, pos_change_x, pos_change_y)
        dt.words = talk_sentense
        return dt

    @classmethod
    def Nurse(cls, x, y, pos_change_x, pos_change_y):
        nur = cls(figure_1, "Nurse", x, y, pos_change_x, pos_change_y)
        nur.words = talk_sentense_2
        return nur

    @classmethod
    def Mario(cls, x, y, pos_change_x, pos_change_y):
        ma = cls(mario_image, "Mario", x, y, pos_change_x, pos_change_y)
        ma.words = talk_sentense_3
        return ma

    @classmethod
    def Enemy(cls, x, y, pos_change_x, pos_change_y):
        en = cls(enemy_image, "Enemy", x, y, pos_change_x, pos_change_y)
        en.words = talk_sentense_4
        return en


class NPC_Group:
    def __init__(self):
        self.pos_change_x = 0
        self.pos_change_y = 0
        self.npc_list = []
        self.selected = None
        self.selected_task = False
        self.doctor_task = False
        self.nurse_task = False
        self.mario_task = False
        self.enemy_task = False

        self.doctor_start = False  #props can be picked or not
        self.nurse_start = False  #props can be picked or not
        self.enemy_start = False  #final game can start or not

        self.game_over = False
        self.sentence = 0
        pass

    def update(self):
        self.npc_list = [NPC.Doctor(400, 350, self.pos_change_x, self.pos_change_y),
                         NPC.Nurse(1000, 570, self.pos_change_x, self.pos_change_y),
                         NPC.Enemy(850, 750, self.pos_change_x, self.pos_change_y),
                         NPC.Mario(1600, 750, self.pos_change_x, self.pos_change_y)]

    def is_selected(self):
        for npc in self.npc_list:
            if npc.distance() == True:
                self.selected = npc
                return self.selected
        return None

    def which_is_selected(self):
        if self.is_selected() != None:
            if self.selected.name == "Doctor":
                self.selected_task = self.doctor_task
                self.doctor_start = True
            elif self.selected.name == "Nurse":
                self.selected_task = self.nurse_task
                self.nurse_start = True
            elif self.selected.name == "Mario":
                self.selected_task = self.mario_task
            elif self.selected.name == "Enemy":
                self.selected_task = self.enemy_task
                if self.doctor_task == True and self.nurse_task == True and self.mario_task == True:
                    self.enemy_start = True

    def open_dialog(self):
        print(self.enemy_start)
        self.which_is_selected()
        if self.is_selected() != None and self.game_over == False:
            if self.selected.name == "Enemy" and self.enemy_start == False:
                if self.sentence == 0 and self.selected_task == False:
                    self.sentence += 1
                    return True
                elif self.sentence == 1 and self.selected_task == False:
                    self.sentence = 0
                    return False
            else:
                if self.sentence < len(self.selected.words) - 1 and self.selected_task == False:
                    self.sentence += 1
                    return True
                elif self.selected_task == False:
                    self.sentence = 0
                    return False

                if self.sentence == 0 and self.selected_task == True:
                    self.sentence += 1
                    return True
                elif self.sentence == 1 and self.selected_task == True:
                    self.sentence = 0
                    return False
        else:
            return False

    def open_pick_money(self):
        if self.selected.name == "Enemy" and self.sentence == len(self.selected.words)-1:
            import pick_money
            #print('the game result from pick-money is',
            #       pick_money.end_result)
            if pick_money.end_result == True:
                 self.enemy_task = True
                 self.selected_task = self.enemy_task
                 self.sentence = 1
        pass

    def open_shooting_game(self):
        if self.selected.name == "Mario" and self.sentence == len(self.selected.words) - 1:
            import shooting_game
            #print('the game result from shooting is',
            #      shooting_game.end_result)
            if shooting_game.end_result == True:
                self.mario_task = True
                self.selected_task = self.mario_task
                self.sentence = 1
        pass

    def dialog_sentence(self, win):
        # print(self.sentence)
        if self.selected != None and self.selected_task == False:
            if self.selected.name == "Enemy" and self.enemy_start == False:
                font = pygame.font.Font(None, 22)
                text_surface = font.render(
                    "Please achieve all challenge first.", True, WHITE)
                win.blit(text_surface, (160, 40))
            else:
                if self.sentence < len(self.selected.words):
                    font = pygame.font.Font(None, 22)
                    text_surface = font.render(
                        self.selected.words[self.sentence - 1], True, WHITE)
                    win.blit(text_surface, (160, 40))
        elif self.selected_task == True:
            font = pygame.font.Font(None, 22)
            text_surface = font.render(
                self.selected.words[len(self.selected.words) - 1], True, WHITE)
            win.blit(text_surface, (160, 40))

    def draw_dialog(self, win):
        if self.selected != None:
            win.blit(dialog_image, (10, 10))
            win.blit(self.selected.image, (40, 30))
            font = pygame.font.Font(None, 22)
            text_name = font.render(self.selected.name, True, WHITE)
            win.blit(text_name, (60, 127))

    def draw_NPC(self, win):
        for npc in self.npc_list:
            npc.draw(win)
