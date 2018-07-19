import sys
import threading
import time
sys.path.append("..")

from core import drive
# from core import mouse
        


click_point = (150, 200)
back_point = (30, 20)
move_start_point = (150, 500)
move_distance = (0, 80)


def work():
    while not drive.esc_pressed:
        time.sleep(2)

        # drive.position_mouse(*click_point)
        # drive.click()

        # time.sleep(20)

        # drive.position_mouse(*back_point)
        # drive.click()

        print("move mouse")
        # drive.position_mouse(*move_start_point)
        # drive.press_mouse()
        # drive.move_mouse(*move_distance)
        # drive.release_mouse()
        drive.position_mouse(*click_point)
        drive.scroll_mouse(0, -200)
        print("move mouse end")


def start():
    t = threading.Thread(target=work)
    t.start()
    t.join()


if __name__ == '__main__':
    start()
