import sys
import threading
sys.path.append("..")

from core import drive
from core import mouse

def work():
	

def start():
	t = threading.Thread(target=work)
	threading.append(t)
	t.start()


if __name__ == '__main__':
	start()
