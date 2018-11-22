from time import *
import unittest
from appium import webdriver


class MyTestCase(unittest.TestCase):
    def setUp(self):
        desired_caps = {
            'platformName': 'Android',
            'platformVersion': '5.1',
            'appPackage': 'com.idreamsky.avg.platform',
            'appActivity': 'com.idreamsky.activity.HomeActivity',
            'deviceName': 'afc7e8a4',
            'unicodeKeyboard': 'True',
            'restKeyboard': 'True',
            'noReset': 'True'
                    }
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)
        sleep(3)

    def test_1(self):
        """进入充值中心页面"""
        self.driver.find_element_by_id("item_personal_center").click()
        sleep(1)
        self.driver.find_element_by_id("view_shop").click()
        sleep(1)
        try:
            if self.driver.find_element_by_id("title_tv").is_displayed():
                print("校验通过，检测到充值中心")
        except ValueError:
            print("校验不通过")
        self.driver.get_screenshot_as_file(r"D:\test_jietu\c1.png")

    def tearDown(self):
        self.driver.quit()
        sleep(2)


if __name__ == '__main__':
    unittest.main()
