import pickle

import pandas as pd
import time
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

        self.but1 = ttk.Button(self.fr1, text="Login", bootstyle=(INFO, OUTLINE), command=self.usr_log_in)
        self.but1.grid(row=3, column=0, pady=20)

        self.but2 = ttk.Button(self.fr1, text="Sign up", bootstyle=(INFO, OUTLINE), command=self.usr_sign_up)
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
        entry_usr_pwd_confirm.place(x=280, y=180)

        # 下面的 sign_to_Hongwei_Website
        btn_comfirm_sign_up = ttk.Button(window_sign_up, text='Sign up',bootstyle=(INFO, OUTLINE),command=sign_to_Meta_Website)
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
        A.add_command(label='Split Receipts', command=self.split_receipt)
        A.add_command(label='Ask and Bid', command=self.ask_bid)
        A.add_command(label='About', command=about)
        A.add_command(label='Exit', command=self.root.destroy)

        self.root.config(menu=menubar)

        self.get_receipt_trace()

    def ask_bid(self):
        if self.jobtxt != 'ask_bid':  # 根据窗体标题来决定否则执行这个菜单功能
            if self.jobtxt == 'Creat Receipt':  # 如果要切换，就先根据窗体标签把现在的框架卸载掉
                self.create_receipt_page.destroy()
            if self.jobtxt == 'Get Receipt Trace':
                self.get_Receipt_page.destroy()
            if self.jobtxt == 'Split Receipt':
                self.split_receipt_page.destroy()

            self.askpage = ask_bid(self.root)  # 调用job.py的ren类，显示人事管理界面
            self.askpage.pack()
            self.root.title('Ask and Bid function')
            self.jobtxt = 'ask_bid'  # 记下窗体标题

    def get_receipt_trace(self):  # 执行人员管理菜单
        if self.jobtxt != 'Get Receipt Trace':  # 根据窗体标题来决定否则执行这个菜单功能
            if self.jobtxt == 'Creat Receipt':  # 如果要切换，就先根据窗体标签把现在的框架卸载掉
                self.create_receipt_page.destroy()
            if self.jobtxt == 'Split Receipt':
                self.split_receipt_page.destroy()
            if self.jobtxt == 'ask_bid':
                self.askpage.destroy()

            self.get_Receipt_page = getReceiptTrace(self.root)  # 调用job.py的ren类，显示人事管理界面
            self.get_Receipt_page.pack()
            self.root.title('Get Receipt Trace')
            self.jobtxt = 'Get Receipt Trace'  # 记下窗体标题

    def get_create_receipt(self):  # 执行考勤管理菜单
        if self.jobtxt != 'Creat Receipt':
            if self.jobtxt == 'Get Receipt Trace':
                self.get_Receipt_page.destroy()
            if self.jobtxt == 'Split Receipt':
                self.split_receipt_page.destroy()
            if self.jobtxt == 'ask_bid':
                self.askpage.destroy()

            self.create_receipt_page = create_receipt(self.root)
            self.create_receipt_page.pack()
            self.root.title('Creat Receipt')
            self.jobtxt = 'Creat Receipt'

    def split_receipt(self):
        if self.jobtxt != 'Split Receipt':
            if self.jobtxt == 'Get Receipt Trace':
                self.get_Receipt_page.destroy()
            if self.jobtxt == 'Creat Receipt':
                self.create_receipt_page.destroy()
            if self.jobtxt == 'ask_bid':
                self.askpage.destroy()

            self.split_receipt_page = splitReceipt(self.root)
            self.split_receipt_page.pack()
            self.root.title('Split Receipt')
            self.jobtxt = 'Split Receipt'

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
        self.bt1 = ttk.Button(self, text='Look up', bootstyle=(INFO, OUTLINE),command=self.cmd_receipt)
        self.bt1.grid(row=2, column=0, pady=20)
        self.bt2 = ttk.Button(self, text='Show Result',bootstyle=(INFO, OUTLINE),command=self.show_result)
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
                tk.Label(window_show_receipt, text='Information: {} \nOperator_Address: {} \nOwner_Id:{} \nOwner_Address: {} '
                                                   '\nSettle_Id: {} \nCommodityId: {} \nCommodityWeight: {} \nCommodityAmount: {} \nQuality_Date: {}'
                                                   ' \nList_Date: {} \nSting_Info: {} \nReceipt_State: {}'.format(page, self.dic_info[page]['operator_address'], self.dic_info[page]['owner_id'],
                                                                                              self.dic_info[page]['owner_address'], self.dic_info[page]['settel_Id'],
                                                                                              self.dic_info[page]['commodityId'],
                                                                                              self.dic_info[page]['commodityWeight'],
                                                                                              self.dic_info[page]['commodityAmount'],
                                                                                              self.dic_info[page]['quality_date'],
                                                                                              self.dic_info[page]['list_date'],
                                                                                              self.dic_info[page]['sting_info'],
                                                                                              self.dic_info[page]['receipt_state']),justify='left').place(x=110, y=10)
                self.page += 1
                tk.Label(window_show_receipt, text='page: {} / {}'.format(self.page, self.index)).place(x=260, y=300)

        def last_info(page):

            if page <= 0:
                messagebox.showerror(title='Error', message="First Page")
            else:
                tk.Label(window_show_receipt, text='Information: {} \nOperator_Address: {} \nOwner_Id:{} \nOwner_Address: {} '
                                                   '\nSettle_Id: {} \nCommodityId: {} \nCommodityWeight: {} \nCommodityAmount: {} \nQuality_Date: {}'
                                                   ' \nList_Date: {} \nSting_Info: {} \nReceipt_State: {}'.format(page, self.dic_info[page]['operator_address'], self.dic_info[page]['owner_id'],
                                                                                              self.dic_info[page]['owner_address'], self.dic_info[page]['settel_Id'],
                                                                                              self.dic_info[page]['commodityId'],
                                                                                              self.dic_info[page]['commodityWeight'],
                                                                                              self.dic_info[page]['commodityAmount'],
                                                                                              self.dic_info[page]['quality_date'],
                                                                                              self.dic_info[page]['list_date'],
                                                                                              self.dic_info[page]['sting_info'],
                                                                                              self.dic_info[page]['receipt_state']),justify='left').place(x=110, y=10)

                self.page -= 1
                tk.Label(window_show_receipt, text='page: {} / {}'.format(self.page, self.index)).place(x=260, y=300)

        if self.dic_info is None:
            messagebox.showerror(title='Results of warehouse receipts', message='No results')
        else:
            window_show_receipt = tk.Toplevel(self)
            window_show_receipt.geometry('600x400+222+111')
            window_show_receipt.title('Results Information')

            tk.Label(window_show_receipt, text='Information: {} \nOperator_Address: {} \nOwner_Id:{} \nOwner_Address: {} '
                                                   '\nSettle_Id: {} \nCommodityId: {} \nCommodityWeight: {} \nCommodityAmount: {} \nQuality_Date: {}'
                                                   ' \nList_Date: {} \nSting_Info: {} \nReceipt_State: {}'.format(self.page, self.dic_info[self.page]['operator_address'], self.dic_info[self.page]['owner_id'],
                                                                                          self.dic_info[self.page]['owner_address'], self.dic_info[self.page]['settel_Id'],
                                                                                          self.dic_info[self.page]['commodityId'],
                                                                                          self.dic_info[self.page]['commodityWeight'],
                                                                                          self.dic_info[self.page]['commodityAmount'],
                                                                                          self.dic_info[self.page]['quality_date'],
                                                                                          self.dic_info[self.page]['list_date'],
                                                                                          self.dic_info[self.page]['sting_info'],
                                                                                          self.dic_info[self.page]['receipt_state']),justify='left').place(x=110, y=10)

            button_next = ttk.Button(window_show_receipt, text='Next',bootstyle=(INFO, OUTLINE),command=lambda: next_info(self.page + 1))
            button_next.place(x=310, y=250)
            button_before = ttk.Button(window_show_receipt, text='Before', bootstyle=(INFO, OUTLINE),command=lambda: last_info(self.page - 1))
            button_before.place(x=210, y=250)

            tk.Label(window_show_receipt, text='page: {} / {}'.format(self.page, self.index)).place(x=260, y=300)


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

        tk.Label(self, text='Settle Id: ').grid(row=6, column=0)
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

        ttk.Button(self, text='Create',bootstyle=(INFO, OUTLINE),command=self.sendCreation).grid(row=9, column=1)

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


class ask_bid(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.page = 1
        self.root = master
        self.creat_UI()

    def creat_UI(self):
        tk.Label(self, text='Ask and Bid Functions ', font=('microsoft yahei', 20, 'bold')).grid(row=0, columnspan=2)
        ttk.Button(self, text='Ask Information', bootstyle=(INFO, OUTLINE),command=self.sendAsk).grid(row=1, column=0, pady=50)
        ttk.Button(self, text='Bid Information', bootstyle=(INFO, OUTLINE),command=self.sendBid).grid(row=1, column=1, pady=50)
        ttk.Button(self, text='Create Ask Order',bootstyle=(INFO, OUTLINE),command=self.createAsk).grid(row=2, column=0, pady=50)
        ttk.Button(self, text='Create Bid Order',bootstyle=(INFO, OUTLINE),command=self.createBid).grid(row=2, column=1, pady=50)

    def sendAsk(self):
        self.page = 1

        window_show_receipt = tk.Toplevel(self)
        window_show_receipt.geometry('600x400+222+111')
        window_show_receipt.title('Ask Information')

        try:
            self.ask_data = pd.read_csv('ask_information.csv', index_col=0)
        except:
            self.ask_data = pd.DataFrame(columns=['Receipt ID', 'order_name', 'order_amount', 'order_price', 'order_time'])
        self.button2 = ttk.Button(window_show_receipt, text='Before',bootstyle=(INFO, OUTLINE), command=lambda: beforpage(self.page - 1, self))
        self.button2.place(x=200,y=200)
        self.button3 = ttk.Button(window_show_receipt, text='Next',bootstyle=(INFO, OUTLINE), command=lambda: nextpage(self.page + 1, self))
        self.button3.place(x=340,y=200)

        self.tree1 = ttk.Treeview(
            window_show_receipt,  #
            height=5,  # 表格显示的行数
            columns=['Receipt ID', 'order_name', 'order_amount', 'order_price', 'order_time'],  # 显示的列
            show='headings',  # 隐藏首列
        )
        for x in ['Receipt ID', 'order_name', 'order_amount', 'order_price', 'order_time']:
            self.tree1.heading(x, text=x)
            self.tree1.column(x, width=120)
        self.tree1.grid(row=2, columnspan=3)
        for i in range(len(self.ask_data)):
            self.tree1.insert('', i, values=self.ask_data.iloc[i, :].tolist())

        def beforpage(page, self):
            if page < 1:
                messagebox.showerror(title='Error', message='First Page')
            if len(self.ask_data) - 5 * (page - 1) <= 0:
                messagebox.showerror(title='Error', message='Last page')
            if len(self.ask_data) - 5 * (page - 1) >= 5:
                index = 5 * (page - 1)
                for i in range(5):
                    self.tree1.insert('', i, values=self.ask_data.iloc[index + i, :].tolist())
            else:
                index = 5 * (page - 1)
                for i in range(len(self.ask_data) - 5 * (page - 1)):
                    self.tree1.insert('', i, values=self.ask_data.iloc[index + i, :].tolist())
                for i in range(5 * page - len(self.ask_data)):
                    self.tree1.insert('', i, values='')

            self.page -= 1

        def nextpage(page, self):

            if len(self.ask_data) - 5 * (page-1) <= 0:
                messagebox.showerror(title='Error', message='Last page')
            if len(self.ask_data) - 5 * (page-1) >= 5:
                index = 5 * (page-1)
                for i in range(5):
                    self.tree1.insert('',  i, values=self.ask_data.iloc[index + i, :].tolist())
            else:
                index = 5 * (page-1)
                for i in range(len(self.ask_data) - 5 * (page-1)):
                    self.tree1.insert('',  i, values=self.ask_data.iloc[index + i, :].tolist())
                for i in range(5 * page - len(self.ask_data)):
                    self.tree1.insert('', i, values='')
            self.page += 1

    def sendBid(self):
        window_show_receipt = tk.Toplevel(self)
        window_show_receipt.geometry('600x400+222+111')
        window_show_receipt.title('Bid Information')

        try:
            self.bid_data = pd.read_csv('bid_information.csv', index_col=0)
        except:
            self.bid_data = pd.DataFrame(columns=['Receipt ID', 'order_name', 'order_amount', 'order_price', 'order_time'])
        self.button2 = ttk.Button(window_show_receipt, text='Before', bootstyle=(INFO, OUTLINE), command=lambda: beforpage(self.page - 1, self))
        self.button2.place(x=200,y=200)
        self.button3 = ttk.Button(window_show_receipt, text='Next',bootstyle=(INFO, OUTLINE), command=lambda: nextpage(self.page + 1, self))
        self.button3.place(x=340,y=200)

        self.tree1 = ttk.Treeview(
            window_show_receipt,  #
            height=5,  # 表格显示的行数
            columns=['Receipt ID', 'order_name', 'order_amount', 'order_price', 'order_time'],  # 显示的列
            show='headings',  # 隐藏首列
        )
        for x in ['Receipt ID', 'order_name', 'order_amount', 'order_price', 'order_time']:
            self.tree1.heading(x, text=x)
            self.tree1.column(x, width=120)
        self.tree1.grid(row=2, columnspan=3)
        for i in range(len(self.bid_data)):
            self.tree1.insert('', i, values=self.bid_data.iloc[i, :].tolist())

        def beforpage(page, self):
            if page < 1:
                messagebox.showerror(title='Error', message='First Page')
            if len(self.bid_data) - 5 * (page - 1) <= 0:
                messagebox.showerror(title='Error', message='Last page')
            if len(self.bid_data) - 5 * (page - 1) >= 5:
                index = 5 * (page - 1)
                for i in range(3):
                    self.tree1.insert('', i, values=self.bid_data.iloc[index + i, :].tolist())
            else:
                index = 5 * (page - 1)
                for i in range(len(self.bid_data) - 5 * (page - 1)):
                    self.tree1.insert('', i, values=self.bid_data.iloc[index + i, :].tolist())
                for i in range(5 * page - len(self.bid_data)):
                    self.tree1.insert('', i, values='')

            self.page -= 1

        def nextpage(page, self):

            if len(self.bid_data) - 5 * (page - 1) <= 0:
                messagebox.showerror(title='Error', message='Last page')
            if len(self.bid_data) - 5 * (page - 1) >= 5:
                index = 5 * (page - 1)
                for i in range(5):
                    self.tree1.insert('', i, values=self.bid_data.iloc[index + i, :].tolist())
            else:
                index = 5 * (page - 1)
                for i in range(len(self.bid_data) - 5 * (page - 1)):
                    self.tree1.insert('', i, values=self.bid_data.iloc[index + i, :].tolist())
                for i in range(5 * page - len(self.bid_data)):
                    self.tree1.insert('', i, values='')
            self.page += 1

    def createBid(self):
        window_show_receipt = tk.Toplevel(self)
        window_show_receipt.geometry('600x400+222+111')
        window_show_receipt.title('Create Bid Order')

        tk.Label(window_show_receipt, text='Create Bid Order',font=('microsoft yahei', 20, 'bold')).place(x=180,y=20)

        #tk.Label(window_show_receipt, text='Owner Id: ').grid(row=1, column=0)
        tk.Label(window_show_receipt, text='Owner Id: ').place(x=160,y=100)
        self.entry_orderId = tk.Entry(window_show_receipt)
        #self.entry_orderId.grid(row=1, column=1)
        self.entry_orderId.place(x=280,y=100)

        #tk.Label(window_show_receipt, text='Order Name: ').grid(row=2, column=0)
        tk.Label(window_show_receipt, text='Owner Name: ').place(x=160, y=140)
        self.entry_orderName = tk.Entry(window_show_receipt)
        #self.entry_orderName.grid(row=2, column=1)
        self.entry_orderName.place(x=280,y=140)

        #tk.Label(window_show_receipt, text='Order Amount : ').grid(row=3, column=0)
        tk.Label(window_show_receipt, text='Order Amount : ').place(x=160,y=180)
        self.entry_orderAmount = tk.Entry(window_show_receipt)
        #self.entry_orderAmount.grid(row=3, column=1)
        self.entry_orderAmount.place(x=280,y=180)

        #tk.Label(window_show_receipt, text='Order Price: ').grid(row=4, column=0)
        tk.Label(window_show_receipt, text='Order Price: ').place(x=160,y=220)
        self.entry_orderPrice = tk.Entry(window_show_receipt)
        #self.entry_orderPrice.grid(row=4, column=1)
        self.entry_orderPrice.place(x=280,y=220)

        ttk.Button(window_show_receipt, text='Create Bid Order',bootstyle=(INFO, OUTLINE),command=self.createBidfunction).place(x=240,y=260)

    def createBidfunction(self):
        entry_orderId = self.entry_orderId.get()
        entry_orderName = self.entry_orderName.get()
        entry_orderAmount = self.entry_orderAmount.get()
        entry_orderPrice = self.entry_orderPrice.get()
        now_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())

        try:
            data = pd.read_csv('bid_information.csv', index_col=0)
        except:
            data = pd.DataFrame(columns=['owner_id', 'order_name', 'order_amount', 'order_price', 'order_time'])
        series = {'owner_id': entry_orderId, 'order_name': entry_orderName, 'order_amount': entry_orderAmount, 'order_price': entry_orderPrice, 'order_time': now_time}
        data = data.append(series, ignore_index=True)

        data.to_csv('bid_information.csv')
        messagebox.showinfo(title='Results', message='Create Bid Information Successfully')

    # ask ask ask functions
    def createAsk(self):
        window_show_receipt = tk.Toplevel(self)
        window_show_receipt.geometry('600x400+222+111')
        window_show_receipt.title('Create Ask Order')

        tk.Label(window_show_receipt, text='Create Ask Order',font=('microsoft yahei', 20, 'bold')).place(x=180,y=20)

        tk.Label(window_show_receipt, text='Owner Id: ').place(x=160,y=100)
        self.entry_orderId = tk.Entry(window_show_receipt)
        self.entry_orderId.place(x=280,y=100)


        tk.Label(window_show_receipt, text='Order Name: ').place(x=160,y=140)
        self.entry_orderName = tk.Entry(window_show_receipt)
        self.entry_orderName.place(x=280,y=140)

        tk.Label(window_show_receipt, text='Order Amount : ').place(x=160,y=180)
        self.entry_orderAmount = tk.Entry(window_show_receipt)
        self.entry_orderAmount.place(x=280,y=180)

        tk.Label(window_show_receipt, text='Order Price: ').place(x=160,y=220)
        self.entry_orderPrice = tk.Entry(window_show_receipt)
        self.entry_orderPrice.place(x=280,y=220)

        ttk.Button(window_show_receipt, text='Create Ask Order',bootstyle=(INFO, OUTLINE),command=self.createAskfunction).place(x=240, y=260)

    def createAskfunction(self):
        entry_orderId = self.entry_orderId.get()
        entry_orderName = self.entry_orderName.get()
        entry_orderAmount = self.entry_orderAmount.get()
        entry_orderPrice = self.entry_orderPrice.get()
        now_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())

        try:
            data = pd.read_csv('Ask_information.csv', index_col=0)
        except:
            data = pd.DataFrame(columns=['owner_id', 'order_name', 'order_amount', 'order_price', 'order_time'])

        series = {'owner_id': entry_orderId, 'order_name': entry_orderName, 'order_amount': entry_orderAmount, 'order_price': entry_orderPrice, 'order_time': now_time}
        data = data.append(series, ignore_index=True)
        print(data)
        data.to_csv('Ask_information.csv')

        messagebox.showinfo(title='Results', message='Create Ask Information Successfully')


class splitReceipt(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.root = master
        self.creat_UI()

    def creat_UI(self):
        tk.Label(self, text='Split Receipts', font=('microsoft yahei', 20, 'bold')).grid(row=0, columnspan=2)
        tk.Label(self, text='Split Receipts Functions ', font=('microsoft yahei', 20, 'bold')).grid(row=0, columnspan=2)

        tk.Label(self, text='Split Receipt ID: ').grid(row=1, column=0)
        self.entry_receipt_id = tk.Entry(self)
        self.entry_receipt_id.grid(row=1, column=1)

        tk.Label(self, text='Old Amount: ').grid(row=2, column=0)
        self.entry_oldAmount = tk.Entry(self)
        self.entry_oldAmount.grid(row=2, column=1)

        tk.Label(self, text='New Receipt ID: ').grid(row=3, column=0)
        self.entry_newReceiptID = tk.Entry(self)
        self.entry_newReceiptID.grid(row=3, column=1)

        tk.Label(self, text='Owner Address: ').grid(row=4, column=0)
        self.entry_ownerAddress = tk.Entry(self)
        self.entry_ownerAddress.grid(row=4, column=1)

        tk.Label(self, text='Commodity Id: ').grid(row=5, column=0)
        self.entry_Commodity_id = tk.Entry(self)
        self.entry_Commodity_id.grid(row=5, column=1)

        tk.Label(self, text='Commodity Weight: ').grid(row=6, column=0)
        self.entry_commodity_weight = tk.Entry(self)
        self.entry_commodity_weight.grid(row=6, column=1)

        tk.Label(self, text='Commodity Amount: ').grid(row=7, column=0)
        self.entry_commodityAmount = tk.Entry(self)
        self.entry_commodityAmount.grid(row=7, column=1)

        tk.Label(self, text='Settel Id: ').grid(row=8, column=0)
        self.entry_settelId = tk.Entry(self)
        self.entry_settelId.grid(row=8, column=1)

        tk.Label(self, text='Quality Date: ').grid(row=9, column=0)
        self.entry_qualityDate = tk.Entry(self)
        self.entry_qualityDate.grid(row=9, column=1)

        new_create = tk.StringVar()  # 将输入的注册名赋值给变量
        new_create.set('Split the {Old Receipt}, Create {New Receipt}')  # 将最初显示定为'example@python.com'
        tk.Label(self, text='Other Info: ').grid(row=10, column=0)
        self.entry_other_Info = tk.Entry(self, textvariable=new_create)
        self.entry_other_Info.grid(row=10, column=1)

        ttk.Button(self, text='Split',bootstyle=(INFO, OUTLINE),command=self.sendSpilt).grid(row=11, column=1)

    def sendSpilt(self):
        entry_old_receipt_id = self.entry_receipt_id.get()
        entry_oldAmount = self.entry_oldAmount.get()

        entry_bool = False if entry_oldAmount == 0 else True

        entry_receipt_id = self.entry_newReceiptID.get()
        entry_ownerAddress = self.entry_ownerAddress.get()
        entry_Commodity_id = self.entry_newReceiptID.get()
        entry_commodity_weight = self.entry_commodity_weight.get()
        entry_commodityAmount = self.entry_commodityAmount.get()
        entry_settelId = self.entry_settelId.get()
        entry_qualityDate = self.entry_qualityDate.get()
        entry_other_Info = self.entry_other_Info.get()

        result = trd.splitReceipt(
            [int(entry_old_receipt_id), int(entry_oldAmount), entry_bool, int(entry_receipt_id), str(entry_ownerAddress), int(entry_Commodity_id), int(entry_commodity_weight),
             int(entry_commodityAmount), int(entry_settelId), int(entry_qualityDate), str(entry_other_Info)])

        if result[0] == 1:
            messagebox.showinfo(title='Create Result', message='Successfully split receipts \n Old Receipt ID : {} \n New Receipt ID: {}'.format(entry_old_receipt_id, entry_receipt_id))
        elif result[0] == -1 and result[1] == -1:
            messagebox.showerror(title='Create Result', message='Fail to create receipts \n Old Receipt ID : {} \n New Receipt ID: {}'.format(entry_old_receipt_id, entry_receipt_id))

        elif result[0] == 0:
            messagebox.showerror(title='Create Result', message='Fail to create receipts \n Old Receipt ID : {} \n New Receipt ID: {} \n{} \n{} \n{}'.format(entry_old_receipt_id, entry_receipt_id, result[1][0], result[1][1], result[1][2]))


def about():
    top1 = tk.Toplevel()
    top1.geometry('600x400+222+111')
    top1.title('About')

    la1 = tk.Label(top1, text='Meta Digital Receipt System')
    la1.pack(pady=10)
    la2 = tk.Label(top1, text='Contact with us: +852 110')
    la2.pack(pady=10)
    but1 = ttk.Button(top1, text="  OK  ",bootstyle=(INFO, OUTLINE),command=top1.destroy)
    but1.pack(side=BOTTOM, pady=10)

    top1.attributes("-toolwindow", 1)  # 无最大化，最小化
    top1.transient()  # 窗口只置顶root之上
    top1.resizable(False, False)  # 不可调节窗体大小
    top1.grab_set()  # 转化模式
    top1.focus_force()  # 得到焦点


root = tk.Tk()
login(root)  # 登录界面类的实例化
root.mainloop()
