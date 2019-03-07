from appium import webdriver
import os
import yaml
import time
apk_path=os.path.dirname(os.path.abspath("."))
desired_caps={}
desired_caps["platformName"]="Android"
desired_caps["platformVersion"]="6.2.7.1"#设备系统版本
desired_caps["deviceName"]="127.0.0.1:62001"#设备名称
desired_caps["sessionOverride"]=True
desired_caps["app"]=apk_path+"/app/znbwl.apk"
desired_caps["noReset"]=True
desired_caps["appPackage"]="com.pdswp.su.smartcalendar"
desired_caps["appActivity"]="com.pdswp.su.smartcalendar.WelcomeNote"
driver=webdriver.Remote("http://127.0.0.1:4723/wd/hub",desired_caps)
#注册
driver.find_element_by_id("com.pdswp.su.smartcalendar:id/ab_icon").click()
# 点击注册
driver.find_element_by_name("点击注册备忘录云平台").click()
driver.find_element_by_name("注册一个吧!").click()
driver.find_element_by_name("昵称").send_keys("aaaaawww")
driver.find_element_by_name("注册邮箱(这将是您的账号)").send_keys("12542332@qq.com")
driver.find_element_by_id("com.pdswp.su.smartcalendar:id/password").send_keys("12ffv34567")
driver.find_element_by_name("注册").click()
# #修改用户名
# driver.find_element_by_id("com.pdswp.su.smartcalendar:id/username").click()
# driver.find_element_by_id("com.pdswp.su.smartcalendar:id/title").click()
# driver.find_element_by_class_name("android.widget.EditText").send_keys("bbb")
# driver.find_element_by_id("com.pdswp.su.smartcalendar:id/quick_add").click()
# driver.find_element_by_id("com.pdswp.su.smartcalendar:id/ab_icon2").click()
#退出当前账户
# driver.find_element_by_id("com.pdswp.su.smartcalendar:id/username").click()
# driver.find_element_by_name("退出当前账号").click()
#登录
# driver.find_element_by_name("未登录(登陆后可云同步)").click()
# driver.find_element_by_name("邮箱").send_keys("1254@qq.com")
# driver.find_element_by_id("com.pdswp.su.smartcalendar:id/password").send_keys("1234567")
# driver.find_element_by_name("登录").click()

#添加备忘录1
# driver.find_element_by_id("com.pdswp.su.smartcalendar:id/menuAdd").click()
# driver.find_element_by_id("com.pdswp.su.smartcalendar:id/add_input_content").send_keys("qwert")
# driver.find_element_by_id("com.pdswp.su.smartcalendar:id/quick_add").click()
#添加备忘录2
# driver.find_element_by_id("com.pdswp.su.smartcalendar:id/ab_icon").click()
# driver.find_element_by_id('com.pdswp.su.smartcalendar:id/design_menu_item_text').click()
# driver.find_element_by_id("com.pdswp.su.smartcalendar:id/add_input_content").send_keys("qwert")
# driver.find_element_by_id("com.pdswp.su.smartcalendar:id/quick_add").click()
