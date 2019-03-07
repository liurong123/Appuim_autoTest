import unittest
from testsuies.base_testcase import Test_basecase
from pageobjects.bwl_page import *
class test_bwl8(Test_basecase):
   def test_znbe8(self):
      h = IndexPage(self.driver)
      h.delect_bel()
      h.delect_see()
      h.qingkong()
      # h.tuichu()


if __name__=="__main__":
   unittest.main()