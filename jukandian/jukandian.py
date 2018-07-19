import sys
import threading
import time
sys.path.append("..")

from core import drive

click_point = (170, 180)
# back_point = (40, 1050)
back_point = (30, 100)
refresh_point = (35, 670)
move_distance = (5, 10)

def scroll(times, distance, direction):
	for x in range(times):
		time.sleep(10)
		drive.scroll_mouse(0, distance * direction)

def fake_read():
	for x in range(1):
		p = list(move_distance)
		p.append(-1 if x % 2 == 0 else 1)
		scroll(*p)


def work():
	while not drive.esc_pressed:
		time.sleep(4)

		# drive.get_position()

		drive.position_mouse(*click_point)
		time.sleep(2)
		drive.click()

		fake_read()

		time.sleep(8)
		
		drive.position_mouse(*back_point)
		time.sleep(2)
		drive.click()

		time.sleep(2)
		drive.position_mouse(*refresh_point)
		time.sleep(2)
		drive.click()

		time.sleep(8)


def start():
	t = threading.Thread(target=work)
	t.start()
	t.join()

if __name__ == '__main__':
	start()