#coding:utf-8
from time import *
import unittest
from appium import webdriver


class MyTestCase(unittest.TestCase):
    def setUp(self):
        desired_caps = {
            'platformName':'Android',
            'platformVersion':'4.4.4',
            'appPackage':'com.idreamsky.avg.platform',
            'appActivity':'com.idreamsky.activity.HomeActivity',
            'deviceName': '192.168.215.103:5555',
            'unicodeKeyboard':'True',
            'restKeyboard':'True',
            'noReset': 'True'
                    }
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)
        sleep(3)

    # def test_1(self):
        """下拉刷新"""
        self.driver.swipe(350, 150, 350, 600)
        sleep(2)
        # try:
        #     if self.driver.find_element_by_name("已收藏").is_displayed():
        #         print "校验通过，作品已收藏"
        # except Exception, e:
        #     print e
        #     print "校验不通过"
        # self.driver.get_screenshot_as_file(r"D:\test_jietu\s1.png")

    def test_2(self):
        """上拉加载"""
        self.driver.swipe(350, 1000, 350, 1)
        sleep(2)

    def tearDown(self):
        self.driver.quit()
        sleep(2)


if __name__ == '__main__':
    unittest.main()
