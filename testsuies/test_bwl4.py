import unittest
from testsuies.base_testcase import Test_basecase
from pageobjects.bwl_page import *
class test_bwl4(Test_basecase):
   def test_znbe4(self):
      h = IndexPage(self.driver)
      h.addbwl1("dfghjkl1234567890")
      h.addbwl2("1234567890qwert")

if __name__=="__main__":
   unittest.main()