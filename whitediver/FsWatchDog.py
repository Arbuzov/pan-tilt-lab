'''
Created on 9 Oct 2020

@author: whitediver
'''
import asyncio
import logging
import os
import sys


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class FSWatchDog(object):
    '''
    classdocs
    '''


    def __init__(self, watch_dir: str):
        '''
        Constructor
        '''
        self.watch_dir = os.path.abspath(watch_dir)
        self.started = False
    
    async def start(self):
        self.started = True
        logger.info(self.watch_dir)
        logger.info("argv was %s", sys.argv)
        logger.info("sys.executable was %s", sys.executable)
        before = max(self.file_times())
        while self.started:
            await asyncio.sleep(1)
            after = max(self.file_times())
            if before != after:
                logger.info('Files changed')
                i = 4
                while i>0:
                    before = after
                    i = i-1
                    await asyncio.sleep(1)
                    after = max(self.file_times())
                    if before != after:
                        i = 3
                os.execvp(sys.executable, ['python'] + sys.argv)
            
    def file_times(self):
        for filename in os.listdir(self.watch_dir):
            yield os.stat(os.path.join(self.watch_dir, filename)).st_mtime            
            
    def stop(self):
        self.started = False