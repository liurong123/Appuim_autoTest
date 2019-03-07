import unittest
from testsuies.base_testcase import Test_basecase
from pageobjects.bwl_page import *
from framework.util import Util
filepath="E:/appuim/data/data.xlsx"
sheetName="Sheet1"
class test_bwl2(Test_basecase):
   def test_znbe2(self):
      u=Util()
      users=u.read_excel(filepath,sheetName)
      data=users[0]
      email=data["email"]
      pwd=data["password"]
      print(email,pwd)
      h = IndexPage(self.driver)
      h.login(email, pwd)
      h.tuichu()
      h.login("aaqq123@qq.com","1234567")

if __name__=="__main__":
   unittest.main()