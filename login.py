#coding:utf-8
from time import *
import unittest
from appium import webdriver


class MyTestCase(unittest.TestCase):
    def setUp(self):
        desired_caps = {
            'platformName':'Android',
            'platformVersion':'4.4.4',
            # 'deviceName':'192.168.215.103:5555',
            # 'appPackage':'com.yingzt.invest',
            # 'appActivity':'.SplashActivity',
            'deviceName': '192.168.215.103:5555',
            'app': 'E:\\com.idreamsky.avg.platform_1.0_1.apk',
            'unicodeKeyboard':'True',
            'restKeyboard':'True'
                    }
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)
        sleep(2)

    def test_1(self):
        """登录"""
        self.driver.find_element_by_id("phone_et").send_keys("18565667723")
        sleep(1)
        self.driver.find_element_by_id("verify_code_et").send_keys("8276")
        sleep(1)
        self.driver.find_element_by_id("login_tv").click()
        sleep(6)
        try:
            if self.driver.find_element_by_id("title_bar").is_displayed():
                print("校验通过，检测到推荐")
        except Exception:
            print("校验不通过")
        self.driver.get_screenshot_as_file(r"D:denglu.png")

    def tearDown(self):
        self.driver.quit()
        sleep(5)


if __name__ == '__main__':
    unittest.main()
