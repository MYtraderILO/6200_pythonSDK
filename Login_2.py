import pickle
import tradeplantform as trd
import tkinter as tk
import ttkbootstrap as ttk
from tkinter import messagebox
from ttkbootstrap.constants import *

class login(object):
    def __init__(self, master=None):
        self.root = master  # 定义内部变量root
        self.root.geometry('600x400+222+111')
        self.root.title('Login')
        self.creatlogin()

    def creatlogin(self):
        self.fr1 = tk.Frame(self.root)
        self.fr1.pack()
        new_name = tk.StringVar()  # 将输入的注册名赋值给变量
        new_name.set('@Meta.com')
        tk.Label(self.fr1, text='Login', font=('microsoft yahei', 20, 'bold')).grid(row=0, columnspan=2)
        self.lab1 = tk.Label(self.fr1, text='User Account: ')
        self.lab1.grid(row=1, column=0, pady=40)
        self.en2 = tk.Entry(self.fr1, textvariable=new_name)
        self.en2.grid(row=1, column=1, pady=40)
        self.lab1 = tk.Label(self.fr1, text='User Password: ')
        self.lab1.grid(row=2, column=0, pady=15)
        self.en1 = tk.Entry(self.fr1)
        self.en1.grid(row=2, column=1, pady=15)

        self.but1 = ttk.Button(self.fr1, text="Login",bootstyle=(INFO,OUTLINE),command=self.usr_log_in)
        self.but1.grid(row=3, column=0, pady=20)

        self.but2 = ttk.Button(self.fr1, text="Sign up", bootstyle=(SUCCESS),command=self.usr_sign_up)
        self.but2.grid(row=3, column=1, pady=20)
        self.en1.focus_set()  # 获得焦点

    def usr_log_in(self):
        user_name = self.en2.get()
        user_name = user_name if '@Meta.com' in user_name else user_name + '@Meta.com'
        user_password = self.en1.get()
        # 这里设置异常捕获，当我们第一次访问用户信息文件时是不存在的，所以这里设置异常捕获。
        # 中间的两行就是我们的匹配，即程序将输入的信息和文件中的信息匹配。
        try:
            with open('usrs_info.pickle', 'rb') as usr_file:
                usrs_info = pickle.load(usr_file)
        except FileNotFoundError:
            # 这里就是我们在没有读取到`usr_file`的时候，程序会创建一个`usr_file`这个文件，并将管理员
            # 的用户和密码写入，即用户名为`admin`密码为`admin`。
            with open('usrs_info.pickle', 'wb') as usr_file:
                usrs_info = {'admin': 'Xuqiwei8'}
                pickle.dump(usrs_info, usr_file)
                usr_file.close()  # 必须先关闭，否则pickle.load()会出现EOFError: Ran out of input
        #
        #     # 如果用户名和密码与文件中的匹配成功，则会登录成功，并跳出弹窗how are you? 加上你的用户名。
        if user_name in usrs_info:
            # print(usrs_info[user_name])
            if user_password == usrs_info[user_name]:
                messagebox.showinfo(title='Welcome', message='Login in')
                self.fr1.destroy()  # 登录界面卸载
                home(self.root)  # 密码对，就把主窗体模块的界面加载
            # 如果用户名匹配成功，而密码输入错误，则会弹出'Error, your password is wrong, try again.'
            else:
                messagebox.showerror(message='Error, your password is wrong, try again.')
        else:  # 如果发现用户名不存在
            is_sign_up = messagebox.askyesno('Welcome！ ', 'You have not sign up yet. Sign up now?')
            # 提示需不需要注册新用户
            if is_sign_up:
                self.usr_sign_up()

    def usr_sign_up(self):
        def sign_to_Meta_Website():
            # 以下三行就是获取我们注册时所输入的信息
            np = new_pwd.get()
            npf = new_pwd_confirm.get()
            nn = new_name.get()

            # 这里是打开我们记录数据的文件，将注册信息读出
            with open('usrs_info.pickle', 'rb') as usr_file:
                exist_usr_info = pickle.load(usr_file)
            # 这里就是判断，如果两次密码输入不一致，则提示Error, Password and confirm password must be the same!
            if np != npf:
                messagebox.showerror('Error', 'Password and confirm password must be the same!')

            # 如果用户名已经在我们的数据文件中，则提示Error, The user has already signed up!
            elif nn in exist_usr_info:
                messagebox.showerror('Error', 'The user has already signed up!')

            # 最后如果输入无以上错误，则将注册输入的信息记录到文件当中，并提示注册成功Welcome！,You have successfully signed up!，然后销毁窗口。
            else:
                exist_usr_info[nn] = np
                with open('usrs_info.pickle', 'wb') as usr_file:
                    pickle.dump(exist_usr_info, usr_file)
                messagebox.showinfo('Welcome', 'You have successfully signed up!')
                # 然后销毁窗口。
                window_sign_up.destroy()

        # 定义长在窗口上的窗口
        window_sign_up = tk.Toplevel(self.fr1)
        window_sign_up.geometry('600x400+222+111')
        window_sign_up.title('Sign up window')

        new_name = tk.StringVar()  # 将输入的注册名赋值给变量
        new_name.set('@Meta.com')  # 将最初显示定为'example@python.com'
        tk.Label(window_sign_up, text='User name: ').place(x=160, y=100)  # 将`User name:`放置在坐标（10,10）。
        entry_new_name = tk.Entry(window_sign_up, textvariable=new_name)  # 创建一个注册名的`entry`，变量为`new_name`
        entry_new_name.place(x=280, y=100)  # `entry`放置在坐标（150,10）.

        new_pwd = tk.StringVar()
        tk.Label(window_sign_up, text='Password: ').place(x=160, y=140)
        entry_usr_pwd = tk.Entry(window_sign_up, textvariable=new_pwd, show='*')
        entry_usr_pwd.place(x=280, y=140)

        new_pwd_confirm = tk.StringVar()
        tk.Label(window_sign_up, text='Confirm password: ').place(x=160, y=180)
        entry_usr_pwd_confirm = tk.Entry(window_sign_up, textvariable=new_pwd_confirm, show='*')
        entry_usr_pwd_confirm.place(x=280,y=180)

        # 下面的 sign_to_Hongwei_Website
        btn_comfirm_sign_up = ttk.Button(window_sign_up, text='Sign up', command=sign_to_Meta_Website)
        btn_comfirm_sign_up.place(x=260, y=240)


class home():
    def __init__(self, master=None):
        self.root = master
        self.root.geometry('600x400+222+111')
        self.jobtxt = ''  # 用这个变量记下窗体的标题
        self.createPage()

    def createPage(self):

        menubar = tk.Menu(self.root)
        A = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label='Operation', menu=A)
        A.add_command(label='Get Receipt Trace', command=self.get_receipt_trace)
        A.add_command(label='Create Receipts', command=self.get_create_receipt)
        # A.add_command(label='工资管理', command=self.gotogong)
        # A.add_command(label='关于',command=self.about)
        A.add_command(label='About', command=about)
        A.add_command(label='Account Management', command=self.User_info)
        A.add_command(label='Exit', command=self.root.destroy)

        self.root.config(menu=menubar)

        self.get_receipt_trace()

    def User_info(self):
        if self.jobtxt != 'User_info':  # 根据窗体标题来决定否则执行这个菜单功能
            if self.jobtxt == 'Creat Receipt':  # 如果要切换，就先根据窗体标签把现在的框架卸载掉
                self.create_receipt_page.destroy()
            if self.jobtxt == 'Get Receipt Trace':
                self.get_Receipt_page.destroy()

            self.userpage = userInfo(self.root)  # 调用job.py的ren类，显示人事管理界面
            self.userpage.pack()
            self.root.title('User information')
            self.jobtxt = 'User_info'  # 记下窗体标题

    def get_receipt_trace(self):  # 执行人员管理菜单
        if self.jobtxt != 'Get Receipt Trace':  # 根据窗体标题来决定否则执行这个菜单功能
            if self.jobtxt == 'Creat Receipt':  # 如果要切换，就先根据窗体标签把现在的框架卸载掉
                self.create_receipt_page.destroy()
            if self.jobtxt == '工资管理':  # 如果要切换，就先根据窗体标签把现在的框架卸载掉
                self.gongpage.destroy()
            if self.jobtxt == 'User_info':
                self.userpage.destroy()

            self.get_Receipt_page = getReceiptTrace(self.root)  # 调用job.py的ren类，显示人事管理界面
            self.get_Receipt_page.pack()
            self.root.title('Get Receipt Trace')
            self.jobtxt = 'Get Receipt Trace'  # 记下窗体标题

    def get_create_receipt(self):  # 执行考勤管理菜单
        if self.jobtxt != 'Creat Receipt':
            if self.jobtxt == 'Get Receipt Trace':
                self.get_Receipt_page.destroy()
            if self.jobtxt == '工资管理':
                self.gongpage.destroy()
            if self.jobtxt == 'User_info':
                self.userpage.destroy()

            self.create_receipt_page = create_receipt(self.root)
            self.create_receipt_page.pack()
            self.root.title('Creat Receipt')
            self.jobtxt = 'Creat Receipt'

    # def gotogong(self):  # 执行工资管理菜单
    #     if self.jobtxt != '工资管理':
    #         if self.jobtxt == 'Creat Receipt':
    #             self.create_receipt_page.destroy()
    #         if self.jobtxt == 'Get Receipt Trace':
    #             self.get_Receipt_page.destroy()
    #         if self.jobtxt == 'User_info':
    #             self.userpage.destroy()
    #
    #         self.gongpage = gong(self.root)
    #         self.gongpage.pack()
    #         self.root.title('工资管理')
    #         self.jobtxt = '工资管理'

    def about(self):  # 调用job.py里的about函数，弹出窗体
        about()


class getReceiptTrace(tk.Frame):  # 继承Frame类
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.root = master
        self.index = None
        self.dic_info = None
        self.page = None
        self.creatInfo()

    def creatInfo(self):
        la1 = tk.Label(self, text='Get Receipts Trace', font=('microsoft yahei', 20, 'bold'))
        la1.grid(row=0, columnspan=2)
        txt1 = tk.Label(self, text='Receipt Id :')
        txt1.grid(row=1, column=0, pady=20)
        self.en1 = tk.Entry(self, text='Get Receipts Trace')
        self.en1.grid(row=1, column=1, pady=20)
        self.bt1 = ttk.Button(self, text='Look up', command=self.cmd_receipt)
        self.bt1.grid(row=2, column=0, pady=20)
        self.bt2 = ttk.Button(self, text='Show Result', command=self.show_result)
        self.bt2.grid(row=2, column=1, pady=20)

    def cmd_receipt(self):
        receipt_id = int(self.en1.get())
        self.index, self.dic_info = trd.getReceiptTraceInfo(receipt_id)
        messagebox.showinfo(title='Results of warehouse receipts', message='A total of {} records'.format(self.index))

    def show_result(self):

        self.page = 1

        def next_info(page):

            if page > self.index:
                messagebox.showerror(title='Error', message="Last Page")
            else:
                tk.Label(window_show_receipt, text='信息: {} \n 操作者地址: {} \n 拥有者信息:{} \n拥有者地址: {} '
                                           '\n 存放仓库id: {} \n货品id: {} \n货品重量: {} \n货品数量: {} \n 质检日期: {}'
                                           ' \n上链时间: {} \n仓单状态:{} \n 其他信息: {}'.format(page, self.dic_info[page]['owner_address'], self.dic_info[page]['owner_id'],
                                                                                      self.dic_info[page]['owner_address'], self.dic_info[page]['settel_Id'],
                                                                                      self.dic_info[page]['commodityId'],
                                                                                      self.dic_info[page]['commodityWeight'],
                                                                                      self.dic_info[page]['commodityAmount'],
                                                                                      self.dic_info[page]['quality_date'],
                                                                                      self.dic_info[page]['list_date'],
                                                                                      self.dic_info[page]['sting_info'],
                                                                                      self.dic_info[page]['receipt_state'])).place(x=10, y=10)
                self.page += 1
                tk.Label(window_show_receipt, text='page: {} / {}'.format(self.page, self.index)).place(x=300, y=300)

        def last_info(page):

            if page <= 0:
                messagebox.showerror(title='Error', message="First Page")
            else:
                tk.Label(window_show_receipt, text='信息: {} \n 操作者地址: {} \n 拥有者信息:{} \n拥有者地址: {} '
                                           '\n 存放仓库id: {} \n货品id: {} \n货品重量: {} \n货品数量: {} \n 质检日期: {}'
                                           ' \n上链时间: {} \n仓单状态:{} \n 其他信息: {}'.format(page, self.dic_info[page]['owner_address'], self.dic_info[page]['owner_id'],
                                                                                      self.dic_info[page]['owner_address'], self.dic_info[page]['settel_Id'],
                                                                                      self.dic_info[page]['commodityId'],
                                                                                      self.dic_info[page]['commodityWeight'],
                                                                                      self.dic_info[page]['commodityAmount'],
                                                                                      self.dic_info[page]['quality_date'],
                                                                                      self.dic_info[page]['list_date'],
                                                                                      self.dic_info[page]['sting_info'],
                                                                                      self.dic_info[page]['receipt_state'])).place(x=10, y=10)

                self.page -= 1
                tk.Label(window_show_receipt, text='page: {} / {}'.format(self.page, self.index)).place(x=300, y=300)

        if self.dic_info is None:
            messagebox.showerror(title='Results of warehouse receipts', message='No results')
        else:
            window_show_receipt = tk.Toplevel(self)
            window_show_receipt.geometry('600x400+222+111')
            window_show_receipt.title('Results Information')


            tk.Label(window_show_receipt, text='信息: {} \n 操作者地址: {} \n 拥有者信息:{} \n拥有者地址: {} '
                                       '\n 存放仓库id: {} \n货品id: {} \n货品重量: {} \n货品数量: {} \n 质检日期: {}'
                                       ' \n上链时间: {} \n仓单状态:{} \n 其他信息: {}'.format(self.page, self.dic_info[self.page]['owner_address'], self.dic_info[self.page]['owner_id'],
                                                                                  self.dic_info[self.page]['owner_address'], self.dic_info[self.page]['settel_Id'],
                                                                                  self.dic_info[self.page]['commodityId'],
                                                                                  self.dic_info[self.page]['commodityWeight'],
                                                                                  self.dic_info[self.page]['commodityAmount'],
                                                                                  self.dic_info[self.page]['quality_date'],
                                                                                  self.dic_info[self.page]['list_date'],
                                                                                  self.dic_info[self.page]['sting_info'],
                                                                                  self.dic_info[self.page]['receipt_state'])).place(x=10, y=10)



            button_next = ttk.Button(window_show_receipt, text='Next', command=lambda: next_info(self.page + 1))
            button_next.place(x=350, y=250)
            button_before = ttk.Button(window_show_receipt, text='Before', command=lambda: last_info(self.page - 1))
            button_before.place(x=250, y=250)

            tk.Label(window_show_receipt, text='page: {} / {}'.format(self.page, self.index)).place(x=300, y=300)

class create_receipt(tk.Frame):

    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.root = master
        self.creat_UI()

    def creat_UI(self):
        tk.Label(self, text='Create Receipts Functions ', font=('microsoft yahei', 20, 'bold')).grid(row=0, columnspan=2)

        tk.Label(self, text='Receipt ID: ').grid(row=1, column=0)
        self.entry_receipt_id = tk.Entry(self)
        self.entry_receipt_id.grid(row=1, column=1)

        tk.Label(self, text='Owner Address: ').grid(row=2, column=0)
        self.entry_ownerAddress = tk.Entry(self)
        self.entry_ownerAddress.grid(row=2, column=1)

        tk.Label(self, text='Commodity Id: ').grid(row=3, column=0)
        self.entry_Commodity_id = tk.Entry(self)
        self.entry_Commodity_id.grid(row=3, column=1)

        tk.Label(self, text='Commodity Weight: ').grid(row=4, column=0)
        self.entry_commodity_weight = tk.Entry(self)
        self.entry_commodity_weight.grid(row=4, column=1)

        tk.Label(self, text='Commodity Amount: ').grid(row=5, column=0)
        self.entry_commodityAmount = tk.Entry(self)
        self.entry_commodityAmount.grid(row=5, column=1)

        tk.Label(self, text='Settel Id: ').grid(row=6, column=0)
        self.entry_settelId = tk.Entry(self)
        self.entry_settelId.grid(row=6, column=1)

        tk.Label(self, text='Quality Date: ').grid(row=7, column=0)
        self.entry_qualityDate = tk.Entry(self)
        self.entry_qualityDate.grid(row=7, column=1)

        new_create = tk.StringVar()  # 将输入的注册名赋值给变量
        new_create.set('First Create Receipts')  # 将最初显示定为'example@python.com'
        tk.Label(self, text='Other Info: ').grid(row=8, column=0)
        self.entry_other_Info = tk.Entry(self, textvariable=new_create)
        self.entry_other_Info.grid(row=8, column=1)

        ttk.Button(self, text='Create', command=self.sendCreation).grid(row=9, column=1)

    def sendCreation(self):

        entry_receipt_id = self.entry_receipt_id.get()
        entry_ownerAddress = self.entry_ownerAddress.get()
        entry_Commodity_id = self.entry_Commodity_id.get()
        entry_commodity_weight = self.entry_commodity_weight.get()
        entry_commodityAmount = self.entry_commodityAmount.get()
        entry_settelId = self.entry_settelId.get()
        entry_qualityDate = self.entry_qualityDate.get()
        entry_other_Info = self.entry_other_Info.get()

        result = trd.createNewReceipt([int(entry_receipt_id), str(entry_ownerAddress), int(entry_Commodity_id), int(entry_commodity_weight),
                              int(entry_commodityAmount), int(entry_settelId), int(entry_qualityDate), str(entry_other_Info)])
        if result[0] == 1:
            messagebox.showinfo(title='Create Result', message='Successfully create receipts \n Receipt ID : {}'.format(entry_receipt_id))
        elif result[0] == -1 and result[1] == -1:
            messagebox.showerror(title='Create Result', message='Fail to create receipts \n Receipt ID : {}'.format(entry_receipt_id))

        elif result[0] == 0:
            messagebox.showerror(title='Create Result', message='Fail to create receipts \n Receipt ID : {} \n{} \n{} \n{}'.format(entry_receipt_id, result[1][0], result[1][1], result[1][2]))

class userInfo(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.root = master
        self.creat_UI()

    def creat_UI(self):
        la1 = tk.Label(self, text='User Information')
        la1.pack()

class change_(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.root = master
        self.creat_UI()

    def creat_UI(self):
        la1 = tk.Label(self, text='User Information')
        la1.pack()

def about():
    top1 = tk.Toplevel()
    top1.geometry('600x400+222+111')
    top1.title('About')

    la1 = tk.Label(top1, text='Meta Digital Receipt System')
    la1.pack(pady=10)
    la2 = tk.Label(top1, text='Contact with us: +852 110')
    la2.pack(pady=10)
    but1 = ttk.Button(top1, text="  O K  ", command=top1.destroy)
    but1.pack(side=BOTTOM, pady=10)

    top1.attributes("-toolwindow", 1)  # 无最大化，最小化
    top1.transient()  # 窗口只置顶root之上
    top1.resizable(False, False)  # 不可调节窗体大小
    top1.grab_set()  # 转化模式
    top1.focus_force()  # 得到焦点


root = tk.Tk()
login(root)  # 登录界面类的实例化
root.mainloop()
