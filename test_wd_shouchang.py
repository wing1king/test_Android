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

    def test_1(self):
        """进入我的收藏页面"""
        self.driver.find_element_by_id("item_my_game").click()
        sleep(1)
        try:
            if self.driver.find_element_by_name("收藏").is_displayed():
                print "校验通过，检测到收藏"
        except Exception, e:
            print e
            print "校验不通过"
        self.driver.get_screenshot_as_file(r"D:\test_jietu\shoucang.png")

    def test_2(self):
        """进入我的历史页面"""
        self.driver.find_element_by_id("item_my_game").click()
        sleep(1)
        self.driver.find_element_by_name("历史").click()
        sleep(1)
        try:
            if self.driver.find_element_by_name("历史").is_displayed():
                print "校验通过，检测到历史"
        except Exception, e:
            print e
            print "校验不通过"
        self.driver.get_screenshot_as_file(r"D:\test_jietu\lishi.png")

    def tearDown(self):
        self.driver.quit()
        sleep(2)


if __name__ == '__main__':
    unittest.main()
