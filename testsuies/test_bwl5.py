import unittest
from ddt import *
from testsuies.base_testcase import Test_basecase
from pageobjects.bwl_page import *
@ddt
class test_bwl5(Test_basecase):
   def test_znbe5(self):
      h = IndexPage(self.driver)
      result=h.find("qwert")
      print(result)
      try:
         self.assertIn("qwert",result,msg=result)
         print("查找成功")
      except AssertionError as result:
         print("找不到这个标题")


if __name__=="__main__":
   unittest.main()