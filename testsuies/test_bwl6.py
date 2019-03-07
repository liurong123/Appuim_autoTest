import unittest
from testsuies.base_testcase import Test_basecase
from pageobjects.bwl_page import *
class test_bwl6(Test_basecase):
   def test_znbe6(self):
      h = IndexPage(self.driver)
      h.paixu()

if __name__=="__main__":
   unittest.main()