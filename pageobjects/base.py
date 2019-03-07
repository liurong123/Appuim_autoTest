from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from framework.logger import Logger
import os
import time
logger=Logger(logger='Base').getlog()
class Base(object):
    def __init__(self,driver):
        self.driver=driver
    def close(self):
        self.driver.close()
    def back(self):
        self.driver.back()
    def forward(self):
        self.driver.forward()
    def get(self,url):
        self.driver.get(url)
    def quit_browser(self):
        pass

    def find_element(self,*element):
        try:
            WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(element))
            return self.driver.find_element(*element)
            # logger.error("找到页面元素")
        except:
            logger.error("%s未找到页面%s元素"%(self,element))
    def find_elements(self,*element):
        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(element))
            return self.driver.find_elements(*element)
        except:
            logger.error("%s未找到页面%s元素"%(self,element))
    def sendkeys(self,text,*element):
        ele=self.find_element(*element)
        ele.send_keys(text)
        logger.info("输入内容")
    def click(self,*element):
        ele=self.find_element(*element)
        ele.click()
    def clear(self,*element):
        ele=self.find_element(*element)
        ele.clear()
    def guanbi(self):
        self.driver.quit()
    def jihuo(self):
        self.driver.switch_to.window(self.driver.current_window_handle)
    def switch_to(self,*element):
        ele=self.find_element(*element)
        self.driver.switch_to.frame(ele)
    def jh(self,x):
        self.driver.switch_to.window(self.driver.window_handles[x])
    def text(self,*element):
        ele=self.find_element(*element)
        return  ele.text
    def huiche(self,*element):
        self.driver.keyevent(66)
    def long_press(self,*element):
        ele=self.driver.find_element(*element)
        TouchAction(self.driver).long_press(ele).wait(1000).perform()

    def left_move(self, *element):
        ele = self.driver.find_element(*element)
        TouchAction(self.driver).press(ele, x=100, y=50).wait(1000).move_to(ele, x=-50, y=0).release().perform()

    def down_move(self, *element):
        ele = self.driver.find_elements(*element)
        TouchAction(self.driver).press(ele[0]).wait(1000).move_to(ele[len(ele) - 1]).release().perform()

    def get_windows_img(self):
        file_path = os.path.dirname(os.path.abspath('.')) + '/screenshots/'
        rq = time.strftime(" %Y%m%d%H%M", time.localtime(time.time()))
        screen_name = file_path + rq + '.png'
        try:
            self.driver.get_screenshot_as_file(screen_name)
            logger.info("Had take screenshot and save to folder：/screenshots")
        except Exception as e:
            self.get_windows_img()
            logger.info("Failed to take screenshot! %s" % e)
        logger.info("截图成功。")
