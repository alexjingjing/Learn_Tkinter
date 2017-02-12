# -*- coding:utf-8 -*-
__author__ = 'liusiming'

from Tkinter import *  # 导入 Tkinter 库

# root = Tk()  # 创建窗口对象的背景色
#
# MainLabel=Label(root,text="I am so ugly. -- Tkinter",font="Times 16 bold")  #创建元件
# MainLabel.pack()  #显示元件
# root.mainloop()  #进入窗体的主循环

root = Tk()
first_label = Label(root, text="First:")
first_label.grid(row=0, sticky=W)
first_label = Label(root, text="Second:")
first_label.grid(row=1, sticky=W)

e1 = Entry(root)
e2 = Entry(root)
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

root.mainloop()

# class App:
#     def __init__(self, master):
#         frame = Frame(master)
#         frame.pack()
#
#         self.button = Button(
#             frame, text="QUIT", fg="red", command=frame.quit
#         )
#         self.button.pack(side=LEFT)
#
#         self.hi_there = Button(frame, text="Hello", command=self.say_hi)
#         self.hi_there.pack(side=LEFT)
#
#     def say_hi(self):
#         print "hi there, everyone!"
#
#
# root = Tk()
#
# app = App(root)
#
# root.mainloop()
# root.destroy()  # optional; see description below

# # 创建两个列表
# li = ['C', 'python', 'php', 'html', 'SQL', 'java']
# movie = ['CSS', 'jQuery', 'Bootstrap']
# listb = Listbox(root)  # 创建两个列表组件
# listb2 = Listbox(root)
# for item in li:  # 第一个小部件插入数据
# listb.insert(0, item)
#
# for item in movie:  # 第二个小部件插入数据
#     listb2.insert(0, item)
#
# listb.pack()  # 将小部件放置到主窗口中
# listb2.pack()
# root.mainloop()  # 进入消息循环
