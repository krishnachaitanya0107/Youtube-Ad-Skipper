import cv2
import numpy as np
import pyautogui

from tkinter import *
window = Tk()
window.title('Youtube AD Skipper')
window.geometry('500x500')

template3 = cv2.imread('template3.png', 0)
template4 = cv2.imread('template4.png', 0)
template5 = cv2.imread('template5.png', 0)
template6 = cv2.imread('template6.png', 0)
threshold = 0.7
task = []


def start():
    im1 = pyautogui.screenshot()
    im1 = np.asarray(im1.convert(mode='L'))
    res = cv2.matchTemplate(im1, template3, cv2.TM_CCOEFF_NORMED)
    loc = np.where(res >= threshold)
    if(loc[0].size != 0):
        pyautogui.click(list(zip(*loc[::-1]))[0])
    res = cv2.matchTemplate(im1, template4, cv2.TM_CCOEFF_NORMED)
    loc = np.where(res >= threshold)
    if(loc[0].size != 0):
        pyautogui.click(list(zip(*loc[::-1]))[0])
    res = cv2.matchTemplate(im1, template5, cv2.TM_CCOEFF_NORMED)
    loc = np.where(res >= threshold)
    if(loc[0].size != 0):
        pyautogui.click(list(zip(*loc[::-1]))[0])
    res = cv2.matchTemplate(im1, template6, cv2.TM_CCOEFF_NORMED)
    loc = np.where(res >= threshold)
    if(loc[0].size != 0):
        pyautogui.click(list(zip(*loc[::-1]))[0])
    temp = window.after(3000, start)
    if(task != []):
        task.pop()
    task.append(temp)
    print(task)


def stop():
    if(task != []):
        window.after_cancel(task[0])
    else:
        print("Oops,Something Went wrong")


canvas = Canvas(window, width=500, height=500)
canvas.pack(fill='both', expand=True)
canvas.config(bg='white')

img = PhotoImage(file='youtube.png')
canvas.create_image(140, 100, image=img, anchor="nw")

canvas.create_text(240, 50, text='Youtube Ad Skipper', font=('Arial', 10))

b1 = Button(window, text="Start", command=start, width=5, height=1)

b2 = Button(window, text="Stop", command=stop, width=5, height=1)

btn_canvas = canvas.create_window(175, 400, anchor="nw", window=b1)

btn_canvas = canvas.create_window(275, 400, anchor="nw", window=b2)

window.mainloop()
