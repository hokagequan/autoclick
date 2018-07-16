
from pynput.mouse import Button, Controller

mouse = Controller()

print('The current pointer position is {0}'.format(mouse.position))

def position_mouse(x, y):
	mouse.position = (x, y)

def click():
	mouse.click(Button.left, 1)

def press_mouse():
	mouse.press(Button.left)

def release_mouse():
	mouse.release(Button.left)

def move_mouse(x, y):
	mouse.move(x, y)