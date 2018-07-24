

class AppWorker(object):
    """docstring for AppWorker"""
    def __init__(self, coord_maker):
        super(__class__, self).__init__()
        self.coord_maker = coord_maker
        self.cancel = False

    def start(self):
    	raise NotImplementedError
    
    def stop(self):
        raise NotImplementedError


    @classmethod
    def create_worker(cls, coord_class, config):
        worker = cls(coord_class.create_coord(config))
        return worker
		