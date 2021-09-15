driver=webdriver.Firefox()
driver.get('https://www.jd.com/')
# driver.implicitly_wait() 隐试等待
#浏览器
driver.get_window_size()#获取浏览器大小
driver.set_window_rect()#设置浏览器大小
driver.refresh()        #刷新
driver.back()           #返回上一步
driver.forward()        #回到上一步
driver.minimize_window()#浏览器最小化
driver.maximize_window()#浏览器最大化
driver.quit()           #关闭驱动
driver.close()          #关闭浏览器页面
#鼠标
ActionChains(driver).click().perform()         #左点击
ActionChains(driver).context_click().perform() #右击
ActionChains(driver).double_click().perform()  #双击
ActionChains(driver).drag_and_drop().perform() #拖动
ActionChains(driver).move_to_element().perform()#鼠标悬停
ActionChains(driver).drag_and_drop_by_offset().perform()#拖拽
ActionChains(driver).release().perform()       #释放鼠标
ActionChains(driver).click_and_hold().perform()# 左键按住不释放
#键盘
driver.find_element_by_id().send_keys(Keys.ENTER) #回车
driver.find_element_by_id().send_keys(Keys.BACK_SPACE)#退空格
driver.find_element_by_id().send_keys(Keys.SPACE)#空格
driver.find_element_by_id().send_keys(Keys.ESCAPE)#返回
driver.find_element_by_id().send_keys(Keys.CONTROL,'a')#全选
driver.find_element_by_id().send_keys(Keys.PAGE_UP)#翻页键上
driver.find_element_by_id().send_keys(Keys.PAGE_DOWN)#翻页键下
driver.find_element_by_id().send_keys(Keys.SHIFT)#大小写转化
#滚动条
driver.execute_script('window.scrollTo(0,3000)') #指定到某地
driver.execute_script('window.scrollTo(0,0)')    #指定到顶部
driver.execute_script('window.scrollTo(0,document.body.scrollHeight)') #指定到底部
#多窗口
driver.switch_to.window(driver.window_handles[-1])
#iframe框架
driver.switch_to.frame(driver.find_element_by_id(''))
#下拉框
a=Select(driver.find_element_by_id(''))
a.select_by_index('第几个')
a.select_by_value('第几个')
#弹窗
b=driver.switch_to.alert
b.accept()
b.dismiss()
b.send_keys()