#————————————————————————————引入模块——————————————————————————————
from selenium.webdriver.common.by import By #定位手段
from time import sleep
from zdh.作业.day7.京东.po.d1c.d1c import lei #调用
from selenium.webdriver.common.keys import Keys #键盘
#————————————————————————————引入模块——————————————————————————————


class yw5(lei):
    jd_001=(By.CLASS_NAME,'link-login')#点击登录
    jd_002=(By.XPATH,'/html/body/div[2]/div[2]/div[1]/div/div[6]/ul/li[1]/a/span')#qq登录
    jd_003=(By.ID,'ptlogin_iframe')#if框架
    jd_004=(By.ID,'switcher_plogin')#账号密码登录
    jd_005=(By.ID,'u')#输入账号
    jd_006=(By.ID,'p')#输入密码
    jd_007=(By.ID,'login_button')#点击登录
    jd_008=(By.ID, "key")  # 输入框


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

    def dck(self):  # 多窗口
        self.driver.switch_to.window(self.driver.window_handles[-1])

    def srk(self):  # 输入框输入
        self.dw(*self.jd_008).send_keys("AJ1高帮")

    def hc(self):  # 回车搜索
        self.dw(*self.jd_008).send_keys(Keys.ENTER)



    def test_005(self):
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
        self.dck()
        sleep(2)
        self.srk()
        sleep(2)
        self.hc()
        sleep(2)





