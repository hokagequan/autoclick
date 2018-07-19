import tkinter as tk


class Size(object):
	"""docstring for Size"""
	def __init__(self, width, height):
		super(__class__, self).__init__()
		self.width = width
		self.height = height


window_size = Size(1200, 700)
phone_size = Size(320, 600)


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        margin_left = 20

        phone_window = tk.Frame(self)
        phone_window.pack(side=tk.LEFT)
        canvas = tk.Canvas(phone_window, width=window_size.width / 2, height=window_size.height)
        canvas.place(x=0, y=0)
        canvas.create_rectangle(margin_left, (window_size.height - phone_size.height) / 2, margin_left + phone_size.width, (window_size.height - phone_size.height) / 2 + phone_size.height, dash=(4, 2))
        canvas.pack()
        
        op_frame = tk.Frame(self)
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
