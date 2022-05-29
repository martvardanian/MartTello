import cv2
from djitellopy import Tello
from datetime import datetime

tello = Tello()

tello.connect()
tello.streamon()  # miacnel kamera

battery = tello.get_battery()
height = tello.get_height()


def print_image():
    now = datetime.now()
    frame_read = tello.get_frame_read()
    cv2.imwrite(f"picture{now}.png", frame_read.frame)  # save nkary


print("Battery: " + str(battery) + "%")
tello.takeoff()
tello.move_up(50)
tello.move_right(50)
tello.move_forward(500)
tello.move_forward(500)
tello.move_forward(500)
tello.move_forward(500)
tello.move_up(150)
tello.move_forward(500)
tello.move_forward(500)
tello.move_forward(100)

tello.rotate_counter_clockwise(180)

print_image()

tello.move_back(500)
tello.move_back(500)
tello.move_back(100)
tello.move_down(150)
tello.move_back(500)
tello.move_back(500)
tello.move_back(500)
tello.move_back(500)
tello.move_left(50)

print("Height: " + str(height) + "cm")
tello.land()
