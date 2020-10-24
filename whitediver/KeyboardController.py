'''
Created on 9 Oct 2020

@author: whitediver
'''
import asyncio
import logging
from whitediver.AxisContainer import AxisContainer

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class KeyboardController(object):
    '''
    classdocs
    '''


    def __init__(self, axis_container: AxisContainer):
        '''
        Constructor
        '''
        self.started = False
        self.axis_container = axis_container   
        
    async def start(self):
        self.started = True
        while self.started:
            await asyncio.sleep(1)
            
    def stop(self):
        self.started = False