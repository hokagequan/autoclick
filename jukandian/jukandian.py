import sys
import threading
import time
sys.path.append("..")

from core import drive, worker
from core.models import Point, Size


class JukandianWorker(worker.AppWorker):
    """docstring for JukandianWorker"""
    def start(self):
        self.cancel = False

        t = threading.Thread(target=self.work)
        t.start()

    def stop(self):
        self.cancel = True

    def work(self):
        click_point = self.coord_maker.get_click_point().to_tuple()
        back_point = self.coord_maker.get_back_point().to_tuple()
        refresh_point = self.coord_maker.get_refresh_point().to_tuple()
        
        while not self.cancel:
            print("I am running")
            time.sleep(4)

            if self.cancel:
            	break

            # drive.get_position()

            drive.position_mouse(*click_point)
            time.sleep(2)
            drive.click()

            if self.cancel:
            	break

            self.fake_read()

            if self.cancel:
            	break

            time.sleep(8)

            if self.cancel:
            	break
		
            drive.position_mouse(*back_point)
            time.sleep(2)
            drive.click()

            if self.cancel:
            	break

            time.sleep(2)
            drive.position_mouse(*refresh_point)
            time.sleep(2)
            drive.click()

            if self.cancel:
            	break

            time.sleep(8)

    def fake_read(self):
        move_distance = self.coord_maker.get_move_distance()
        for x in range(1):
            p = list(move_distance.to_tuple())
            p.append(-1 if x % 2 == 0 else 1)
            self.scroll(*p)

    def scroll(self, times, distance, direction):
        for x in range(times):
            time.sleep(10)
            if self.cancel:
            	break
            drive.scroll_mouse(0, distance * direction)	
