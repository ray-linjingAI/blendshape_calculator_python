from pythonosc import udp_client
import glob
import time
import cv2
client = udp_client.SimpleUDPClient('127.0.0.1',6969)
files = glob.glob('result_face_bs/*')
for i in range(1,302):
    with open('result_face_bss/face_bs_{}.txt'.format(i)) as f:
        bs = f.read()
        bs = eval(bs)
    print(bs)
    cv2.imshow('sss',cv2.imread('testvideo/{}.jpg'.format(i-1)))
    cv2.waitKey(1)
    client.send_message("/test", bs)
    time.sleep(0.05)