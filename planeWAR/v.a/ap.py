import tkinter

if __name__ == '__main__':
    root_window = tkinter.Tk()

    root_window.title('打飞机')# 标题
    root_window.resizable(width=False, height=False)#锁定窗口
    window_canvas = tkinter.Canvas(root_window, width=480, height=600)#定义长宽高
    window_canvas.pack()


    bg_img = tkinter.PhotoImage(file='E:/Python/planeWAR/v.1/images/background.png')

    window_canvas.create_image(240,300,anchor=tkinter.CENTER, image=bg_img, tags='bg')

    bee_img = tkinter.PhotoImage(file='E:/Python/planeWAR/v.1/images/enemy1.png')

    window_canvas.create_image(240,300,anchor=tkinter.CENTER, image=bee_img, tags='bee')

    root_window.mainloop()