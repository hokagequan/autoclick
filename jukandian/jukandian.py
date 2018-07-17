import sys
import threading
import time
sys.path.append("..")

from core import drive

click_point = (270, 240)
# back_point = (40, 1050)
back_point = (50, 120)
refresh_point = (60, 1000)

def scroll(times, distance, direction):
	for x in range(times):
		time.sleep(1)
		drive.scroll_mouse(0, distance * direction)

def fake_read():
	for x in range(8):
		p = list(move_distance)
		p.append(-1 if x % 2 == 0 else 1)
		scroll(*p)


def work():
	while not drive.esc_pressed:
		time.sleep(2)

		# drive.get_position()

		drive.position_mouse(*click_point)
		time.sleep(1)
		drive.click()

		time.sleep(5)
		
		drive.position_mouse(*back_point)
		time.sleep(1)
		drive.click()
		# time.sleep(1)
		# drive.click()

		time.sleep(1)
		drive.position_mouse(*refresh_point)
		time.sleep(1)
		drive.click()

		time.sleep(6)


def start():
	t = threading.Thread(target=work)
	t.start()
	t.join()

if __name__ == '__main__':
	start()