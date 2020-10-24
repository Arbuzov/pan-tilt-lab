'''
Created on 9 Oct 2020

@author: info
'''
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class Axis(object):
    '''
    classdocs
    '''
        
    def __init__(self):
        '''
        Constructor
        '''
        self.name = ''
        self.velocity = 0
        self.position = 0

class AxisContainer(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.coods = {
            14: Axis(),
            15: Axis(),
        }
    
    def update_coords(self):
        for axis in self.coods:
            self.coods.get(axis).position = self.coods.get(axis).position + self.coods.get(axis).velocity    