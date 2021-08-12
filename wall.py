import pygame
import math



class Wall():
    """boundary of map"""
    def __init__(self, centerx, centery):
        #中心點
        self.rect0=pygame.Rect(centerx, centery, 50, 60)
        #左牆
        self.wall_L1=pygame.Rect(340, 220, 10, 500)
        self.wall_L2=pygame.Rect(570, 480, 10, 500)
        self.wall_L3=pygame.Rect(570, 220, 10, 100)
        self.wall_L4=pygame.Rect(810, 220, 10, 100)
        self.wall_L5=pygame.Rect(810, 450, 10, 30)
        self.wall_L6=pygame.Rect(810, 600, 10, 700)
        self.wall_L7=pygame.Rect(1280, 680, 10, 550)
        self.wall_L8=pygame.Rect(1400, 220, 10, 350)
        self.wall_L9=pygame.Rect(1640, 220, 10, 350)
        self.wall_L10=pygame.Rect(670, 680, 10, 20)
        self.wall_L11=pygame.Rect(1140, 680, 10, 20)
        self.wall_L12=pygame.Rect(1730, 690, 10, 550)
        self.wall_L13=pygame.Rect(1860, 220, 10, 550)
        self.wall_LEFT=[self.wall_L1, self.wall_L2, self.wall_L3, 
                        self.wall_L4, self.wall_L5, self.wall_L6,
                        self.wall_L7, self.wall_L8, self.wall_L9,
                        self.wall_L10, self.wall_L11, self.wall_L12
                        ,self.wall_L13]
        #右牆
        self.wall_R1=pygame.Rect(330, 220, 10, 160)
        self.wall_R2=pygame.Rect(330, 560, 10, 140)
        self.wall_R3=pygame.Rect(560, 480, 10, 500)
        self.wall_R4=pygame.Rect(560, 220, 10, 100)
        self.wall_R5=pygame.Rect(800, 220, 10, 100)
        self.wall_R6=pygame.Rect(800, 450, 10, 30)
        self.wall_R7=pygame.Rect(800, 600, 10, 700)
        self.wall_R8=pygame.Rect(1270, 680, 10, 550)
        self.wall_R9=pygame.Rect(1390, 220, 10, 350)
        self.wall_R10=pygame.Rect(1630, 220, 10, 350)
        self.wall_R11=pygame.Rect(1720, 690, 10, 550)
        self.wall_R12=pygame.Rect(1850, 220, 10, 550)
        self.wall_R13=pygame.Rect(1390, 680, 10, 20)
        self.wall_RIGHT=[self.wall_R1, self.wall_R2, self.wall_R3, 
                         self.wall_R4, self.wall_R5, self.wall_R6,
                         self.wall_R7, self.wall_R8, self.wall_R9,
                         self.wall_R10, self.wall_R11, self.wall_R12,
                         self.wall_R13]
        #上牆
        self.wall_U1=pygame.Rect(340, 220, 1550, 10)
        self.wall_U2=pygame.Rect(340, 690, 340, 10)
        self.wall_U3=pygame.Rect(810, 690, 340, 10)
        self.wall_U4=pygame.Rect(1390, 690, 500, 10)
        self.wall_U5=pygame.Rect(560, 320, 20, 10)
        self.wall_U6=pygame.Rect(800, 320, 20, 10)
        self.wall_U7=pygame.Rect(800, 470, 20, 10)
        self.wall_U8=pygame.Rect(1390, 570, 20, 10)
        self.wall_U9=pygame.Rect(1630, 570, 20, 10)
        self.wall_U10=pygame.Rect(560, 940, 250, 10)
        self.wall_U11=pygame.Rect(800, 1180, 1000, 10)
        self.wall_UP=[self.wall_U1, self.wall_U2, self.wall_U3, 
                      self.wall_U4, self.wall_U5, self.wall_U6,
                      self.wall_U7, self.wall_U8, self.wall_U9,
                      self.wall_U10, self.wall_U11]
        #下牆
        self.wall_D1=pygame.Rect(340, 680, 340, 10)
        self.wall_D2=pygame.Rect(810, 680, 340, 10)
        self.wall_D3=pygame.Rect(1270, 680, 20, 10)
        self.wall_D4=pygame.Rect(1390, 680, 500, 10)
        self.wall_D5=pygame.Rect(560, 930, 250, 10)
        self.wall_D6=pygame.Rect(800, 1170, 1000, 10)
        self.wall_D7=pygame.Rect(560, 470, 20, 10)
        self.wall_D8=pygame.Rect(800, 450, 20, 10)
        self.wall_D9=pygame.Rect(800, 600, 20, 10)
        self.wall_D10=pygame.Rect(330, 210, 1550, 10)
        self.wall_DOWN=[self.wall_D1, self.wall_D2, self.wall_D3, 
                        self.wall_D4, self.wall_D5, self.wall_D6,
                        self.wall_D7, self.wall_D8, self.wall_D9,
                        self.wall_D10]
    def iscollide_left(self):
        return pygame.Rect.collidelist(self.rect0, self.wall_LEFT) 
    
    def iscollide_right(self):
        return pygame.Rect.collidelist(self.rect0, self.wall_RIGHT)
    
    def iscollide_up(self):
        return pygame.Rect.collidelist(self.rect0, self.wall_UP)
    
    def iscollide_down(self):
        return pygame.Rect.collidelist(self.rect0, self.wall_DOWN)
    
    
"""
if you want to see frame, copy this to main:

                self.wall_L1=pygame.Rect(340, 220, 10, 500)
                self.wall_L2=pygame.Rect(570, 480, 10, 500)
                self.wall_L3=pygame.Rect(570, 220, 10, 100)
                self.wall_L4=pygame.Rect(810, 220, 10, 100)
                self.wall_L5=pygame.Rect(810, 450, 10, 30)
                self.wall_L6=pygame.Rect(810, 600, 10, 700)
                self.wall_L7=pygame.Rect(1280, 680, 10, 550)
                self.wall_L8=pygame.Rect(1400, 220, 10, 350)
                self.wall_L9=pygame.Rect(1640, 220, 10, 350)
                self.wall_L10=pygame.Rect(670, 680, 10, 20)
                self.wall_L11=pygame.Rect(1140, 680, 10, 20)
                self.wall_L12=pygame.Rect(1730, 690, 10, 550)
                self.wall_L13=pygame.Rect(1860, 220, 10, 550)

                self.wall_R1=pygame.Rect(330, 220, 10, 160)
                self.wall_R2=pygame.Rect(330, 560, 10, 140)
                self.wall_R3=pygame.Rect(560, 480, 10, 500)
                self.wall_R4=pygame.Rect(560, 220, 10, 100)
                self.wall_R5=pygame.Rect(800, 220, 10, 100)
                self.wall_R6=pygame.Rect(800, 450, 10, 30)
                self.wall_R7=pygame.Rect(800, 600, 10, 700)
                self.wall_R8=pygame.Rect(1270, 680, 10, 550)
                self.wall_R9=pygame.Rect(1390, 220, 10, 350)
                self.wall_R10=pygame.Rect(1630, 220, 10, 350)
                self.wall_R11=pygame.Rect(1720, 690, 10, 550)
                self.wall_R12=pygame.Rect(1850, 220, 10, 550)
                self.wall_R13=pygame.Rect(1390, 680, 10, 20)

                self.wall_U1=pygame.Rect(340, 220, 1550, 10)
                self.wall_U2=pygame.Rect(340, 690, 340, 10)
                self.wall_U3=pygame.Rect(810, 690, 340, 10)
                self.wall_U4=pygame.Rect(1390, 690, 500, 10)
                self.wall_U5=pygame.Rect(560, 320, 20, 10)
                self.wall_U6=pygame.Rect(800, 320, 20, 10)
                self.wall_U7=pygame.Rect(800, 470, 20, 10)
                self.wall_U8=pygame.Rect(1390, 570, 20, 10)
                self.wall_U9=pygame.Rect(1630, 570, 20, 10)
                self.wall_U10=pygame.Rect(560, 940, 250, 10)
                self.wall_U11=pygame.Rect(800, 1180, 1000, 10)

                self.wall_D1=pygame.Rect(340, 680, 340, 10)
                self.wall_D2=pygame.Rect(810, 680, 340, 10)
                self.wall_D3=pygame.Rect(1270, 680, 20, 10)
                self.wall_D4=pygame.Rect(1390, 680, 500, 10)
                self.wall_D5=pygame.Rect(560, 930, 250, 10)
                self.wall_D6=pygame.Rect(800, 1170, 1000, 10)
                self.wall_D7=pygame.Rect(560, 470, 20, 10)
                self.wall_D8=pygame.Rect(800, 450, 20, 10)
                self.wall_D9=pygame.Rect(800, 600, 20, 10)
                self.wall_D10=pygame.Rect(330, 210, 1550, 10)

                self.rect0=pygame.Rect(centerx, centery, 50, 60)
                pygame.draw.rect(bg_images, (255, 255, 255), self.wall_L1, 0)
                pygame.draw.rect(bg_images, (255, 255, 255), self.wall_L2, 0)
                pygame.draw.rect(bg_images, (255, 255, 255), self.wall_L3, 0)    
                pygame.draw.rect(bg_images, (255, 255, 255), self.wall_L4, 0)
                pygame.draw.rect(bg_images, (255, 255, 255), self.wall_L5, 0)
                pygame.draw.rect(bg_images, (255, 255, 255), self.wall_L6, 0)
                pygame.draw.rect(bg_images, (255, 255, 255), self.wall_L7, 0)
                pygame.draw.rect(bg_images, (255, 255, 255), self.wall_L8, 0)
                pygame.draw.rect(bg_images, (255, 255, 255), self.wall_L9, 0)
                pygame.draw.rect(bg_images, (255, 255, 255), self.wall_L10, 0)
                pygame.draw.rect(bg_images, (255, 255, 255), self.wall_L11, 0) 
                pygame.draw.rect(bg_images, (255, 255, 255), self.wall_L12, 0)
                pygame.draw.rect(bg_images, (255, 255, 255), self.wall_L13, 0)

                pygame.draw.rect(bg_images, (0, 0, 0), self.wall_R1, 0)
                pygame.draw.rect(bg_images, (0, 0, 0), self.wall_R2, 0)
                pygame.draw.rect(bg_images, (0, 0, 0), self.wall_R3, 0)
                pygame.draw.rect(bg_images, (0, 0, 0), self.wall_R4, 0)
                pygame.draw.rect(bg_images, (0, 0, 0), self.wall_R5, 0)
                pygame.draw.rect(bg_images, (0, 0, 0), self.wall_R6, 0)
                pygame.draw.rect(bg_images, (0, 0, 0), self.wall_R7, 0)
                pygame.draw.rect(bg_images, (0, 0, 0), self.wall_R8, 0)
                pygame.draw.rect(bg_images, (0, 0, 0), self.wall_R9, 0)
                pygame.draw.rect(bg_images, (0, 0, 0), self.wall_R10, 0)
                pygame.draw.rect(bg_images, (0, 0, 0), self.wall_R11, 0)
                pygame.draw.rect(bg_images, (0, 0, 0), self.wall_R12, 0)
                pygame.draw.rect(bg_images, (0, 0, 0), self.wall_R13, 0)

                pygame.draw.rect(bg_images, (255, 0, 0), self.wall_U1, 0)
                pygame.draw.rect(bg_images, (255, 0, 0), self.wall_U2, 0)
                pygame.draw.rect(bg_images, (255, 0, 0), self.wall_U3, 0)
                pygame.draw.rect(bg_images, (255, 0, 0), self.wall_U4, 0)
                pygame.draw.rect(bg_images, (255, 0, 0), self.wall_U5, 0)
                pygame.draw.rect(bg_images, (255, 0, 0), self.wall_U6, 0)
                pygame.draw.rect(bg_images, (255, 0, 0), self.wall_U7, 0)
                pygame.draw.rect(bg_images, (255, 0, 0), self.wall_U8, 0)
                pygame.draw.rect(bg_images, (255, 0, 0), self.wall_U9, 0)
                pygame.draw.rect(bg_images, (255, 0, 0), self.wall_U10, 0)
                pygame.draw.rect(bg_images, (255, 0, 0), self.wall_U11, 0)

                pygame.draw.rect(bg_images, (0, 255, 0), self.wall_D1, 0)
                pygame.draw.rect(bg_images, (0, 255, 0), self.wall_D2, 0)
                pygame.draw.rect(bg_images, (0, 255, 0), self.wall_D3, 0)
                pygame.draw.rect(bg_images, (0, 255, 0), self.wall_D4, 0)
                pygame.draw.rect(bg_images, (0, 255, 0), self.wall_D5, 0)
                pygame.draw.rect(bg_images, (0, 255, 0), self.wall_D6, 0)
                pygame.draw.rect(bg_images, (0, 255, 0), self.wall_D7, 0)
                pygame.draw.rect(bg_images, (0, 255, 0), self.wall_D8, 0)
                pygame.draw.rect(bg_images, (0, 255, 0), self.wall_D9, 0)
                pygame.draw.rect(bg_images, (0, 255, 0), self.wall_D10, 0)
                pygame.draw.rect(bg_images, (0, 0, 0), self.wall_R12, 0)
                pygame.draw.rect(bg_images, (0, 0, 0), self.wall_R13, 0)
"""