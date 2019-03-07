import unittest
from testsuies.base_testcase import Test_basecase
from pageobjects.bwl_page import *
class test_bwl7(Test_basecase):
   def test_znbe7(self):
      h = IndexPage(self.driver)
      h.guidang()
      h.seeGD()
      h.backGD()


if __name__=="__main__":
   unittest.main()