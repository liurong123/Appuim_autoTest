import unittest
from testsuies.base_testcase import Test_basecase
from pageobjects.bwl_page import *
class test_bwl3(Test_basecase):
   def test_znbe3(self):
      h = IndexPage(self.driver)
      h.login("asdfggggr@qq.com", "asdfgggg")
      h.rename("q111qqwqq")

if __name__=="__main__":
   unittest.main()