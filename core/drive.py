
from pynput.mouse import Button, Controller
from pynput import keyboard


esc_pressed = False


# def on_press(key):
#     if key == keyboard.Key.esc:
#         esc_pressed = True


# def on_release(key):
#     pass


# with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
#     listener.join()


mouse = Controller()

def get_position():
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


def scroll_mouse(x, step):
    mouse.scroll(x, step)
