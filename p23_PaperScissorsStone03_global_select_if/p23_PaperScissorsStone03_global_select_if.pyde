# p23_PaperScissorsStone03_global_select_if
select = -1
def setup():
    size(600,300)
def draw():
    fill(255) # 白色的格子
    rect(0,0, 300,300)
    rect(300,0, 300,300)
    if select==0: fill(255,0,0)
    else: fill(255)
    rect(400,100, 100,50) # 剪刀Scissor
    if select==1: fill(255,0,0)
    else: fill(255)
    rect(400,150, 100,50) # 石頭Rock
    if select==2: fill(255,0,0)
    else: fill(255)
    rect(400,200, 100,50) # 布Paper
    
    textSize(25) # 文字大小
    textAlign(LEFT, TOP) # 文字對齊左上
    fill(0) # 黑色字
    text("Scissor", 400,100)
    text("Rock", 400,150)
    text("paper", 400,200)
def mousePressed(): # 如果mouse按下去
    global select
    if 400 < mouseX < 400+100: # 左右範圍內
        if 100 < mouseY < 150: select = 0 # 上下範圍也對
        if 150 < mouseY < 200: select = 1
        if 200 < mouseY < 250: select = 2
    print(select) # 把現在的選擇印出來
