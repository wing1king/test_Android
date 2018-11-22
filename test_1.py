#coding:utf-8
from time import *
import unittest,warnings#忽略警告
from appium import webdriver


class MyTestCase(unittest.TestCase):
    def setUp(self):
        desired_caps = {
                'platformName': 'Android',
                'platformVersion': '7.0',
                'app': 'd://com.idreamsky.avg.platform_1.0.0_3.apk',
                'deviceName': 'B2T7N16C10000831',#'afc7e8a4',
                'noReset': 'True'}
        warnings.simplefilter("ignore", ResourceWarning)
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        sleep(5)

    def test_1(self):
        self.driver.tap([(370, 390)])
        sleep(3)
        self.driver.find_element_by_id("bt_start_game").click()
        sleep(5)
        self.driver.find_element_by_id("img_button_play").click()
        sleep(20)
        elems = self.driver.find_element_by_class_name("android.view.View")
        while True:
            sleep(0.5)
            elems.click()
            try:
                print("正常点击")
            except Exception as e:
                print(e)
                print("点击错误")

    def tearDown(self):
        self.driver.quit()
        sleep(2)


if __name__ == '__main__':
    unittest.main()
