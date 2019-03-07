from pageobjects.base import Base
from appium.webdriver.common.mobileby import By
import time
class IndexPage(Base):
    # 展开注册按钮
    page_zhuce=(By.ID,'com.pdswp.su.smartcalendar:id/ab_icon2')
    # 登录按钮进入注册
    page_login=(By.ID,'com.pdswp.su.smartcalendar:id/email')
    # 注册按钮
    page_zcyx=(By.ID,'com.pdswp.su.smartcalendar:id/register')
    # 注册昵称输入框
    page_name=(By.ID,'com.pdswp.su.smartcalendar:id/username')
    # 注册邮箱输入框
    page_email=(By.ID,'com.pdswp.su.smartcalendar:id/email')
    # 注册密码输入框
    page_pwd=(By.ID,'com.pdswp.su.smartcalendar:id/password')
    # 提交注册
    page_zhuce_button=(By.ID,'com.pdswp.su.smartcalendar:id/reguser')
    # 退出
    page_tuichu=(By.ID,'com.pdswp.su.smartcalendar:id/exit')
    # 登录
    login_button=(By.ID,'com.pdswp.su.smartcalendar:id/login')
    #用户名
    user_name=(By.ID,'com.pdswp.su.smartcalendar:id/username')
    user_name2=(By.ID,'com.pdswp.su.smartcalendar:id/title')
    new_user_name=(By.CLASS_NAME,'android.widget.EditText')
    #对勾
    duigou=(By.ID,'com.pdswp.su.smartcalendar:id/quick_add')
    #添加备忘录加号
    add_logo=(By.ID,'com.pdswp.su.smartcalendar:id/menuAdd')
    #添加内容框
    add_text=(By.ID,'com.pdswp.su.smartcalendar:id/add_input_content')
    #添加备忘
    page_add_bwl=(By.ID,'com.pdswp.su.smartcalendar:id/design_menu_item_text')
    #查找
    find_logo=(By.ID,'com.pdswp.su.smartcalendar:id/toolbar_search')
    #搜索框
    find_text=(By.ID,'android:id/search_src_text')
    find_result=(By.ID,'com.pdswp.su.smartcalendar:id/note_title')
    #归档备忘录
    gd_text=(By.ID,'com.pdswp.su.smartcalendar:id/note_all')
    gd_button=(By.NAME,'归档')
    gd_mulu=(By.NAME,'归档')
    #还原归档
    back_gd=(By.ID,'com.pdswp.su.smartcalendar:id/note_title')
    gd_clear=(By.ID,'com.pdswp.su.smartcalendar:id/menu')
    #删除备忘录
    delect_button=(By.NAME,'删除备忘')
    huishou=(By.NAME,'回收站')
    qk_button=(By.NAME,"清空回收站")
    sure_button=(By.NAME,"确定")
    #排序
    paixu_button=(By.NAME,'排序')
    move_button=(By.ID,'com.pdswp.su.smartcalendar:id/sortBtn')
    def zhuce(self, name, email, pwd):
        self.click(*self.page_zhuce)
        self.click(*self.page_login)
        self.click(*self.page_zcyx)
        self.sendkeys(name, *self.page_name)
        self.sendkeys(email, *self.page_email)
        self.sendkeys(pwd, *self.page_pwd)
        self.click(*self.page_zhuce_button)
    def tuichu(self):
        self.click(*self.page_zhuce)
        self.click(*self.page_login)
        self.click(*self.page_tuichu)
    def login(self, email, pwd):
        self.click(*self.page_zhuce)
        self.click(*self.page_login)
        self.click(*self.page_email)
        self.sendkeys(email, *self.page_email)
        self.sendkeys(pwd, *self.page_pwd)
        self.click(*self.login_button)
        time.sleep(2)
    def rename(self,name):
        self.click(*self.page_zhuce)
        self.click(*self.user_name)
        self.click(*self.user_name2)
        self.sendkeys(name,*self.new_user_name)
        self.click(*self.duigou)
    def addbwl1(self,text):
        self.click(*self.add_logo)
        self.sendkeys(text,*self.add_text)
        self.click(*self.duigou)
    def addbwl2(self,text):
        self.click(*self.page_zhuce)
        self.click(*self.page_add_bwl)
        self.sendkeys(text, *self.add_text)
        self.click(*self.duigou)
    def find(self,text):
        self.click(*self.find_logo)
        self.sendkeys(text,*self.find_text)
        self.huiche(*self.find_text)
        results=self.text(*self.find_result)
        return results
    def guidang(self):
        self.long_press(*self.gd_text)
        self.click(*self.gd_button)
    def seeGD(self):
        self.click(*self.page_zhuce)
        self.click(*self.gd_mulu)
    def backGD(self):
        self.left_move(*self.back_gd)
        self.click(*self.gd_clear)
    def delect_bel(self):
        self.long_press(*self.gd_text)
        self.click(*self.delect_button)
    def delect_see(self):
        self.click(*self.page_zhuce)
        self.click(*self.huishou)
    def qingkong(self):
        self.click(*self.qk_button)
        self.click(*self.sure_button)
    def paixu(self):
        self.long_press(*self.gd_text)
        self.click(*self.paixu_button)
        self.get_windows_img()
        self.down_move(*self.move_button)






