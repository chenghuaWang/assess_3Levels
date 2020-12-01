from PIL import ImageGrab
import numpy as np
import cv2
p = ImageGrab.grab()#获得当前屏幕
k=np.zeros((200,200),np.uint8)#清零
a,b=p.size#获得当前屏幕的大小
fourcc = cv2.VideoWriter_fourcc(*'XVID')#编码格式
video = cv2.VideoWriter('test.avi', fourcc, 16, (a, b))#输出文件命名为test.mp4,帧率为16，可以自己设置
while True:
    im = ImageGrab.grab()#获得当前屏幕
    imm=cv2.cvtColor(np.array(im), cv2.COLOR_RGB2BGR)#转为opencv的BGR格式
    video.write(imm)#写入
    # cv2.imshow('imm', k)#显示
    if cv2.waitKey(1) & 0xFF == ord('q'):#q键推出
        break
video.release()
cv2.destroyAllWindows()
