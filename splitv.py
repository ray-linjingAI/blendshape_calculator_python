import cv2

vid = cv2.VideoCapture('223.mov')
count = 0
_ = True
while _:
    _,frame = vid.read()
    cv2.imwrite("testvideo/{}.jpg".format(count),frame)
    count+=1