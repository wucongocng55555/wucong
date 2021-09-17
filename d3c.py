import unittest
from selenium import webdriver
from zdh.作业.day7.京东.po.d2c.yw1 import yw1
from zdh.作业.day7.京东.po.d2c.yw2 import yw2
from zdh.作业.day7.京东.po.d2c.yw3 import yw3
from zdh.作业.day7.京东.po.d2c.yw4 import yw4
from zdh.作业.day7.京东.po.d2c.yw5 import yw5



class d3c(unittest.TestCase):
    def setUp(self) -> None:
        self.driver=webdriver.Firefox()
    def tearDown(self) -> None:
        pass
    def test_001(self):
        try:
            po = yw1(self.driver)
            po.test_001()
        except Exception as e:
            print(e)
    def test_002(self):
        try:
            po=yw2(self.driver)
            po.test_002()
        except Exception as e:
            print(e)
    def test_003(self):
        try:
            po=yw3(self.driver)
            po.test_003()
        except Exception as e:
            print(e)
    def test_004(self):
        try:
            po=yw4(self.driver)
            po.test_004()
        except Exception as e:
            print(e)
    def test_005(self):
        try:
            po=yw5(self.driver)
            po.test_005()
        except Exception as e:
            print(e)


if __name__ == '__main__':
    unittest.main()


