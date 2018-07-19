import tkinter as tk


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
		


window_size = Size(1200, 700)
phone_size = Size(320, 600)


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.init_window()
        self.create_widgets()

    def init_window(self):
        self.master.wm_attributes("-transparent", True)
        self.master.config(bg="systemTransparent")

    def create_widgets(self):
        phone_window_size = Size(window_size.width / 2, window_size.height)
        left_top_x = (phone_window_size.width - phone_size.width) / 2
        left_top_y = (phone_window_size.height - phone_size.height) / 2
        left_top = Point(left_top_x, left_top_y)

        # Phone container
        phone_window = tk.Frame(self, bg="red", width=window_size.width / 2, height=window_size.height)
        phone_window.pack(side=tk.LEFT)

        # Phone position
        canvas = tk.Canvas(phone_window, width=window_size.width / 2, height=window_size.height, bg="systemTransparent")
        canvas.place(x=0, y=0)
        canvas.create_rectangle(left_top.x, left_top.y, left_top.x + phone_size.width, left_top.y + phone_size.height, dash=(10, 6), outline="green", width=3)
        canvas.pack()
        
        # Operation panel
        op_frame = tk.Frame(self, width=window_size.width / 2, height=window_size.height)
        op_frame.pack(side=tk.LEFT)

        # self.hi_there = tk.Button(self)
        # self.hi_there["text"] = "Hello World\n(click me)"
        # self.hi_there["command"] = self.say_hi
        # self.hi_there.pack(side="top")

        # self.quit = tk.Button(self, text="QUIT", fg="red",
        #                       command=root.destroy)
        # self.quit.pack(side="bottom")

    def say_hi(self):
        print("hi there, everyone!")

root = tk.Tk()
app = Application(master=root)
app.master.geometry("1200x700+10+10")
app.mainloop()
