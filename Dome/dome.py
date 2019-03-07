from appium import webdriver
import os
from appium.webdriver.common.touch_action import TouchAction
apk_path=os.path.dirname(os.path.abspath("."))
desired_caps={}
desired_caps["platformName"]="Android"#设备系统
desired_caps["platformVersion"]="6.2.7.1"#设备系统版本
desired_caps["deviceName"]="127.0.0.1:62001"#设备名称
desired_caps["sessionOverride"]=True
desired_caps["app"]=apk_path+"/app/todolist.apk"
desired_caps["noReset"]=True
desired_caps["appPackage"]="com.example.todolist"
desired_caps["appActivity"]="com.example.todolist.LoginActivity"
driver=webdriver.Remote("http://127.0.0.1:4723/wd/hub",desired_caps)#启动app
#登录
driver.find_element_by_id("com.example.todolist:id/nameET").send_keys(1)
driver.find_element_by_id("com.example.todolist:id/passwordET").send_keys(1)
driver.find_element_by_id("com.example.todolist:id/loginBtn").click()
#新建事物
driver.find_element_by_id("com.example.todolist:id/action_new").click()
driver.find_element_by_name("输入待办事项。。。").send_keys("dgfbgbhnn")
driver.find_element_by_id("com.example.todolist:id/saveBtn").click()
#删除事物
el=driver.find_element_by_id("com.example.todolist:id/toDoItemDetailTv")
TouchAction(driver).long_press(el).wait(1000).perform()
driver.find_element_by_name("删除").click()
driver.find_element_by_name("确定").click()