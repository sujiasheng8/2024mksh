# p10_setup_loadImage_draw_image_global
def setup():
    global imgBG,imgRabbit
    size(1000,667) # 用你的background.jpg圖的大小
    imgBG = loadImage('background.jpg')
    imgRabbit= loadImage('rabbit.png') # 找半透明的png圖
def draw():
    global imgBG,imgRabbit
    image(imgBG, 0, 0)
    for i in range(100):
        image(imgRabbit, x[i], y[i], 150, 100)
    image(imgRabbit, mouseX, mouseY, 150, 100)
x = [0]*100
y = [0]*100
N = 0
def mousePressed():
    global N
    x[N], y[N] = mouseX, mouseY
    N += 1
