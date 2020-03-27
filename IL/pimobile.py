import brickpi3
import keyboard
from keras.models import load_model
import cv2 
from keras.preprocessing.image import img_to_array
import time
from imutils.video import VideoStream
import numpy as np

BP = brickpi3.BrickPi3()
model = load_model('full_model.h5')
print('Model: ON')
latenceStart = 2.0
runningTime = 500
vs = VideoStream(usePiCamera = True).start()
time.sleep(latenceStart)
begin = time.time()
end = time.time()

while (end - begin) < runningTime:
    end = time.time()

    frame = vs.read()
    frame = imutils.resize(frame,width=224)

    image = cv2.resize(frame,(224,224))
    image = image.astype("float") / 255.
    image = img_to_array(image)

    image = np.expand_dims(image,axis=0)

    if keyboard.is_pressed('e'):
        condition = 1
    elif keyboard.is_pressed('r'):
        condition = 2
    else:
        condition = 0

    predictions = model.predict([[image],[condition]])[0]

    if np.argmax(predictions) == 0:
        BP.set_motor_power(BP.PORT_B,-100)
        BP.set_motor_power(BP.PORT_C,-100)
        BP.set_motor_position(BP.PORT_D,1)
    elif np.argmax(predictions) == 1:
        BP.set_motor_position(BP.PORT_D,-150)
    else:
        BP.set_motor_position(BP.PORT_D,150)

