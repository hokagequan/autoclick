

class Size(object):
    """docstring for Size"""
    def __init__(self, width, height):
        super(__class__, self).__init__()
        self.width = width
        self.height = height

class Point(object):
    """docstring for Point"""
    def __init__(self, x, y):
	    super(__class__, self).__init__()
	    self.x = x
	    self.y = y

    def __add__(self, other_point):
    	return Point(self.x + other_point.x, self.y + other_point.y)

    def __str__(self):
    	return "({}, {})".format(self.x, self.y)

    def to_tuple(self):
    	return (self.x, self.y)