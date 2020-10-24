import asyncio
import logging
import pathlib
import signal

from whitediver.AxisContainer import AxisContainer
from whitediver.FaceDetector import FaceDetector
from whitediver.FsWatchDog import FSWatchDog
from whitediver.KeyboardController import KeyboardController
from whitediver.ServoController import ServoController


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def main():

    loop = asyncio.get_event_loop()
    axis = AxisContainer()
    servo_controller = ServoController(axis)
    fs_watch_dog = FSWatchDog(pathlib.Path(__file__).parent.absolute())
    keyboard_controller = KeyboardController(axis)
    face_detector = FaceDetector()
    signals = [signal.SIGHUP, signal.SIGTERM, signal.SIGINT]

    async def kill_loop():
        '''Watches tasks and stops the loop then all tasks are done'''  
        loop = asyncio.get_event_loop()
        servo_controller.stop()
        fs_watch_dog.stop()
        keyboard_controller.stop()
        face_detector.stop()
        while len([t for t in asyncio.all_tasks() if t is not
                 asyncio.current_task()])>0:
            #print(asyncio.all_tasks())
            await asyncio.sleep(1)
        loop.stop()
    
    def shutdown_handler():
        ''''Graceful shutdown'''
        loop = asyncio.get_event_loop()
        loop.create_task(kill_loop())
    
    try:
        for _signal in signals:
            loop.add_signal_handler(_signal, shutdown_handler)      
    except NotImplementedError:
        logging.warning('Not implemented signal')
      
    logger.info('Launching startup sequence')
    loop.create_task(servo_controller.start())
    loop.create_task(fs_watch_dog.start())
    loop.create_task(keyboard_controller.start())
    loop.create_task(face_detector.start())
    logger.info('Launching main loop')
    loop.run_forever()

if __name__ == '__main__':
    main()