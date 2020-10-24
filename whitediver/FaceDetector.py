'''
Created on 9 Oct 2020

@author: whitediver
'''
import asyncio
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

try:
    import cv2
except ImportError as error:
    logger.error(error)

class FaceDetector(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.started = False
        self.cap = None
    
    async def start(self):
        self.started = True
        self.cap = cv2.VideoCapture(0)
        self.cap.set(3,640)
        self.cap.set(4,480)
        while self.started:
            try:
                ret, img = self.cap.read()
                await asyncio.sleep(1)
                gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                cv2.imshow('video', img)
            except Exception as error:
                logger.error(error)
                self.started = False
            
    def stop(self):
        self.started = False
        self.cap.release()
        cv2.destroyAllWindows()