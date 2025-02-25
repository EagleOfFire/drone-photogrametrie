import cv2, time
from djitellopy import Tello

tello = Tello()
tello.connect()

tello.streamoff()
tello.streamon()

while True:
        img = tello.get_frame_read().frame
        cv2.imshow("drone", img)
        cv2.imwrite(f'./data/orbit_around_{time.time()}.jpg', img)
        key = cv2.waitKey(1) & 0xff
        if key == 27 or key == ord('n'): # ESC
            break
tello.streamoff()