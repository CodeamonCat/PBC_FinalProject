import pygame
import os
import tkinter as tk
import tkinter.font as tkFont
WIDTH = 800
HEIGHT = 534
FPS = 10  # 偵數，一個指令0.1秒 ->時間每次加0.1
show_init = True
running = True
runsound_judge = 1

# 遊戲初始化 and 版面設置
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))  # 創建一個幾乘幾的視窗
clock = pygame.time.Clock()  # 因為每個電腦的效能不同造成體驗不同，所以進行降維打擊

# 匯入圖片、音效
background_img = pygame.image.load(
    os.path.join("image", "background.jpg")).convert()
CMKuan = pygame.image.load(os.path.join("image", "管中閔.jpg")).convert()
SMALLCMKuan = pygame.transform.scale(CMKuan, (20, 20))
init_img = pygame.image.load(os.path.join("image", "start.jpg")).convert()

BGM = pygame.mixer.music.load(os.path.join("music", "BGM.wav"))
run_sound = pygame.mixer.Sound(os.path.join("music", "run.wav"))
pygame.mixer.music.set_volume(0.1)  # 調整音量

# 標題
pygame.display.set_caption("112模擬器")
pygame.display.set_icon(SMALLCMKuan)


class Player(pygame.sprite.Sprite):
    def __init__(self):  # 定義各種屬性
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((70, 70))
        self.image = pygame.transform.scale(CMKuan, (70, 70))
        self.rect = self.image.get_rect()  # 把它給定位
        self.rect.x = WIDTH/2
        self.rect.y = HEIGHT/2  # 起始位置
        self.speedx = 5  # 速度
        self.energy = 100  # 管爺能量
        self.tiring = False  # 管爺累不累
        self.time = 300  # 總時間
        self.point = 0

    def update(self):  # 定義各種按鍵的功能
        self.time -= 0.1  # 計時
        key_pressed = pygame.key.get_pressed()
        # 他有一大堆布林值，key_pressed偵測這個按鍵有沒有被按

        # 管爺走路
        if key_pressed[pygame.K_LEFT]:
            self.rect.x -= self.speedx
        if key_pressed[pygame.K_RIGHT]:
            self.rect.x += self.speedx
        if key_pressed[pygame.K_UP]:
            self.rect.y -= self.speedx
        if key_pressed[pygame.K_DOWN]:
            self.rect.y += self.speedx

        # 管爺加速
        if key_pressed[pygame.K_LSHIFT]:
            self.tiring = True
            if self.energy-4 >= 0:
                self.speedx = 10
                self.energy -= 4
            else:
                self.speedx = 5
        if not key_pressed[pygame.K_LSHIFT]:
            self.tiring = False
            self.speedx = 5
            if self.energy < 100:
                self.energy += 2

        # 管爺跳跳
        if key_pressed[pygame.K_SPACE]:
            self.rect.y -= 20
            self.energy -= 7

        # 管爺撞牆
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT


class Question1(tk.Frame):
    def __init__(self):
        self.root = tk.Tk()
        self.root.title('Attempt 1')
        self.createwidget()

    def createwidget(self):
        f1 = tkFont.Font(size=28, family='Arial')
        f2 = tkFont.Font(size=18, family='Arial')
        self.heading = tk.Label(self.root, text='管爺幾月幾號生日？',
                                height=1, width=15, font=f1)
        self.buttomNum1 = tk.Button(
            self.root, text="6/22", command=self.clickbutton1, height=1, width=6, font=f2)
        self.buttomNum2 = tk.Button(
            self.root, text="8/15", command=self.clickbutton2, height=1, width=6, font=f2)
        self.buttomNum3 = tk.Button(
            self.root, text="11/22", command=self.clickbutton3, height=1, width=6, font=f2)
        self.heading.pack()
        self.buttomNum1.pack()
        self.buttomNum2.pack()
        self.buttomNum3.pack()
        self.root.mainloop()

    def clickbutton1(self):
        self.root.destroy()

    def clickbutton2(self):
        player.point += 5
        self.root.destroy()

    def clickbutton3(self):
        self.root.destroy()


def draw_text(surf, text, size, x, y):  # 文字顯示
    font = pygame.font.Font(pygame.font.match_font("arial"), size)  # 名稱大小
    text_surface = font.render(text, True, (255, 255, 255))  # 渲染顏色
    text_rect = text_surface.get_rect()  # 定位
    text_rect.centerx, text_rect.top = x, y
    surf.blit(text_surface, text_rect)


def draw_init():  # 設定初始化界面
    screen.blit(init_img, (0, 0))
    draw_text(screen, str('A day of CM KUan'), 60, WIDTH/2, HEIGHT/4)
    draw_text(screen, str('Play with CM Kuan and enjoy the game!'),
              30, WIDTH/2, HEIGHT/2)
    draw_text(screen, str('~Press any button to start~'),
              30, WIDTH/2, HEIGHT/1.5)
    pygame.display.update()
    waiting = True
    clock.tick(FPS)  # 一秒鐘之內最多只能執行10次
    # 偵測有沒有鍵盤按鈕被按到
    while waiting:
        for event in pygame.event.get():  # 取得鍵盤的所有輸入
            if event.type == pygame.QUIT:  # 離開
                pygame.quit()
                return True
            elif event.type == pygame.KEYUP:
                # 按下任何按鍵(KEYDOWN:按下去直接開始，KEYUP:鬆開才開始)
                waiting = False
                return False


# 物件設定
all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)
pygame.mixer.music.play(-1)
run_sound.play()

Q1check = False
while running:
    clock.tick(FPS)  # 一秒鐘之內最多只能執行10次
    # 初始化界面
    if show_init:
        run_sound.stop()
        close = draw_init()
        if close:
            break
        show_init = False

    # 播放喘氣聲
    if not player.tiring:
        runsound_judge = 0
        run_sound.stop()
    else:
        runsound_judge += 1
        if runsound_judge == 1:
            run_sound.play()

    if not Q1check:
        if player.rect.x == WIDTH/2-20:
            run_sound.stop()
            Q1check = True
            Question1()

    # 取得輸入
    for event in pygame.event.get():  # 取得輸入，把他得到的動作並成為一個list
        if event.type == pygame.QUIT:  # 沒有函數的離開(?)
            running = False

    # 更新遊戲
    all_sprites.update()

    # 畫面顯示
    screen.blit(background_img, (0, 0))  # 改成了圖片
    all_sprites.draw(screen)
    draw_text(screen, str(player.energy), 30, WIDTH/2, 12)
    draw_text(screen, str("ENERGY:"), 30, WIDTH/2-80, 12)
    draw_text(screen, str(int(player.time)), 30, WIDTH/2, 50)
    draw_text(screen, str("TIME:"), 30, WIDTH/2-80, 50)
    draw_text(screen, str("POINT:"), 30, WIDTH/2-80, 100)
    draw_text(screen, str(player.point), 30, WIDTH/2, 100)
    pygame.display.update()  # 更新
pygame.quit()  # 離開
