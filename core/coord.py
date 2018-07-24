
class CoordMaker(object):
    """docstring for CoordMaker"""
    def __init__(self, config):
        super(__class__, self).__init__()
        self.origin_point = config['origin_point']
        self.screen_size = config['screen_size']

    def get_click_point(self):
    	raise NotImplementedError

    @classmethod
    def create_coord(cls, config):
        return cls(config)	
