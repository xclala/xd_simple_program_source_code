from tkinter import *
try:
    from tkinter.scrolledtext import ScrolledText

    def search():
        from webbrowser import open
        open("https://baike.baidu.com/item/"+wangzhi.get())

    def setting_button():
        Button(text=m.get(), command=search).pack(side=RIGHT)

    top = Tk()
    top.title("浏览器")
    top.geometry('1500x30')
    wangzhi = Entry()
    m = Entry(bg='black', fg='white')
    Label(text='请输入内容：').pack(side=LEFT)
    wangzhi.pack(side=LEFT, expand=True, fill=X)
    Label(text='请输入临时收藏名：', bg='black', fg='white').pack(side=LEFT)
    m.pack(side=LEFT, expand=True, fill=X)
    Button(text='临时收藏', command=setting_button, bg='black',
           fg='white').pack(side=RIGHT)
    Button(text='进入词条', command=search).pack(side=RIGHT)
    mainloop()
except:
    pass