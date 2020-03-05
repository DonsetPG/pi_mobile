
import time 
import cv2
import imutils
import numpy    as np

from keras.preprocessing.image  import img_to_array
from imutils.video              import VideoStream

class PiCamera:

    def __init__(self,latence_start: float,width: int, height: int) -> PiCamera:
        self.latence_start: float = latence_start
        self.width: int = width
        self.height: int = height
        self.stream = None 

    def _start_stream(self):
        print('Starting video stream...')
        self.stream = VideoStream(usePiCamera = True).start() 
        time.sleep(self.latence_start)
        print('Video Stream started!')

    def _get_current_video(self) -> np.Array:

        frame = self.stream.read() 
        frame = imutils.resize(frame,width=self.width)
        image = cv2.resize(frame,(self.width,self.height))
        image = image.astype("float") / 255.
        image = img_to_array(image)
        image = np.expand_dims(image,axis=0)

        return image

    def shutdown(self):
        cv2.destroyAllWindows()
        self.stream.stop()