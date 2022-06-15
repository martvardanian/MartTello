import cv2
from djitellopy import Tello
import time
from datetime import datetime
from threading import Thread

tello = Tello()

tello.connect()
keepRecording = True
tello.streamon()

battery = tello.get_battery()


def print_image():
    now = datetime.now()
    frame_read = tello.get_frame_read()
    cv2.imwrite(f"picture{now}.png", frame_read.frame)  # save nkary


def record_video():
    frame_read = tello.get_frame_read()
    height, width, _ = frame_read.frame.shape
    video = cv2.VideoWriter('video1.avi', cv2.VideoWriter_fourcc(*'XVID'), 30, (width, height))

    while keepRecording:
        video.write(frame_read.frame)
        time.sleep(1 / 30)

    video.release()


recorder = Thread(target=record_video)
recorder.start()

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
    tello.move_down(h - 500)
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

height = tello.get_height()
print("Height: " + str(height) + "cm")

tello.land()

keepRecording = False
recorder.join()
