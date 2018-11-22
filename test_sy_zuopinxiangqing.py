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
        """进入作品详情页面"""
        self.driver.tap([(370,390)])
        sleep(2)
        try:
            if self.driver.find_element_by_id("bt_start_game").is_displayed():
                print "校验通过，检测到开始游戏按钮"
        except Exception, e:
            print e
            print "校验不通过"
        self.driver.get_screenshot_as_file(r"D:\test_jietu\zuopinxiangqing.png")

    def test_2(self):
        """返回首页"""
        self.driver.tap([(370,390)])
        sleep(2)
        self.driver.find_element_by_class_name("android.widget.ImageButton").click()
        sleep(1)
        try:
            if self.driver.find_element_by_name("推荐").is_displayed():
                print "校验通过，检测到首页推荐"
        except Exception, e:
            print e
            print "校验不通过"
        self.driver.get_screenshot_as_file(r"D:\test_jietu\fanhuishouye.png")

    def tearDown(self):
        self.driver.quit()
        sleep(5)


if __name__ == '__main__':
    unittest.main()
