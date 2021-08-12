#!/usr/bin/env python
# coding: utf-8

# In[ ]:

import pygame

class Area():
    """area of map"""
    def __init__(self, centerx, centery, win):
        #中心點
        self.rect0=pygame.Rect(centerx, centery, 50, 60)
        self.win=win
        
        self.area1=pygame.Rect(340,220,230,480)
        self.area2=pygame.Rect(570,220,800,470)
        
    def in_this_area(self):
        Pink=(255, 192, 203)
        
        
        font = pygame.font.Font(None,48)
        #render方法返回Surface物件
        text = font.render('Door',True,(255,255,255),Pink)
        
        textRect = text.get_rect()
        textRect.center=(100,470)
        
        
        
        
        if pygame.Rect.contains(self.area1, self.rect0):
            
            self.win.blit(text, textRect)
        elif pygame.Rect.contains(self.area2, self.rect0):
            text = font.render('Lobby',True,(255,255,255),Pink)
            self.win.blit(text, textRect)
        else:
            None