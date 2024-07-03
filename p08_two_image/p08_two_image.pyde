# p08_two_image
size(1000,667) # 用你的background.jpg圖的大小
imgBG = loadImage('background.jpg')
image(imgBG, 0, 0)
imgRabbit= loadImage('rabbit.png') # 找半透明的png圖
image(imgRabbit, 0, 0, 450, 300)
