import unittest
from framework.browser_engine import BrowerEngine
class Test_basecase(unittest.TestCase):
    def setUp(self):
        self.browerengine=BrowerEngine()
        self.driver=self.browerengine.open_driver()
    def tearDown(self):
        self.browerengine.quit_browser()
        print("结束")
