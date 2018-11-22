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
        """打赏打CALL"""
        self.driver.tap([(370,390)])
        sleep(3)
        self.driver.find_element_by_id("bt_feed").click()
        sleep(1)
        self.driver.find_element_by_name("打CALL").click()
        sleep(1)
        self.driver.find_element_by_id("tx_add").click()
        sleep(1)
        self.driver.find_element_by_id("btn_feed").click()
        sleep(1)
        self.driver.find_element_by_id("bt_confirm").click()
        sleep(1)
        self.driver.get_screenshot_as_file(r"D:\test_jietu\dacall.png")

    def test_2(self):
        """打赏吃瓜"""
        self.driver.tap([(370,390)])
        sleep(3)
        self.driver.find_element_by_id("bt_feed").click()
        sleep(1)
        self.driver.find_element_by_name("吃瓜").click()
        sleep(1)
        self.driver.find_element_by_id("tx_add").click()
        sleep(1)
        self.driver.find_element_by_id("btn_feed").click()
        sleep(1)
        self.driver.find_element_by_id("bt_confirm").click()
        sleep(1)
        self.driver.get_screenshot_as_file(r"D:\test_jietu\chigua.png")

    def test_3(self):
        """打赏冰阔落"""
        self.driver.tap([(370,390)])
        sleep(3)
        self.driver.find_element_by_id("bt_feed").click()
        sleep(1)
        self.driver.find_element_by_name("冰阔落").click()
        sleep(1)
        self.driver.find_element_by_id("tx_add").click()
        sleep(1)
        self.driver.find_element_by_id("btn_feed").click()
        sleep(1)
        self.driver.find_element_by_id("bt_confirm").click()
        sleep(1)
        self.driver.get_screenshot_as_file(r"D:\test_jietu\bingkele.png")

    def test_4(self):
        """打赏加个鸡腿"""
        self.driver.tap([(370,390)])
        sleep(3)
        self.driver.find_element_by_id("bt_feed").click()
        sleep(1)
        self.driver.find_element_by_name("加个鸡腿").click()
        sleep(1)
        self.driver.find_element_by_id("tx_add").click()
        sleep(1)
        self.driver.find_element_by_id("btn_feed").click()
        sleep(1)
        self.driver.find_element_by_id("bt_confirm").click()
        sleep(1)
        self.driver.get_screenshot_as_file(r"D:\test_jietu\jitui.png")

    def test_5(self):
        """打赏 大哥，喝啤酒"""
        self.driver.tap([(370,390)])
        sleep(3)
        self.driver.find_element_by_id("bt_feed").click()
        sleep(1)
        self.driver.find_element_by_name("大哥，喝啤酒").click()
        sleep(1)
        self.driver.find_element_by_id("tx_add").click()
        sleep(1)
        self.driver.find_element_by_id("btn_feed").click()
        sleep(1)
        self.driver.find_element_by_id("bt_confirm").click()
        sleep(1)
        # try:
        #     if self.driver.find_element_by_name("已收藏").is_displayed():
        #         print "校验通过，作品已收藏"
        # except Exception, e:
        #     print e
        #     print "校验不通过"
        self.driver.get_screenshot_as_file(r"D:\test_jietu\pijiu.png")

    def test_6(self):
        """打赏蟹蟹"""
        self.driver.tap([(370,390)])
        sleep(3)
        self.driver.find_element_by_id("bt_feed").click()
        sleep(1)
        self.driver.find_element_by_name("蟹蟹").click()
        sleep(1)
        self.driver.find_element_by_id("tx_add").click()
        sleep(1)
        self.driver.find_element_by_id("btn_feed").click()
        sleep(1)
        self.driver.find_element_by_id("bt_confirm").click()
        sleep(1)
        self.driver.get_screenshot_as_file(r"D:\test_jietu\pangxie.png")

    def test_7(self):
        """取消打赏"""
        self.driver.tap([(370,390)])
        sleep(3)
        self.driver.find_element_by_id("bt_feed").click()
        sleep(1)
        self.driver.find_element_by_name("打CALL").click()
        sleep(1)
        self.driver.find_element_by_id("tx_add").click()
        sleep(1)
        self.driver.find_element_by_id("btn_feed").click()
        sleep(1)
        self.driver.find_element_by_id("bt_cancel").click()
        sleep(1)
        self.driver.get_screenshot_as_file(r"D:\test_jietu\tanchuangshouqi.png")

    def tearDown(self):
        self.driver.quit()
        sleep(2)


if __name__ == '__main__':
    unittest.main()
