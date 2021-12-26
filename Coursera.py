import tkinter as tk
import tkinter.font as tkFont
import math
from PIL import ImageTk
from PIL import Image
class Calculator(tk.Frame):  # 從tk那邊inherit視窗介面
    def __init__(self):  # 初始化，初始tk，切格子
        tk.Frame.__init__(self)
        self.shouldreset = True
        self.grid()
        self.image = Image.open('sqrt.jpg')  # 為了改變大小多import一個東西
        self.image = self.image.resize((50, 50), Image.ANTIALIAS) 
        self.image = ImageTk.PhotoImage(self.image)
        self.createwidget()
    def setnumber(self, content):
        if self.shouldreset == True:
            self.labelNum.configure(text = content)
            self.shouldreset = False
        else:
            self.labelNum.configure(text=self.labelNum.cget("text") + content)

    def createwidget(self):
        f1 = tkFont.Font(size=48, family='Arial')
        f2 = tkFont.Font(size=48, family='Arial')
        # 這個0(label)屬於WINDOW
        self.labelNum = tk.Label(self, text=None, height=1, width=7, font=f1)
        self.buttomNum1 = tk.Button(
            self, text="1", command=self.clickbutton1, height=1, width=2, font=f2)
        self.buttomNum2 = tk.Button(
            self, text="2", command=self.clickbutton2, height=1, width=2, font=f2)
        self.buttomNum3 = tk.Button(
            self, text="3", command=self.clickbutton3, height=1, width=2, font=f2)
        self.buttomNum4 = tk.Button(
            self, text="4", command=self.clickbutton4, height=1, width=2, font=f2)
        self.buttomNum5 = tk.Button(
            self, text="5", command=self.clickbutton5, height=1, width=2, font=f2)
        self.buttomNum6 = tk.Button(
            self, text="6", command=self.clickbutton6, height=1, width=2, font=f2)
        self.buttomNum7 = tk.Button(
            self, text="7", command=self.clickbutton7, height=1, width=2, font=f2)
        self.buttomNum8 = tk.Button(
            self, text="8", command=self.clickbutton8, height=1, width=2, font=f2)
        self.buttomNum9 = tk.Button(
            self, text="9", command=self.clickbutton9, height=1, width=2, font=f2)
        self.buttomNum0 = tk.Button(
            self, text="0", command=self.clickbutton0, height=1, width=2, font=f2)
        self.buttomNums = tk.Button(
            self, image=self.image, command=self.clickbuttons, height=1, width=2, font=f2)
        # Command:按下去之後做的事情
        self.labelNum.grid(row=0, column=0, columnspan=3, sticky=tk.NW+tk.SE)  # 擺哪裡
        self.buttomNum1.grid(row=1, column=0, sticky=tk.NW+tk.SE)  # 擺哪裡
        self.buttomNum2.grid(row=1, column=1, sticky=tk.NW+tk.SE)
        self.buttomNum3.grid(row=1, column=2, sticky=tk.NW+tk.SE)
        self.buttomNum4.grid(row=2, column=0, sticky=tk.NW+tk.SE)
        self.buttomNum5.grid(row=2, column=1, sticky=tk.NW+tk.SE)
        self.buttomNum6.grid(row=2, column=2, sticky=tk.NW+tk.SE)
        self.buttomNum7.grid(row=3, column=0, sticky=tk.NW+tk.SE)
        self.buttomNum8.grid(row=3, column=1, sticky=tk.NW+tk.SE)
        self.buttomNum9.grid(row=3, column=2, sticky=tk.NW+tk.SE)
        self.buttomNum0.grid(row=4, column=0, columnspan=2, sticky=tk.NW+tk.SE)
        self.buttomNums.grid(row=4, column=2, sticky=tk.NW+tk.SE)

    def clickbutton1(self):
        self.setnumber("1")
    def clickbutton2(self):
        self.setnumber("2")
    def clickbutton3(self):
        self.setnumber("3")
    def clickbutton4(self):
        self.setnumber("4")
    def clickbutton5(self):
        self.setnumber("5")
    def clickbutton6(self):
        self.setnumber("6")
    def clickbutton7(self):
        self.setnumber("7")
    def clickbutton8(self):
        self.setnumber("8")
    def clickbutton9(self):
        self.setnumber("9")
    def clickbutton0(self):
        self.setnumber("0")
    def clickbuttons(self):
        current = float(self.labelNum.cget("text"))
        self.labelNum.configure(text = str(round(math.sqrt(current), 2)))
        self.shouldreset = True

        # cget:得到目前的text是甚麼(預設是0)
        # 如果按鈕會跟者跑，代表還沒有設定對其之類ㄉ東西(預設在中間)
cal = Calculator()  # 呼叫這個class
cal.master.title("SQUARE ROOT")
cal.mainloop()
