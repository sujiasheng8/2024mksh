# p21_PaperScissorsStone01_text
def setup():
    size(600,300)
def draw():
    fill(255)# 白色的格子
    rect(0,0, 300,300)
    rect(300,0, 300,300)
    
    rect(400,100, 100,50) # 剪刀Scissor
    rect(400,150, 100,50) # 石頭Rock
    rect(400,200, 100,50) # 布Paper
    
    textSize(50) # 文字大小
    textAlign(LEFT, TOP)
    fill(0) # 黑色字
    text("Scissor", 400,100)
    text("Rock", 400,150)
    text("paper", 400,200)
