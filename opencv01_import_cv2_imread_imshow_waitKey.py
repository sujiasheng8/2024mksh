# -*- coding: utf-8 -*-
import cv2 # 使用 OpenCV 的 cv2 外掛
# 匯入 cv2
img = cv2.imread('onepiece.png')
# 讀入 opencv.png 這張圖，小心副檔名
cv2.imshow('onecv01', img) # 要在 'opencv01'視窗裡 秀圖
cv2.imshow('hello', img) # 要在 'hello'視窗裡 秀圖
cv2.imshow('mksh', img) # 要在 'mksh'視窗裡 秀圖

cv2.waitKey(0) # 等待任意建，卡住，不要結束
# File-New Ctrl-N 開新檔案
# File-Save as 另存新檔 opencv01.py
# 存在桌面的opencv01.py
# 先寫好，不要執行，沒有圖，會當掉，要放圖
# 圖也要放在同一個目錄「桌面」