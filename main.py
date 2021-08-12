import pygame
import time
import math
from detector import *
from settings import *
from pictures import *
from npc import *
from backpack import *
from wall import *
from start_menu import *
from area import *
WIN_WIDTH = 500
WIN_HEIGHT = 500
FPS = 80

# initialize
pygame.init()
pygame.mixer.init()
# clock
clock = pygame.time.Clock()

# set the title
pygame.display.set_caption("Walk")

# set the window
window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))

bg_images = pygame.transform.scale(
    pygame.image.load("images/hospital_new.png"), (2208, 1426))
fg_images = figure_1
menu_images = pygame.transform.scale(pygame.image.load(os.path.join("images", "start_menu.png")),
                                     (WIN_WIDTH, WIN_HEIGHT))
sound_images = pygame.transform.scale(pygame.image.load(os.path.join("images", "sound.png")),
                                      (60, 60))
muse_images = pygame.transform.scale(pygame.image.load(os.path.join("images", "muse.png")),
                                     (60, 60))


class Game:
    def __init__(self):
        self.figure = Figure()
        self.next_frame = Figure.clock()
        self.frame = 0
        self.open_npc = False
        self.open_props = False
        self.open_bp = 0
        self.NPC = NPC_Group()
        self.PROPS = PROPS_Group()
        self.backpack = Backpack()
        self.menu = menu_images
        self.counter = 0
        # touch botton
        self.start_btn = Buttons(150, 225, 200, 60)
        self.sound_btn = Buttons(360, 10, 60, 60)
        self.mute_btn = Buttons(430, 10, 60, 60)
        self.buttons = [self.start_btn, self.sound_btn, self.mute_btn]
        # opening music
        self.openings = pygame.mixer.Sound("./music/opening.wav")
        self.start = pygame.mixer.Sound("./music/start_sound.wav")
        pass

    def play_music(self):
        pygame.mixer.music.load("./music/opening.wav")
        pygame.mixer.music.set_volume(0.2)
        pygame.mixer.music.play(-1)
        self.openings.set_volume(0.2)

    def game_run(self):
        global bg_x, bg_y, fg_images
        # 中心位置
        centerx, centery = (WIN_WIDTH / 2, WIN_HEIGHT / 2)
        # opening music
        self.play_music()
        window.blit(self.menu, (bg_x, bg_y))

        run = True
        while run:
            clock.tick(FPS)
            if self.counter == 0:
                self.buttons = [self.start_btn, self.sound_btn, self.mute_btn]
                window.blit(self.menu, (bg_x, bg_y))
                window.blit(sound_images, (360, 10))
                window.blit(muse_images, (430, 10))
            else:
                self.buttons = [self.sound_btn, self.mute_btn]
                window.blit(bg_images, (bg_x, bg_y))
                window.blit(fg_images, (250 - PLAYER_WIDTH /
                                        2, 250 - PLAYER_HEIGHT / 2))
                self.NPC.draw_NPC(bg_images)
                self.PROPS.draw_PROPS(bg_images)
                window.blit(sound_images, (360, 10))
                window.blit(muse_images, (430, 10))

            x, y = pygame.mouse.get_pos()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    # check if hit start btn
                    if self.start_btn.clicked(x, y):
                        self.counter += 1
                        self.start.play()
                    if self.sound_btn.clicked(x, y):
                        pygame.mixer.music.unpause()
                    if self.mute_btn.clicked(x, y):
                        pygame.mixer.music.pause()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.open_npc = self.NPC.open_dialog()
                        self.open_props = self.PROPS.open_dialog()
                        self.backpack.add_props()
                    if event.key == pygame.K_b:
                        self.open_bp += 1
                    if event.key == pygame.K_y and self.open_npc == True:
                        self.NPC.open_pick_money()
                        self.NPC.open_shooting_game()

                        pass
                    if event.key == pygame.K_n:
                        self.open_npc = self.NPC.open_dialog()

            for btn in self.buttons:  # 用for檢查每一個按鈕是否有按到~
                btn.create_frame(x, y)  # 利用已經創造了功能畫出邊框(創造邊框)
                btn.draw_frame(window)  # 利用已經創造了功能畫出邊框(劃出邊框)

            if self.open_npc == True:
                self.NPC.draw_dialog(window)
                self.NPC.dialog_sentence(window)

            if self.open_props == True:
                self.PROPS.draw_dialog(window)
                self.PROPS.dialog_sentence(window)

            if self.open_bp % 2 == 1:
                self.backpack.draw(window)

            if self.open_npc == False and self.open_props == False and self.open_bp % 2 == 0 and self.NPC.enemy_task == False:
                if Figure.clock() > self.next_frame:
                    self.frame = (self.frame + 1) % 8
                    self.next_frame += 100

                if keyPressed("right"):
                    fg_images = figure[0 * 8 + self.frame]
                    if Wall(centerx, centery).iscollide_right() == -1 and self.counter != 0:
                        bg_x -= 5
                        self.NPC.pos_change_x -= 5
                        self.PROPS.pos_change_x -= 5
                        centerx += 5

                if keyPressed("left"):
                    fg_images = figure[1 * 8 + self.frame]
                    if Wall(centerx, centery).iscollide_left() == -1 and self.counter != 0:
                        bg_x += 5
                        self.NPC.pos_change_x += 5
                        self.PROPS.pos_change_x += 5
                        centerx -= 5

                if keyPressed("up") and Wall(centerx, centery).iscollide_up() == -1 and self.counter != 0:
                    bg_y += 5
                    self.NPC.pos_change_y += 5
                    self.PROPS.pos_change_y += 5
                    centery -= 5
                elif keyPressed("up"):
                    pass

                if keyPressed("down") and Wall(centerx, centery).iscollide_down() == -1 and self.counter != 0:
                    bg_y -= 5
                    self.NPC.pos_change_y -= 5
                    self.PROPS.pos_change_y -= 5
                    centery += 5
                elif keyPressed("down"):
                    pass

            if self.open_npc == False and self.NPC.enemy_task == True:
                window.blit(game_over_image, (60, 60))
                self.NPC.game_over = True

            self.PROPS.alcohol_start = self.NPC.doctor_start
            self.PROPS.rapidtest_start = self.NPC.nurse_start
            self.NPC.doctor_task = self.PROPS.alcohol_picked
            self.NPC.nurse_task = self.PROPS.rapidtest_picked

            self.NPC.update()
            self.PROPS.update()

            # self.area1=pygame.Rect(340,220,230,480)
            #pygame.draw.rect(bg_images, (255,255,255), self.area1, 0)
            # self.area2=pygame.Rect(570,220,800,470)
            #pygame.draw.rect(bg_images, (0,0,0), self.area2, 0)

            # 偵測background邊界
            Detector(bg_images, bg_x, bg_y, WIN_WIDTH, WIN_HEIGHT).detect()

            Area(centerx, centery, window).in_this_area()

            pygame.display.update()
        pygame.quit()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    test_RPG = Game()
    test_RPG.game_run()
