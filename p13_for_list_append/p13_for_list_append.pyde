# p13_for_list_append
def setup():
    global imgBG,imgRabbit
    size(1000,667) # 用你的background.jpg圖的大小
    imgBG = loadImage('background.jpg')
    imgRabbit= loadImage('rabbit.png') # 找半透明的png圖
def draw():
    global imgBG,imgRabbit
    image(imgBG, 0, 0)
    for i in range(len(x)):
        image(imgRabbit, x[i], y[i], 150, 100)
    image(imgRabbit, mouseX, mouseY, 150, 100)
x = [] # x = [0]*10
y = [] # y = [0]*10
#N = 0
def mousePressed():
    x.append(mouseX) #global N
    y.append(mouseY) #x[N], y[N] = mouseX, mouseY
    #N += 1
