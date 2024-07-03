# p10_setup_loadImage_draw_image_global
def setup():
    global imgBG,imgRabbit
    size(1000,667) # 用你的background.jpg圖的大小
    imgBG = loadImage('background.jpg')
    imgRabbit= loadImage('rabbit.png') # 找半透明的png圖
def draw():
    global imgBG,imgRabbit
    image(imgBG, 0, 0)
    for i in range(5):
        image(imgRabbit, i*200, 0, 450, 300)
    image(imgRabbit, mouseX, mouseY, 450, 300)
