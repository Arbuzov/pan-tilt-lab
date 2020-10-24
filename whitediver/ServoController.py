'''
Created on 9 Oct 2020

@author: whitediver
'''
import asyncio
import logging
import Adafruit_PCA9685

from whitediver.AxisContainer import AxisContainer

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class ServoController(object):
    '''
    classdocs
    '''


    def __init__(self, axis_container: AxisContainer):
        '''
        Constructor
        '''
        self.pwm = Adafruit_PCA9685.PCA9685()
        self.pwm.set_pwm_freq(60)
        self.started = False
        self.axis_container = axis_container
    
    async def start(self):
        self.started = True
        while self.started:
            self.axis_container.update_coords()
            await asyncio.sleep(1)
            
    def stop(self):
        self.started = False