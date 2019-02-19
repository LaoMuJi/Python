import tkinter
import time
import random as rd


step = (0,10)
direciton = (1,1)

x=0
y=10

def set_right(e):
    global x
    x -= 20

def set_left(e):
    global x
    x -= 20

root_window = tkinter.Tk()
root_window.title('飞机大战')


#绑定按键左右
root_window.bind('<Key-Left>', set_left)
root_window.bind('<Key-Right>', set_right)

root_window.resizable(width=False, height=False)

#创建画布
window_canvas = tkinter.Canvas(root_window, width=480,height=600)
window_canvas.pack()

def main():
    # 创建 开始界面
    bg_img = tkinter.PhotoImage(file='E:/Python/planeWAR/v.1/images/background.png')

    window_canvas.create_image(240, 300, anchor=tkinter.CENTER, image=bg_img, tags='bg')

    bee_img = tkinter.PhotoImage(file='E:/Python/planeWAR/v.1/images/enemy1.png')

    window_canvas.create_image(240, 300, anchor=tkinter.CENTER, image=bee_img, tags='bee')




root_window.mainloop()







