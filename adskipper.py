import cv2
import numpy as np
import pyautogui
import os
import tkinter.font as tkfont
import tkinter as tk


class YoutubeAdSkipper:
    def __init__(self, threshold=0.7):
        self.threshold = threshold
        self.templates = []
        self.task = None
        self.load_templates()

        self.window = tk.Tk()
        self.window.title('Youtube AD Skipper')
        self.window.geometry('500x500')
        self.window.config(bg='black')

        self.canvas = tk.Canvas(self.window, width=500, height=500)
        self.canvas.pack(fill='both', expand=True)

        self.play_icon = tk.PhotoImage(file='play.png')
        self.stop_icon = tk.PhotoImage(file='stop.png')

        self.window.iconphoto(True, self.play_icon)

        self.window.bind("<Escape>", lambda e: self.window.quit())

        self.create_widgets()

    def create_widgets(self):
        font = tkfont.Font(family='Comic Sans MS', size=20, weight='bold')

        img = tk.PhotoImage(file='YoutubeLogo.png')
        self.canvas.create_image(140, 100, image=img, anchor="nw")

        self.canvas.create_text(240, 50, text='Youtube Ad Skipper',
                                font=font, fill='white')

        play_btn = tk.Button(self.window,
                             command=self.start, width=60, height=60, image=self.play_icon,
                             bg='black', bd=0, activebackground='black')

        stop_btn = tk.Button(self.window,
                             command=self.stop, width=60, height=60, image=self.stop_icon,
                             bg='black', bd=0, activebackground='black')

        btn_canvas = self.canvas.create_window(
            175, 400, anchor="nw", window=play_btn)

        btn_canvas = self.canvas.create_window(
            275, 400, anchor="nw", window=stop_btn)

    def load_templates(self):
        cur_dir_path = os.path.abspath(os.path.dirname(__file__))
        self.templates.append(
            cv2.imread(os.path.join(cur_dir_path, 'template3.png'), 0))
        self.templates.append(
            cv2.imread(os.path.join(cur_dir_path, 'template4.png'), 0))
        self.templates.append(
            cv2.imread(os.path.join(cur_dir_path, 'template5.png'), 0))
        self.templates.append(
            cv2.imread(os.path.join(cur_dir_path, 'template6.png'), 0))

    def start(self):
        im1 = pyautogui.screenshot()
        im1 = np.asarray(im1.convert(mode='L'))
        for template in self.templates:
            res = cv2.matchTemplate(im1, template, cv2.TM_CCOEFF_NORMED)
            loc = np.where(res >= self.threshold)
            if loc[0].size != 0:
                pyautogui.click(list(zip(*loc[::-1]))[0])
        self.task = self.window.after(3000, self.start)

    def stop(self):
        if self.task is not None:
            self.window.after_cancel(self.task)
        else:
            print("Oops, Something Went wrong")

    def run(self):
        self.window.mainloop()


if __name__ == '__main__':
    app = YoutubeAdSkipper()
    app.run()
