from tkinter import *
from tkinter import font
import tkinter as tk
import sys
sys.path.append("..")

from jukandian.jukandian import JukandianWorker
from jukandian.jkd_coord import JukandianCoord
from core.models import Point, Size
		

root = tk.Tk()
window_size = Size(1200, 700)
phone_size = Size(360, 700)

workers_map = {"聚看点": (JukandianWorker, JukandianCoord)}

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
        self.left_top = Point(left_top_x, left_top_y)

        # Phone container
        phone_window = tk.Frame(self, bg="systemTransparent", width=window_size.width / 2, height=window_size.height)
        phone_window.pack(side=tk.LEFT)

        # Phone position
        canvas = tk.Canvas(phone_window, width=window_size.width / 2, height=window_size.height, bg="systemTransparent")
        canvas.place(x=0, y=0)
        canvas.create_rectangle(self.left_top.x, self.left_top.y, self.left_top.x + phone_size.width, self.left_top.y + phone_size.height, dash=(10, 6), outline="green", width=3)
        canvas.pack()

        # Phone prompt
        phone_prompt_lab_pos_x = phone_window_size.width / 2
        phone_prompt_lab_pos_y = phone_window_size.height / 2
        phone_prompt_lab_font = font.Font(size="30")
        phone_prompt_lab = tk.Label(phone_window, text="将模拟器放置虚线以内")
        phone_prompt_lab.config(bg="systemTransparent", fg="gray", font=phone_prompt_lab_font)
        phone_prompt_lab.place(x=phone_prompt_lab_pos_x, y=phone_prompt_lab_pos_y, anchor="center")
        
        # Operation panel
        op_frame = tk.Frame(self, width=phone_window_size.width, height=phone_window_size.height)
        op_frame.pack(side=tk.LEFT)

        # App options
        options = ("聚看点",)
        self.default_op = tk.StringVar()
        self.default_op.set(options[0])
        app_options = tk.OptionMenu(op_frame, self.default_op, *options)
        app_options.place(x=0, y=0)

        # Buttons container
        btn_frame = tk.Frame(op_frame, width=phone_window_size.width, height=120)
        btn_frame.place(x=0, y=phone_window_size.height, anchor="sw")

        # Buttons
        start_btn_pos_x = phone_window_size.width - 50
        start_btn_pos_y = 50
        start_btn = tk.Button(btn_frame, text="开始", command=self.click_start)
        start_btn.config(anchor="se")
        print("{}-{}".format(start_btn_pos_x, start_btn_pos_y))
        start_btn.place(x=start_btn_pos_x, y=start_btn_pos_y, anchor="se")
        
        stop_btn_pos_x = start_btn_pos_x - 60
        stop_btn_pos_y = start_btn_pos_y
        stop_btn = tk.Button(btn_frame, text="停止", command=self.click_stop)
        stop_btn.place(x=stop_btn_pos_x, y=stop_btn_pos_y, anchor="se")

        # self.hi_there = tk.Button(self)
        # self.hi_there["text"] = "Hello World\n(click me)"
        # self.hi_there["command"] = self.say_hi
        # self.hi_there.pack(side="top")

        # self.quit = tk.Button(self, text="QUIT", fg="red",
        #                       command=root.destroy)
        # self.quit.pack(side="bottom")

    def origin_point(self):
        window_pos = Point(root.winfo_x(), root.winfo_y())
        return window_pos + self.left_top

    def mapreduce(self, config, worker_class, coord_class):
        return worker_class.create_worker(coord_class, config)

    def click_start(self):
        o_pos = self.origin_point()
        print("origin_point: {}".format(o_pos))
        config = {"origin_point": o_pos, "screen_size": phone_size}
        info = workers_map[self.default_op.get()]
        self.worker = self.mapreduce(config, *info)
        self.worker.start()

    def click_stop(self):
        self.worker.stop()


app = Application(master=root)
app.master.geometry("1200x700+10+10")
app.mainloop()
