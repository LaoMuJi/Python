from tkinter import *

root = Tk()

#定义面板的大小
root.geometry('250x380')

root.title('杀熊')

#定义面板 bg是背景色
frame_show = Frame(width=300,height=150,bg='#dddddd')

frame_show.pack()

#定义顶部区域
sv = StringVar()
sv.set('0')

# anchor:定义控件的锚点，e代表右边，font代表字体
show_label = Label(frame_show, textvariable=sv, bg = 'green', width=12, height=1,\
                   font=('黑体',20,'bold'), justify=LEFT, anchor='e')
show_label.pack(padx=10, pady=10)


def delete():
    print('del')

#按键区域
frame_bord = Frame(width=400, height=350, bg="#cccccc")
b_del = Button(frame_bord, text='←', width=5, height=1,\
               command=delete)
b_del.grid(row=0,column=0)


def change(num):
    print(num)


def operation(op):
    print(op)


b_1 = Button(frame_bord, text='1', width=5, height=2, \
             command=lambda: change("1"))
b_1.grid(row=1, column=0)



b_jia = Button(frame_bord, text='+',width=5, height=2,\
               command=lambda:operation("+"))
b_jia.grid(row=2, column=0)

frame_bord.pack(padx=10,pady=10)

root.mainloop()
