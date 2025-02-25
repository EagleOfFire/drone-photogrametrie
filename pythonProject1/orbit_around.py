import cv2, time
from djitellopy import Tello

def orbit_around_with_image():
    angle = 0
    tello.streamoff()
    tello.streamon()
    
    while angle < 360:
        tello.rotate_clockwise(angle)
        tello.move_left(3)
        img = tello.get_frame_read().frame
        cv2.imwrite(f'orbit_around_{time.time()}.jpg', img)
        angle += 1
        time.sleep(1)
        key = cv2.waitKey(1) & 0xff
        if key == 27 or key == ord('n'): # ESC
            break
    
    tello.streamoff()
        
def orbit_around():
    angle = 0
    while angle < 360:
        tello.rotate_clockwise(angle)
        tello.move_left(3)
        angle += 1
        key = cv2.waitKey(1) & 0xff
        if key == 27 or key == ord('n'): # ESC
            break
        
def safe_test():
    angle = 0
    while angle < 10:
        tello.rotate_clockwise(angle)
        tello.move_left(3)
        angle += 1
        key = cv2.waitKey(1) & 0xff
        if key == 27 or key == ord('n'): # ESC
            break
        

if __name__ == '__main__':
    tello = Tello()
    tello.connect()

    tello.takeoff()
    orbit_around_with_image()
    tello.land()

