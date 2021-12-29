import pygame
import os
import tkinter as tk
from tkinter import messagebox as msg
WIDTH = 401
HEIGHT = 330
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
img1 = pygame.image.load(
    os.path.join("image", "1.png")).convert()
img2 = pygame.image.load(
    os.path.join("image", "2.png")).convert()
img3 = pygame.image.load(
    os.path.join("image", "3.png")).convert()
img4 = pygame.image.load(
    os.path.join("image", "4.png")).convert()
img5 = pygame.image.load(
    os.path.join("image", "5.png")).convert()
img6 = pygame.image.load(
    os.path.join("image", "6.png")).convert()
img7 = pygame.image.load(
    os.path.join("image", "7.png")).convert()
img8 = pygame.image.load(
    os.path.join("image", "8.png")).convert()
img9 = pygame.image.load(
    os.path.join("image", "9.png")).convert()
img10 = pygame.image.load(
    os.path.join("image", "10.png")).convert()
img11 = pygame.image.load(
    os.path.join("image", "11.png")).convert()
img12 = pygame.image.load(
    os.path.join("image", "12.png")).convert()
photolist = [img1, img2, img3, img4, img5,
             img6, img7, img8, img9, img10, img11, img12]
visited = [0]*12
CMKuanL = pygame.image.load(os.path.join("image", "管中閔(左).jpg")).convert()
CMKuanR = pygame.image.load(os.path.join("image", "管中閔(右).jpg")).convert()
CMKuanLT = pygame.image.load(os.path.join("image", "管中閔(左累).jpg")).convert()
CMKuanRT = pygame.image.load(os.path.join("image", "管中閔(右累).jpg")).convert()
SMALLCMKuan = pygame.transform.scale(CMKuanL, (20, 20))
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
        self.image = pygame.transform.scale(CMKuanL, (70, 70))
        self.rect = self.image.get_rect()  # 把它給定位
        self.rect.x = WIDTH/2
        self.rect.y = HEIGHT/2  # 起始位置
        self.speedx = 5  # 速度
        self.energy = 100  # 管爺能量
        self.tiring = False  # 管爺累不累
        self.time = 300  # 總時間
        self.point = 0
        self.nowimage = 'CMKuanL'

    def update(self):  # 定義各種按鍵的功能
        self.time -= 0.1  # 計時
        key_pressed = pygame.key.get_pressed()
        # 他有一大堆布林值，key_pressed偵測這個按鍵有沒有被按

        # 管爺走路
        if key_pressed[pygame.K_LEFT]:
            self.rect.x -= self.speedx
            self.image = pygame.transform.scale(CMKuanL, (70, 70))
            self.nowimage = 'CMKuanL'
        if key_pressed[pygame.K_RIGHT]:
            if key_pressed[pygame.K_LSHIFT]:
                pass
            self.image = pygame.transform.scale(CMKuanR, (70, 70))
            self.nowimage = 'CMKuanR'
            self.rect.x += self.speedx
        if key_pressed[pygame.K_UP]:
            self.rect.y -= self.speedx
        if key_pressed[pygame.K_DOWN]:
            self.rect.y += self.speedx

        # 管爺加速
        if key_pressed[pygame.K_LSHIFT]:
            if self.nowimage == 'CMKuanLT' or self.nowimage == 'CMKuanL':
                self.image = pygame.transform.scale(CMKuanLT, (70, 70))
            if self.nowimage == 'CMKuanRT' or self.nowimage == 'CMKuanR':
                self.image = pygame.transform.scale(CMKuanRT, (70, 70))
            self.tiring = True
            if self.energy-4 >= 0:
                self.speedx = 10
                self.energy -= 4
            else:
                self.speedx = 5
        if not key_pressed[pygame.K_LSHIFT]:
            if self.nowimage == 'CMKuanLT' or self.nowimage == 'CMKuanL':
                self.image = pygame.transform.scale(CMKuanL, (70, 70))
            if self.nowimage == 'CMKuanRT' or self.nowimage == 'CMKuanR':
                self.image = pygame.transform.scale(CMKuanR, (70, 70))
            self.tiring = False
            self.speedx = 5
            if self.energy < 100:
                self.energy += 2
            if self.energy > 100:
                self.energy = 100

        # 管爺撞牆
        if self.rect.right > WIDTH:
            image = rightexceed(self.background)
            self.background = image
        elif self.rect.left < 0:
            image = leftexceed(self.background)
            self.background = image
        elif self.rect.top < 0:
            image = topexceed(self.background)
            self.background = image
        elif self.rect.bottom > HEIGHT:
            image = bottomexceed(self.background)
            self.background = image
        else:
            self.background = self.background


def rightexceed(photo):
    position = photolist.index(photo)
    if position in [0, 1, 3, 4, 6, 7, 9, 10]:
        player.rect.left = 0
        return photolist[position + 1]
    else:
        player.rect.right = WIDTH
        return photo


def leftexceed(photo):
    position = photolist.index(photo)
    if position in [2, 1, 5, 4, 8, 7, 10, 11]:
        player.rect.right = WIDTH
        return photolist[position - 1]
    else:
        player.rect.left = 0
        return photo


def topexceed(photo):
    position = photolist.index(photo)
    if position in [3, 4, 5, 6, 7, 8, 9, 10, 11]:
        player.rect.bottom = HEIGHT
        return photolist[position - 3]
    else:
        player.rect.top = 0
        return photo


def bottomexceed(photo):
    position = photolist.index(photo)
    if position in [0, 1, 2, 3, 4, 5, 6, 7, 8]:
        player.rect.top = 0
        return photolist[position + 3]
    elif position == 9:
        run_sound.stop()
        root = tk.Tk()
        root.withdraw()
        waterbox = msg.askquestion("前往水源", "Are you sure to go to 水源?")
        if waterbox == 'yes':
            player.rect.top = 0
            return img1
        else:
            player.rect.bottom = HEIGHT-10
            return photo
    else:
        player.rect.bottom = HEIGHT
        return photo


all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)


class BuildWindow(tk.Tk):

    def __init__(self, number, Q1, A1, A2, A3, explain,  right_ans, point, A4, HowmanyA):
        self.Q1 = Q1
        self.A1 = A1
        self.A2 = A2
        self.A3 = A3
        self.A4 = A4
        self.point = point
        self.right_ans = right_ans
        self.number = number
        self.explain = explain
        self.HowmanyA = HowmanyA
        self.join = True
        self.createwidget()

    def createwidget(self):
        self.root = tk.Tk()
        self.root.title(self.number)
        self.heading = tk.Label(self.root, text=self.Q1)
        self.buttomNum1 = tk.Button(
            self.root, text=self.A1, command=self.clickbutton1)
        self.buttomNum2 = tk.Button(
            self.root, text=self.A2, command=self.clickbutton2)
        self.buttomNum3 = tk.Button(
            self.root, text=self.A3, command=self.clickbutton3)
        if self.HowmanyA > 3:
            buttomNum4 = tk.Button(
                self.root, text=self.A4, command=self.clickbutton4)

        self.heading.pack()
        self.buttomNum1.pack()
        self.buttomNum2.pack()
        self.buttomNum3.pack()
        if self.HowmanyA > 3:
            buttomNum4.pack()
        self.root.mainloop()

    def clickbutton1(self):
        print("PRESS 1")
        if self.A1 == '進去拉哪次不進去的':
            self.join = True
            self.root.destroy()

        else:
            if self.right_ans == 1:
                player.point += self.point
            msg.showinfo(self.number, self.explain)
            self.root.destroy()

    def clickbutton2(self):
        print("PRESS 2")
        if self.A2 == '先不要啦QQ':
            self.join = False
            self.root.destroy()

        else:
            msg.showinfo(self.number, self.explain)
            if self.right_ans == 2:
                player.point += self.point
            self.root.destroy()

    def clickbutton3(self):
        print("PRESS 3")
        if self.A3 == '讓我再考慮一下><':
            self.join = False
            self.root.destroy()
        else:
            msg.showinfo(self.number, self.explain)
            if self.right_ans == 3:
                player.point += self.point
            self.root.destroy()

    def clickbutton4(self):
        print("PRESS 4")
        msg.showinfo(self.number, self.explain)
        if self.right_ans == 4:
            player.point += self.point
        self.root.destroy()


def draw_text(surf, text, size, x, y):  # 文字顯示
    font = pygame.font.Font(pygame.font.match_font("微軟正黑體"), size)  # 名稱大小
    text_surface = font.render(text, True, (0, 0, 0))  # 渲染顏色
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
                root = tk.Tk()
                root.withdraw()
                exitbox = msg.askquestion("Exit", "Are you sure to exit?")
                if exitbox == "yes":
                    pygame.quit()
                    return True
            elif event.type == pygame.KEYUP:
                # 按下任何按鍵(KEYDOWN:按下去直接開始，KEYUP:鬆開才開始)
                waiting = False
                return False


player.background = img4
pygame.mixer.music.play(-1)
run_sound.play()
while running:
    clock.tick(FPS)  # 一秒鐘之內最多只能執行10次

    if show_init:  # 初始化界面
        run_sound.stop()
        close = draw_init()
        if close:
            break
        show_init = False
        continue

    if not player.tiring:  # 播放喘氣聲
        runsound_judge = 0
        run_sound.stop()
    else:
        runsound_judge += 1
        if runsound_judge == 1:
            run_sound.play()

    if visited[0] == 0 and player.background == img1:   # 總圖問題(編號1)
        run_sound.stop()
        visited[0] = 1
        result = BuildWindow("是否進入？", "請問是否要進入宿舍？", "進去拉哪次不進去的",
                             "先不要啦QQ", '讓我再考慮一下><', None, None, None, None, 1)
        if result.join:
            BuildWindow("Q1-1", "現今總圖為1998/11/14正式啟用之新總圖書館，請問舊總圖為現今的哪一棟建築？",
                        "校史館", "文學院", "哈哈騙你的啦，總圖沒搬過家", '校史館', 1, 5, "舊總圖紀念館", 4)
            BuildWindow("Q1-2", "下列各項優點當中，何者非總圖的優點？", "位置多，書架後面有許多位子，不想被打擾的同學有自己的空間",
                        "位於辛亥路旁，很好找食物", "相比社科圖，就算不帶MAC進去也不會自卑", '位於辛亥路旁的圖書館為社科圖', 2, 5, "地下自習室給人完整的K書空間", 4)
            BuildWindow("Q1-3", "同學間口耳相傳的「總打」是…？", "總圖打掃阿姨",
                        "總圖打code打到起肖", "總圖啪啪啪", '呵呵不用多說了吧', 3, 10, "總圖打麻將", 4)
            root = tk.Tk()
            root.withdraw()
            msg.showinfo('分數小結', '你總共獲得了%d分，繼續加油' % player.point)
        else:
            root = tk.Tk()
            root.withdraw()
            msg.showinfo('BYEBYE!', 'BYEBYE!!!')
    if visited[1] == 0 and player.background == img2:   # 傅鐘問題(編號2)
        run_sound.stop()
        visited[1] = 1
        result = BuildWindow("是否進入？", "請問是否要進入宿舍？", "進去拉哪次不進去的",
                             "先不要啦QQ", '讓我再考慮一下><', None, None, None, None, 1)
        if result.join:
            BuildWindow("Q2-1", "目前位於椰林大道上的傅鐘其實非第一個傅鐘，第一代傅鐘因為禁不起長年的敲打而出現裂痕，所以後來才再重新造了一口鐘。請問，當初第一代傅鐘日響幾聲?",
                        "根據當時時間決定敲打次數 ", "根據當年台大幾週年決定", "55聲", '為55聲，因為55是傅校長逝世的歲數。', 3, 5, "21聲", 4)
            BuildWindow("Q2-2", "承上題，第一代傅鐘上面刻了什麼字？", "「敦品勵學，愛國愛人」", "「我愛令傑，令傑愛我」",
                        "「葉台清交，謙虛內斂」", '「敦品勵學，愛國愛人」為台大校訓，「思想自由，兼容並包」為北京大學校訓', 1, 5, "「思想自由，兼容並包」", 4)
            BuildWindow("Q2-3", "傳說，如果跟著傅鐘數完21聲，會發生什麼事情？", "能永遠停留在21歲", "會被21", "會交到21個男/女朋友",
                        '原本會響21聲是因為傅校長曾經說過：「一天只有21個小時，因為3小時是用來沈思的」，後來被傳為要是跟著一起數會被21', 2, 10, "校長在21:21在臉書上親自發文致謝", 4)
            root = tk.Tk()
            root.withdraw()
            msg.showinfo('分數小結', '你總共獲得了%d分，繼續加油' % player.point)
        else:
            root = tk.Tk()
            root.withdraw()
            msg.showinfo('BYEBYE!', 'BYEBYE!!!')
    if visited[2] == 0 and player.background == img3:   # 醉月湖問題(編號3)
        run_sound.stop()
        visited[2] = 1
        result = BuildWindow("是否進入？", "請問是否要進入宿舍？", "進去拉哪次不進去的",
                             "先不要啦QQ", '讓我再考慮一下><', None, None, None, None, 1)
        if result.join:
            BuildWindow("Q3-1", "醉月湖的舊稱為何？", "亭心湖", "牛湳池", "文心堤",
                        '醉月湖原本是農用池埤，為調節瑠公圳之用，舊稱為牛湳池', 2, 5, "瑠公圳第四蓄水池", 4)
            BuildWindow("Q3-2", "醉月湖名稱由來為何？", "〈春夜宴從弟桃花源序〉：「開瓊筵以坐花，飛羽觴而醉月」", "為了吸引畢業生以及其他外校學生而取的炫砲名字", "校長經過時因陶醉於此月色，而因此取「醉月」為其名",
                        '1973年，鄭梓和蘇元良兩位同學為舉辦畢業聯誼會，因此策劃了划船比賽，為了能使畢業生踴躍參與及吸引校內其它同學的目光，這兩位同學將比賽地點命名「醉月湖」，並於海報上刊登活動日期3月19日～20日，直到划船比賽的當日，「醉月湖」之名才出現於《畢聯會訊》，而後媒體及校內人士廣為稱之', 2, 5, "景色之美足以閉月，引此取名為「醉月」", 4)
            BuildWindow("Q3-3", "3.  傳說，半夜經過醉月湖，會聽到一位女生悄悄地問：「」，但怎麼樣都找不到問話的人。", "「半夜還敢走這裡，這麼說，你很勇ㄛ」", "「歐尼醬！要不要陪我去散步啊」", "「晚上好冷，可以借我一件外套嗎」",
                        '傳說，曾經有位女學生為了挽回感情，與男友相約晚上11點在醉月湖的湖心亭相見，但因為遲遲等不到對方的到來，於是想不開輕生。此後，有人曾在11點左右時路過湖畔，聽到有女生悄悄地問：「請問，現在幾點了？」但怎麼找都找不到問話的人', 4, 10, "「請問，現在幾點了」", 4)
            root = tk.Tk()
            root.withdraw()
            msg.showinfo('分數小結', '你總共獲得了%d分，繼續加油' % player.point)
        else:
            root = tk.Tk()
            root.withdraw()
            msg.showinfo('BYEBYE!', 'BYEBYE!!!')
    if visited[11] == 0 and player.background == img12:  # 水源問題(編號12)
        run_sound.stop()
        visited[11] = 1
        result = BuildWindow("是否進入？", "請問是否要進入宿舍？", "進去拉哪次不進去的",
                             "先不要啦QQ", '讓我再考慮一下><', None, None, None, None, 1)
        if result.join:
            BuildWindow("Q12-1", ".請問若貼有台大自行車車證的自行車被拖吊，第幾次之後開始須繳罰金?", "第一次 ",
                        "第二次", "第三次", '被拖吊第三次開始須繳納50元', 3, 5, "只要有貼車證就不需繳罰金", 4)
            BuildWindow("Q12-2", "水源拖吊場會有二手自行車的拍賣，提供給學校師生以便宜的價格購買腳踏車的機會，請問每人每學年有幾次的購買機會?",
                        "一次", "兩次", "三次", '每學年每人可購買二手自行車次數 以 1 次為限', 1, 5, "想買多少就買多少", 4)
            BuildWindow("Q12-3", "若未申請車證且腳踏車被拖吊，一次須繳納多少金額?", "50",
                        "100", "300", '須繳納100元/次', 2, 10, "1000", 4)
            root = tk.Tk()
            root.withdraw()
            msg.showinfo('分數小結', '你總共獲得了%d分，繼續加油' % player.point)
        else:
            root = tk.Tk()
            root.withdraw()
            msg.showinfo('BYEBYE!', 'BYEBYE!!!')
    if visited[4] == 0 and player.background == img5:  # 新體問題(編號5)
        run_sound.stop()
        visited[4] = 1
        result = BuildWindow("是否進入？", "請問是否要進入宿舍？", "進去拉哪次不進去的",
                             "先不要啦QQ", '讓我再考慮一下><', None, None, None, None, 1)
        if result.join:
            BuildWindow("Q5-1", "下列何者為新體沒有的設施?", "壁球場 ", "技擊室 ",
                        "手球場(館) ", '新體沒有滑板場', 4, 5, "滑板場", 4)
            BuildWindow("Q5-2", "請問新體從民國幾年起啟用?", "民國85年", "民國90年",
                        "民國93年", '新體民國90年啟用', 2, 5, "民國102年", 4)
            BuildWindow("Q5-3", "請問新體3-5樓的主球場共有多少固定座位?", "3321",
                        "3221", "2113", '共有3221個', 2, 10, "1322", 4)
            root = tk.Tk()
            root.withdraw()
            msg.showinfo('分數小結', '你總共獲得了%d分，繼續加油' % player.point)
        else:
            root = tk.Tk()
            root.withdraw()
            msg.showinfo('BYEBYE!', 'BYEBYE!!!')
    if visited[5] == 0 and player.background == img6:  # 社科問題(編號6)
        run_sound.stop()
        visited[5] = 1
        result = BuildWindow("是否進入？", "請問是否要進入宿舍？", "進去拉哪次不進去的",
                             "先不要啦QQ", '讓我再考慮一下><', None, None, None, None, 1)
        if result.join:
            BuildWindow("Q5-1", "請問社科院由哪位知名建築師設計?", "安藤忠雄", "貝聿銘 ",
                        "札哈·哈蒂", '台大社科院新館由伊東豊雄(Toyo Ito)所精心設計', 4, 5, "伊東豊雄", 4)
            BuildWindow("Q5-2", "社科院整棟造價約新台幣多少元?", "16億", "5億",
                        "35億", '造價：新台幣16億元', 1, 5, "5500萬", 4)
            BuildWindow("Q5-3", "請問社科院共有幾層樓?", "地上7層、地下2層", "地上8層、地下2層",
                        "地上7層、地下4層", '地上8層、地下2層', 2, 10, "地上5層、地下2層", 4)
            root = tk.Tk()
            root.withdraw()
            msg.showinfo('分數小結', '你總共獲得了%d分，繼續加油' % player.point)
        else:
            root = tk.Tk()
            root.withdraw()
            msg.showinfo('BYEBYE!', 'BYEBYE!!!')
    if visited[6] == 0 and player.background == img7:  # 男一舍問題(編號7)
        run_sound.stop()
        visited[6] = 1
        result = BuildWindow("是否進入？", "請問是否要進入宿舍？", "進去拉哪次不進去的",
                             "先不要啦QQ", '讓我再考慮一下><', None, None, None, None, 1)
        if result.join:
            BuildWindow("Q7-1", "台大男一舍是什麼類型的宿舍？", "男學生宿舍", "男女學生混合宿舍", "男教職員宿舍",
                        '台大男一舍主要提供一年級的男學生住宿，雖然裡面可能蠻常會遇到女性，不過男一舍確實是男性宿舍喔！', 1, 5, "狗狗宿舍", 4)
            BuildWindow("Q7-2", "男一舍B1樓沒有提供什麼服務？", "影印部", "撞球場", "卡拉OK",
                        '雖然偶爾在男一舍可以聽到美妙的歌聲，不過只有在浴室才有這種享受喔，男一舍B1樓有超商、影印部、餐飲部(提供早、午、晚餐及宵夜)、桌球場、撞球場，不過沒有卡拉OK喔！', 3, 5, "餐飲部", 4)
            BuildWindow("Q7-3", "男一舍位於什麼地方呢？", "長興街", "舟山路", "溫州路",
                        '台大男一舍位於台北市大安區長興街50號。', 1, 10, "椰林大道", 4)
            root = tk.Tk()
            root.withdraw()
            msg.showinfo('分數小結', '你總共獲得了%d分，繼續加油' % player.point)
        else:
            root = tk.Tk()
            root.withdraw()
            msg.showinfo('BYEBYE!', 'BYEBYE!!!')
    if visited[7] == 0 and player.background == img8:  # 校門問題(編號8)
        run_sound.stop()
        visited[0] = 1
        result = BuildWindow("是否進入？", "請問是否要進入宿舍？", "進去拉哪次不進去的",
                             "先不要啦QQ", '讓我再考慮一下><', None, None, None, None, 1)
        if result.join:
            BuildWindow("Q8-1", "台大校門是什麼顏色的呢？", "銀白色", "紅褐色", "七彩霓虹色",
                        '台大校門使用褐色面磚與唭哩岸石建造，色彩與校園校舍同為咖啡色系。', 2, 5, "暗紫色", 4)
            BuildWindow("Q8-2", "台大校門最早在什麼時候建成呢？？", "1931", "1963", "2004",
                        '台大校門建於日治時期昭和6年，是由臺灣總督府總督官房營繕課設計。', 1, 5, "還沒蓋好", 4)
            BuildWindow("Q8-3", "台大校門中間的「國立臺灣大學」字樣是誰所題的呢？", "傅斯年", "蔣中正",
                        "朱家驊", '臺大校門中間的「國立臺灣大學」字樣是由前中華民國教育部部長朱家驊題字。', 3, 10, "管中閔", 4)
            root = tk.Tk()
            root.withdraw()
            msg.showinfo('分數小結', '你總共獲得了%d分，繼續加油' % player.point)
        else:
            root = tk.Tk()
            root.withdraw()
            msg.showinfo('BYEBYE!', 'BYEBYE!!!')
    if visited[8] == 0 and player.background == img9:  # 管理學院問題(編號9)
        run_sound.stop()
        visited[0] = 1
        result = BuildWindow("是否進入？", "請問是否要進入宿舍？", "進去拉哪次不進去的",
                             "先不要啦QQ", '讓我再考慮一下><', None, None, None, None, 1)
        if result.join:
            BuildWindow("Q9-1", "台大管院希望培養學生什麼樣的能力？", "獨立思考與解決問題的能力", "如猴猴一般快樂玩耍的能力", "優秀的跑跳能力",
                        '教學方面，管理學院期望招收及培育具有領導管理潛能的一流學生，培養學生獨立思考與解決問題能力。', 1, 5, "我也不知道要培養什麼樣的能力", 4)
            BuildWindow("Q9-2", "台大管院大學部共有幾個系？", "4", "5", "6",
                        '台大管理學院大學部有國企、工管、會計、財金、資管共五個系。', 2, 5, "7", 4)
            BuildWindow("Q9-3", "台大管院財金系知名的日月大賢者是哪一位教授呢？", "陳明賢", "陳聖賢", "李賢源",
                        '陳明賢教授因爲對學生的溫馨關懷、熱心協助，尤其是他開設的財務金融入門課程，讓大一學生對未來有了更明確的方向，對學生而言如日月一般引領著前進，因而被學生尊稱為日月大賢者。', 1, 10, "這個人是虛構的", 4)
            root = tk.Tk()
            root.withdraw()
            msg.showinfo('分數小結', '你總共獲得了%d分，繼續加油' % player.point)
        else:
            root = tk.Tk()
            root.withdraw()
            msg.showinfo('BYEBYE!', 'BYEBYE!!!')

    for event in pygame.event.get():  # 取得輸入，把他得到的動作並成為一個list
        if event.type == pygame.QUIT:  # 沒有函數的離開(?)
            root = tk.Tk()
            root.withdraw()
            exitbox = msg.askquestion("Exit", "Are you sure to exit?")
            if exitbox == 'yes':
                running = False

    all_sprites.update()  # 更新遊戲
    screen.blit(player.background, (0, 0))  # 畫面顯示改成了圖片
    all_sprites.draw(screen)  # 把all_sprite裡面的東西都畫出來
    draw_text(screen, str(player.energy), 30, WIDTH/2, 12)
    draw_text(screen, str("ENERGY:"), 30, WIDTH/2-80, 12)
    draw_text(screen, str(int(player.time)), 30, WIDTH/2, 50)
    draw_text(screen, str("TIME:"), 30, WIDTH/2-80, 50)
    draw_text(screen, str("POINT:"), 30, WIDTH/2-80, 100)
    draw_text(screen, str(player.point), 30, WIDTH/2, 100)
    pygame.display.update()  # 更新
pygame.quit()  # 離開
