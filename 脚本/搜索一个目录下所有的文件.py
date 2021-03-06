#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 4.12
# In conjunction with Tcl version 8.6
#    Dec 27, 2019 09:25:12 AM
import builtins
import os
import time
from shutil import copyfile
from tkinter.filedialog import askdirectory
from tkinter.scrolledtext import ScrolledText


try:
    from Tkinter import *
except ImportError:
    from tkinter import *

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True


from os.path import isdir
from threading import Thread


warning_message = ''


def myprint(*args,**kwargs):
    return builtins.print(*args,**kwargs)


print=myprint


def get_items(path, direct_file, pattern, level=0,subindex=''):
    '''
    :param path: 文件路径，输入要处理的文件夹
    :param direct_file: 用于把找到的文件存起来的路径
    :param level: 递归层级
    :param subindex: 序号
    :return: 该文件自己的编号
    '''
    global listnum,warning_message
    if level == 0:
        listnum = 0
        direct_file = os.path.join(direct_file,'target_file')
        if not os.path.exists(direct_file):
            os.mkdir(direct_file)
    dirs = os.listdir(path) #获取所有的子文件夹和子文件
    subpath = [os.path.join(path, dir) for dir in dirs] #得到所有的地址
    if  (os.path.abspath(direct_file) in subpath):#把我们要搜索的目录中去掉用来存放目标文件的文件夹

        subpath.remove(os.path.abspath(direct_file))

    for index,each_item in enumerate(subpath):
        if isdir(each_item):
            kwargs = {
                'path':each_item,
                'pattern':pattern,
                'direct_file':direct_file,
                'level':level+1,
                'subindex':subindex+str(index)+'.',

            }
            Mythread = Thread(target=get_items,kwargs=kwargs)
            Mythread.start()
            Mythread.join()
            # get_items(each_item,pattern=pattern,direct_file=direct_file, level=level+1,subindex = subindex+str(index)+'.')

        else:
            basename = os.path.basename(each_item)#文件的名字

            # ^ \w + (\.pdf)$
            if re.fullmatch(pattern,basename) is not None:
                # 匹配以 .pdf结尾的所有文件
                # newname = str(listnum)+'_'+basename
                newname = str(listnum+146)+'.jpg'
                # 重命名可以重写
                direct_file_name = os.path.join(direct_file,newname)
                if not os.path.exists(direct_file_name):
                    copyfile(each_item,direct_file_name)
                    warning_message = '正在复制%s...\n' % basename
                    print('正在复制%s...' % basename)
                else:
                    warning_message = '%s已存在,已经跳过...\n'% newname
                    print('%s已存在,已经跳过...'% newname)
                    pass
                listnum+=1
    if level ==0:

        warning_message = '复制结束,共执行了{}个文件。\n'.format(listnum)
        print('复制结束,共复制{}个文件。'.format(listnum))
        pass





def set_Tk_var():
    global path,direct_file,repattern,pattern,outputmessage,old_warning_message
    path = StringVar(value='')
    direct_file = StringVar(value='')
    pattern = StringVar(value='')
    repattern = StringVar(value='')
    outputmessage = StringVar(value='欢迎使用！'
                                    '请输入查询路径，目标路径，'
                                    '后缀名匹配和正则匹配填一个即可，优先使用正则匹配。\n')
    old_warning_message = ''


def init(top, gui, *args, **kwargs):
    global w, top_level, root
    w = gui
    top_level = top
    root = top

def destroy_window():
    # Function which closes the window.
    global top_level
    top_level.destroy()
    top_level = None

def start():
    global warning_message
    print('按下了确认按钮')
    finalpattern = ''
    inputpath = path.get()
    outputpath = direct_file.get()
    inputrepattern = repattern.get()
    inputpattern = pattern.get()
    if inputrepattern != '':
        finalpattern = inputrepattern
        print(finalpattern)
    else:
        if inputpattern != '':
            finalpattern = '\S+'+inputpattern
            print(finalpattern)
        else:
            print('3',inputrepattern,inputpattern)
    print(all([inputpath, outputpath,finalpattern]))
    if all([inputpath, outputpath,finalpattern]):
        get_items(path=inputpath, direct_file=outputpath, pattern=finalpattern)
    else:
        warning_message = '请输入必要的查询参数。\n'
    sys.stdout.flush()

def selectpath():
    path_ = askdirectory()
    path.set(path_)

def selectpath2():
    path_ = askdirectory()
    direct_file.set(path_)



def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = Tk()



    set_Tk_var()
    top = New_Toplevel(root)

    def renewmessage():
        global old_warning_message, warning_message
        while True:
            time.sleep(0.1)
            if old_warning_message != warning_message:
                old_warning_message = warning_message
                top.Scrolledtext1.configure(state=NORMAL)
                top.Scrolledtext1.insert(END, warning_message)
                top.Scrolledtext1.configure(state=DISABLED)
    setwarning_message = Thread(target=renewmessage,daemon=True)
    setwarning_message.start()
    init(root, top)
    root.mainloop()

w = None
def create_New_Toplevel(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = Toplevel (root)
    set_Tk_var()
    top = New_Toplevel(w)
    init(w, top, *args, **kwargs)
    return (w, top)

def destroy_New_Toplevel():
    global w
    w.destroy()
    w = None


class New_Toplevel:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#d9d9d9' # X11 color: 'gray85'
        font12 = "-family 华文中宋 -size 16 -weight bold -slant roman "  \
            "-underline 0 -overstrike 0"
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.configure('.',font="TkDefaultFont")
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])

        top.geometry("600x450+500+274")
        top.title("欢迎使用！")
        top.configure(background="#d9d9d9")
        # top.iconbitmap('D:\Download\\funny.ico')



        self.Frame1 = Frame(top)
        self.Frame1.place(relx=0.08, rely=0.29, relheight=0.63, relwidth=0.83)
        self.Frame1.configure(relief=GROOVE)
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief=GROOVE)
        self.Frame1.configure(background="#d9d9d9")
        self.Frame1.configure(width=495)

        self.Label1 = Label(self.Frame1)
        self.Label1.place(relx=0.025, rely=0.1, height=23, width=97)
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(text='''查找路径''')
        self.Label1.configure(width=97)

        self.Label1_1 = Label(self.Frame1)
        self.Label1_1.place(relx=0.02, rely=0.24, height=23, width=97)
        self.Label1_1.configure(activebackground="#f9f9f9")
        self.Label1_1.configure(activeforeground="black")
        self.Label1_1.configure(background="#d9d9d9")
        self.Label1_1.configure(disabledforeground="#a3a3a3")
        self.Label1_1.configure(foreground="#000000")
        self.Label1_1.configure(highlightbackground="#d9d9d9")
        self.Label1_1.configure(highlightcolor="black")
        self.Label1_1.configure(text='''目标路径''')

        self.fra38_lab41 = Label(self.Frame1)
        self.fra38_lab41.place(relx=0.02, rely=0.38, height=23, width=97)
        self.fra38_lab41.configure(activebackground="#f9f9f9")
        self.fra38_lab41.configure(activeforeground="black")
        self.fra38_lab41.configure(background="#d9d9d9")
        self.fra38_lab41.configure(disabledforeground="#a3a3a3")
        self.fra38_lab41.configure(foreground="#000000")
        self.fra38_lab41.configure(highlightbackground="#d9d9d9")
        self.fra38_lab41.configure(highlightcolor="black")
        self.fra38_lab41.configure(text='''匹配后缀名''')

        self.fra38_lab42 = Label(self.Frame1)
        self.fra38_lab42.place(relx=0.51, rely=0.38, height=23, width=97)
        self.fra38_lab42.configure(activebackground="#f9f9f9")
        self.fra38_lab42.configure(activeforeground="black")
        self.fra38_lab42.configure(background="#d9d9d9")
        self.fra38_lab42.configure(disabledforeground="#a3a3a3")
        self.fra38_lab42.configure(foreground="#000000")
        self.fra38_lab42.configure(highlightbackground="#d9d9d9")
        self.fra38_lab42.configure(highlightcolor="black")
        self.fra38_lab42.configure(text='''正则匹配''')

        self.start = Button(self.Frame1)
        self.start.place(relx=0.38, rely=0.82, height=38, width=131)
        self.start.configure(activebackground="#d9d9d9")
        self.start.configure(activeforeground="#000000")
        self.start.configure(background="#d9d9d9")
        self.start.configure(command=start)
        self.start.configure(disabledforeground="#a3a3a3")
        self.start.configure(foreground="#000000")
        self.start.configure(highlightbackground="#d9d9d9")
        self.start.configure(highlightcolor="black")
        self.start.configure(pady="0")
        self.start.configure(text='''开始''')
        self.start.configure(width=131)

        self.SearchPathInput = Entry(self.Frame1)
        self.SearchPathInput.place(relx=0.26, rely=0.08, height=27
                , relwidth=0.52)
        self.SearchPathInput.configure(background="white")
        self.SearchPathInput.configure(disabledforeground="#a3a3a3")
        self.SearchPathInput.configure(font="TkFixedFont")
        self.SearchPathInput.configure(foreground="#000000")
        self.SearchPathInput.configure(insertbackground="black")
        self.SearchPathInput.configure(textvariable=path)
        self.SearchPathInput.configure(width=334)

        self.pathselect = Button(self.Frame1)
        self.pathselect.place(relx=0.80, rely=0.08, height=27
                , relwidth=0.12)
        self.pathselect.configure(activebackground="#d9d9d9")
        self.pathselect.configure(activeforeground="#000000")
        self.pathselect.configure(background="#d9d9d9")
        self.pathselect.configure(command=selectpath)

        self.pathselect.configure(disabledforeground="#a3a3a3")
        self.pathselect.configure(foreground="#000000")
        self.pathselect.configure(highlightbackground="#d9d9d9")
        self.pathselect.configure(highlightcolor="black")
        self.pathselect.configure(pady="0")
        self.pathselect.configure(text='''路径选择''')
        self.pathselect.configure(width=131)


        self.LastPatternInput = Entry(self.Frame1)
        self.LastPatternInput.place(relx=0.26, rely=0.37, height=27
                , relwidth=0.25)
        self.LastPatternInput.configure(background="white")
        self.LastPatternInput.configure(disabledforeground="#a3a3a3")
        self.LastPatternInput.configure(font="TkFixedFont")
        self.LastPatternInput.configure(foreground="#000000")
        self.LastPatternInput.configure(highlightbackground="#d9d9d9")
        self.LastPatternInput.configure(highlightcolor="black")
        self.LastPatternInput.configure(insertbackground="black")
        self.LastPatternInput.configure(selectbackground="#c4c4c4")
        self.LastPatternInput.configure(selectforeground="black")
        self.LastPatternInput.configure(textvariable=pattern)
        self.LastPatternInput.configure(width=124)

        self.StorePathInput = Entry(self.Frame1)
        self.StorePathInput.place(relx=0.26, rely=0.22,height=27, relwidth=0.52)
        self.StorePathInput.configure(background="white")
        self.StorePathInput.configure(disabledforeground="#a3a3a3")
        self.StorePathInput.configure(font="TkFixedFont")
        self.StorePathInput.configure(foreground="#000000")
        self.StorePathInput.configure(highlightbackground="#d9d9d9")
        self.StorePathInput.configure(highlightcolor="black")
        self.StorePathInput.configure(insertbackground="black")
        self.StorePathInput.configure(selectbackground="#c4c4c4")
        self.StorePathInput.configure(selectforeground="black")
        self.StorePathInput.configure(textvariable=direct_file)
        self.StorePathInput.configure(width=334)


        self.pathselect2 = Button(self.Frame1)
        self.pathselect2.place(relx=0.80, rely=0.22, height=27
                , relwidth=0.12)
        self.pathselect2.configure(activebackground="#d9d9d9")
        self.pathselect2.configure(activeforeground="#000000")
        self.pathselect2.configure(background="#d9d9d9")
        self.pathselect2.configure(command=selectpath2)
        self.pathselect2.configure(disabledforeground="#a3a3a3")
        self.pathselect2.configure(foreground="#000000")
        self.pathselect2.configure(highlightbackground="#d9d9d9")
        self.pathselect2.configure(highlightcolor="black")
        self.pathselect2.configure(pady="0")
        self.pathselect2.configure(text='''路径选择''')
        self.pathselect2.configure(width=131)


        self.ReInput = Entry(self.Frame1)
        self.ReInput.place(relx=0.68, rely=0.37,height=27, relwidth=0.23)
        self.ReInput.configure(background="white")
        self.ReInput.configure(disabledforeground="#a3a3a3")
        self.ReInput.configure(font="TkFixedFont")
        self.ReInput.configure(foreground="#000000")
        self.ReInput.configure(highlightbackground="#d9d9d9")
        self.ReInput.configure(highlightcolor="black")
        self.ReInput.configure(insertbackground="black")
        self.ReInput.configure(selectbackground="#c4c4c4")
        self.ReInput.configure(selectforeground="black")
        self.ReInput.configure(textvariable=repattern)
        self.ReInput.configure(width=114)

        self.TLabel1 = ttk.Label(top)
        self.TLabel1.place(relx=0.1, rely=0.11, height=31, width=489)
        self.TLabel1.configure(background="#d9d9d9")
        self.TLabel1.configure(foreground="#000000")
        self.TLabel1.configure(font=font12)
        self.TLabel1.configure(relief=FLAT)
        self.TLabel1.configure(anchor=N)
        self.TLabel1.configure(text='''搜索一个目录下所有的文件''')
        self.TLabel1.configure(width=489)

        self.Label2 = Label(top)
        self.Label2.place(relx=0.75, rely=0.2, height=23, width=87)
        self.Label2.configure(background="#d9d9d9")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(text='''作者：高凡启''')
        self.Label2.configure(width=87)

        self.Label2 = Label(self.Frame1)
        self.Label2.place(relx=0.035, rely=0.605, height=23, width=87)
        self.Label2.configure(background="#d9d9d9")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(text='''输出信息''')
        self.Label2.configure(width=146)



        self.Scrolledtext1 = ScrolledText(top)
        self.Scrolledtext1.place(relx=0.30, rely=0.605, relheight=0.18, relwidth=0.54)
        self.Scrolledtext1.configure(background="white")
        self.Scrolledtext1.configure(font="TkTextFont")
        self.Scrolledtext1.configure(foreground="black")
        self.Scrolledtext1.configure(highlightbackground="#d9d9d9")
        self.Scrolledtext1.configure(highlightcolor="black")
        self.Scrolledtext1.configure(insertbackground="black")
        self.Scrolledtext1.configure(insertborderwidth="3")
        self.Scrolledtext1.configure(selectbackground="#c4c4c4")
        self.Scrolledtext1.configure(selectforeground="black")
        self.Scrolledtext1.insert(END,outputmessage.get())
        self.Scrolledtext1.configure(state=DISABLED)
        self.Scrolledtext1.configure(width=100)


vp_start_gui()



