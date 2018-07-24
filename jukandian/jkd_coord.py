import sys
sys.path.append("..")

from core.coord import CoordMaker
from core.models import Point

click_point = Point(170, 180)
back_point = Point(30, 100)
refresh_point = Point(35, 670)
move_distance = Point(5, 10)

class JukandianCoord(CoordMaker):
    """docstring for JukandianCoord"""
    def get_click_point(self):
    	return self.origin_point + click_point

    def get_move_distance(self):
    	return move_distance

    def get_back_point(self):
        return self.origin_point + back_point

    def get_refresh_point(self):
    	return self.origin_point + refresh_point
		
