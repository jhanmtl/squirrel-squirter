# -*- coding: utf-8 -*-
"""
Created on Sat Sep  7 13:29:35 2019

@author: jh
"""
from threading import Thread
import cv2
import requests
import numpy as np

def draw(info,img):
        data=info.split(',')
  
        x1=int(round(float(data[0])))
        y1=int(round(float(data[1])))
        x2=int(round(float(data[2])))
        y2=int(round(float(data[3])))
        label=data[4]
        score=float(data[5])
        fps=float(data[6])
        if label=='person':
            cv2.rectangle(img, (int(x1), int(y1)), (int(x2), int(y2)), (0,255,0), 1)
            cv2.putText(img,label+': '+str(round(100*score,4))+'%', (int(x1),int(y2-5)),cv2.FONT_HERSHEY_SIMPLEX, 0.5,(0,255,0),1)

class frameGrabber:
    
    def __init__(self,url):
        self.r=requests.get(url,stream=True)
        self.img=None
        self.stopped=False
        print(self.r.status_code)       
                  
        
    def start(self):
        print('starting thread')
        t=Thread(target=self.update,args=())
        t.setDaemon(True)
        t.start()
        print('thread started')
        return self
       
    def update(self):
        while True:
            if self.stopped==True:
                return
            else:
                img_bytes=bytes()
                for chunk in self.r.iter_content(chunk_size=1024):
                    img_bytes+=chunk
                    a=img_bytes.find(b'\xff\xd8')
                    b=img_bytes.find(b'\xff\xd9')
                    if a!=-1 and b!=-1:
                        jpg=img_bytes[a:b+2]
                        img_bytes=img_bytes[b+2:]
                        self.img=cv2.imdecode(np.frombuffer(jpg,dtype=np.uint8),cv2.IMREAD_COLOR)
    def read(self):
        return self.img
    
    def stop(self):
        self.stopped=True
        
class predictionGrabber(frameGrabber):
          
    def update(self):
        while True:
            if self.stopped==True:
                return
            else:
                msg=bytes()
                for chunk in self.r.iter_content():
                    msg+=chunk
                    a=msg.find(b'<')
                    b=msg.find(b'>')
                    if a!=-1 and b!=-1:
                        val=msg[a+1:b]
                        msg=msg[b+1:]
                        self.img=val.decode()
                        

    


