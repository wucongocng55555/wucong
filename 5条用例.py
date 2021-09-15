import unittest
import unittest
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys #键盘
from selenium.webdriver.common.action_chains import ActionChains #鼠标
from selenium.webdriver.support.ui import Select #下拉框

class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Firefox()
        self.driver.get('https://www.jd.com/')
        # 点击登录
        self.driver.find_element_by_class_name('link-login').click()
        sleep(2)
        # 窗口切换
        self.driver.switch_to(self.driver.window_handles[-1])
        sleep(2)
        # 鼠标悬停
        ActionChains(self.driver).move_to_element(self.driver.find_element_by_class_name('checked')).perform()
        # 选择账户登录
        self.driver.find_element_by_class_name('checked').click()
        sleep(2)
        # 输入账号
        self.driver.find_element_by_class_name('item.item-fore1').send_keys('19904340382')
        sleep(2)
        # 输入密码
        self.driver.find_element_by_id('entry').send_keys('wucongcong55555')
        sleep(2)
        # 授权登录
        self.driver.find_element_by_class_name('login-btn').click()
        sleep(3)
        # 窗口切换
        self.driver.switch_to(self.driver.window_handles[-1])



    def tearDown(self) -> None:
        pass
        # self.driver.quit()
    def test01(self):
        pass
    # def tast02(self):
    #     pass
    # def test03(self):
    #     pass
    # def test04(self):
    #     pass
    # def test05(self):
    #     pass

if __name__ == '__main__':
    unittest.main()
