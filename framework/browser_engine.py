import yaml
import os
from appium import webdriver
from framework.logger import Logger
import os.path
# from configparser import ConfigParser
logger=Logger(logger="BrowerEngine").getlog()
class BrowerEngine(object):
    def open_driver(self):
        config_path="E:/appuim/config/config.yaml"
        with open(config_path,"r",encoding="utf_8") as file:
            data=yaml.load(file)
        desired_caps = {}
        desired_caps['platformName'] = data['platformName']
        desired_caps['platformVersion'] = data['platformVersion']
        desired_caps['deviceName'] = data['deviceName']
        desired_caps['sessionOverride'] = data['sessionOverride']
        desired_caps['app'] = os.path.dirname(os.path.abspath('.'))+'/app/'+data['app']
        desired_caps['noReset'] = data['noReset']
        desired_caps['appPackage'] = data['appPackage']
        desired_caps['appActivity'] = data['appActivity']

        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub",desired_caps)
        return self.driver
    def quit_browser(self):
        logger.info("现在关闭浏览器")
        self.driver.quit()
# if __name__=="__main__":
#     appium_desired()


