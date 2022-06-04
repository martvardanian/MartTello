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
height_start = tello.get_height()

tello.move_up(20)
height_up20 = tello.get_height()

tello.move_forward(10)
print_image()

tello.rotate_counter_clockwise(90)
h = height_start + height_up20 - 18
tello.move_down(h)

tello.move_forward(500)
print_image()

tello.rotate_counter_clockwise(90)
print_image()
tello.rotate_counter_clockwise(90)
print_image()
tello.rotate_counter_clockwise(90)
print_image()

tello.move_forward(20)
tello.move_up(20)

print("Height: " + str(height) + "cm")
tello.land()
