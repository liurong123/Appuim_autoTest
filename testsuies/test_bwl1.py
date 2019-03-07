import unittest
from testsuies.base_testcase import Test_basecase
from pageobjects.bwl_page import *
class test_bwl1(Test_basecase):
   def test_znbel(self):
      h = IndexPage(self.driver)
      h.zhuce("z1xen23p234", "aggrn242x3@qq.com", "agggg123")
      h.tuichu()
      h.zhuce("zxcv", "asdfgggg@qq.com", "asdfgggg")


if __name__=="__main__":
   unittest.main()