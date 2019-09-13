# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 17:22:53 2019

@author: jh
"""

import utils
import time
import cv2
import argparse

ap=argparse.ArgumentParser()
ap.add_argument('img',type=str)
ap.add_argument('data',type=str)
args=ap.parse_args()
data_url=args.data
img_url=args.img

data_cap=utils.predictionGrabber(data_url).start()
img_cap=utils.frameGrabber(img_url).start()
time.sleep(5)

while True:
    info=data_cap.read()
    img=img_cap.read()
    if info!='pass':
        fps,delta_x,delta_y,label=utils.draw(info,img)
    cv2.imshow('',img)

    if cv2.waitKey(1)==ord('q'):
        cv2.destroyAllWindows()
        break

        
