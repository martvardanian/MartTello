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
print(height_start)

tello.move_up(500)
tello.move_up(500)
height_up10 = tello.get_height()
print(height_up10)

tello.move_forward(500)
tello.move_forward(500)
print_image()

tello.rotate_counter_clockwise(90)
h = height_start + height_up10 - 100
print(h)
if h > 500:
    tello.move_down(h-500)
    tello.move_down(500)
else:
    tello.move_down(h)


tello.move_forward(500)
print_image()

tello.rotate_counter_clockwise(90)
print_image()
tello.rotate_counter_clockwise(90)
print_image()
tello.rotate_counter_clockwise(90)
print_image()

tello.move_back(500)
tello.move_back(500)
tello.move_up(500)
tello.move_up(500)
print_image()

print("Height: " + str(height) + "cm")
tello.land()
