#————————————————————————————引入模块——————————————————————————————
from selenium.webdriver.common.by import By #定位手段
from time import sleep
from zdh.作业.day7.京东.po.d1c.d1c import lei #调用
#————————————————————————————引入模块——————————————————————————————


class yw2(lei):
    jd_001=(By.CLASS_NAME,'link-login')#点击登录
    jd_002=(By.XPATH,'/html/body/div[2]/div[2]/div[1]/div/div[6]/ul/li[1]/a/span')#qq登录
    jd_003=(By.ID,'ptlogin_iframe')#if框架
    jd_004=(By.ID,'switcher_plogin')#账号密码登录
    jd_005=(By.ID,'u')#输入账号
    jd_006=(By.ID,'p')#输入密码
    jd_007=(By.ID,'login_button')#点击登录
    jd_008 = (By.XPATH, "/html/body/div[1]/div[5]/div[1]/div[1]/div/ul/li[3]/a[1]")  # 电脑
    jd_009 = (By.XPATH,"/html/body/div[3]/div[2]/div/div[2]/div/div[1]/div[1]/div/div/div/div/div/ul/li[1]/nav/a[1]/span")  # 点击笔记本
    jd_010 = (By.XPATH, "/html/body/div[7]/div/div[2]/div[1]/div/div[2]/ul/li[1]/div/div[1]/a/img")  # 商品详情
    jd_011 = (By.ID, "InitCartUrl")  # 加入购物车按钮



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

    def djdn(self):  # 点击电脑
        self.dw(*self.jd_008).click()

    def djbjb(self):  # 点击笔记本
        self.dw(*self.jd_009).click()

    def gd(self):  # 滚动400
        self.driver.execute_script('window.scrollTo(0,400)')

    def sp(self):  # 商品详情
        self.dw(*self.jd_010).click()

    def jrgwc(self):  # 加入购物车
        self.dw(*self.jd_011).click()

    def test_002(self):
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
        self.djdn()
        sleep(2)
        self.djbjb()
        sleep(2)
        self.gd()
        sleep(2)
        self.sp()
        sleep(2)
        self.jrgwc()
        sleep(2)



