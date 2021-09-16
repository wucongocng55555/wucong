from selenium import webdriver
from time import sleep #强制等待时间
from selenium.webdriver.common.keys import Keys #键盘
from selenium.webdriver.common.action_chains import ActionChains #鼠标
from selenium.webdriver.support.ui import Select #下拉框

# 打开携程
driver=webdriver.Firefox()
driver.get('https://www.ctrip.com/')

# 登录
driver.find_element_by_class_name('person-text').click()
sleep(2)
# 窗口切换
driver.switch_to.window(driver.window_handles[-1])
sleep(2)
# qq登录
driver.find_element_by_class_name('icon-qq').click()
sleep(2)
# 窗口切换
driver.switch_to.window(driver.window_handles[-1])
sleep(2)
# if框架
driver.switch_to.frame(driver.find_element_by_id('ptlogin_iframe'))
sleep(2)
# 鼠标悬停
ActionChains(driver).move_to_element(driver.find_element_by_id('switcher_plogin')).perform()
sleep(2)
# 账号密码登录
driver.find_element_by_id('switcher_plogin').click()
sleep(2)
# 输入账号
driver.find_element_by_id('u').send_keys('2707974464')
sleep(2)
# 输入密码
driver.find_element_by_id('p').send_keys('wucongcong55555')
sleep(2)
# 授权登录
driver.find_element_by_xpath('//*[@id="login_button"]').click()
sleep(2)
# 窗口切换
driver.switch_to.window(driver.window_handles[-1])
sleep(2)
# 鼠标悬停
ActionChains(driver).move_to_element(driver.find_element_by_css_selector('#c_ph_hp')).perform()
sleep(2)
# 点击首页
driver.find_element_by_css_selector('#c_ph_hp').click()
sleep(2)
# 点击搜索框
driver.find_element_by_xpath('//*[@id="_allSearchKeyword"]').send_keys('西安')
sleep(2)
# 回车
driver.find_element_by_xpath('//*[@id="_allSearchKeyword"]').send_keys(Keys.ENTER)
sleep(2)
