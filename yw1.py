#————————————————————————————引入模块——————————————————————————————
from selenium.webdriver.common.by import By #定位手段
from selenium.webdriver.support.wait import WebDriverWait   #显示等待
from selenium.webdriver.support import expected_conditions as ES
from time import sleep #强制等待
from selenium import webdriver
from selenium.webdriver.common.keys import Keys #键盘
from selenium.webdriver.common.action_chains import ActionChains # 鼠标
from selenium.webdriver.support.select import Select #下拉框
from zdh.作业.day7.京东.po.d1c.d1c import lei #调用
#————————————————————————————引入模块——————————————————————————————



class yw1(lei):
    jd_001=(By.CLASS_NAME,'link-login')#点击登录
    jd_002=(By.XPATH,'/html/body/div[2]/div[2]/div[1]/div/div[6]/ul/li[1]/a/span')#qq登录
    jd_003=(By.ID,'ptlogin_iframe')#if框架
    jd_004=(By.ID,'switcher_plogin')#账号密码登录
    jd_005=(By.ID,'u')#输入账号
    jd_006=(By.ID,'p')#输入密码
    jd_007=(By.ID,'login_button')#点击登录



    def link_login(self): #点击登录
        self.dw(*self.jd_001).click()
    def qqdl(self): #qq登录
        self.dw(*self.jd_002).click()
    def ifkj(self):#if框架
        kj=self.dw(*self.jd_003)
        self.driver.switch_to.frame(kj)
    def zhmm(self):#账号密码登录
        self.dw(*self.jd_004).click()
    def zh(self):#输入账号
        self.dw(*self.jd_005).send_keys('2707974464')
    def mm(self):#输入密码
        self.dw(*self.jd_006).send_keys('wucongcong55555')
    def dl(self):#点击登录
        self.dw(*self.jd_007).click()
    def test_001(self):
        self.dz('https://www.jd.com/')
        sleep(2)
        self.link_login()
        sleep(2)
        self.qqdl()
        sleep(2)
        self.ifkj()
        sleep(2)
        self.zhmm()
        sleep(2)
        self.zh()
        sleep(2)
        self.mm()
        sleep(2)
        self.dl()
        sleep(2)







