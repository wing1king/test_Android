#coding:utf-8
from time import *
import unittest
from appium import webdriver


class MyTestCase(unittest.TestCase):
    def setUp(self):
        desired_caps = {
                'platformName':'Android',
                'platformVersion':'7.0',
                'appPackage': 'com.idreamsky.avg.platform',
                'appActivity': 'com.idreamsky.activity.HomeActivity',
                'deviceName': 'N8K5T16C26020898',
                'noReset': 'True'}
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)
        sleep(10)

    def test_1(self):
        self.driver.tap([(370,390)])
        sleep(5)
        self.driver.find_element_by_id("bt_start_game").click()
        sleep(5)
        self.driver.swipe(950, 850, 500, 850)
        sleep(1)
        self.driver.find_element_by_id("img_button_play").click()
        sleep(30)
        elems = self.driver.find_element_by_class_name("android.view.View")
        while True:
            sleep(3)
            elems.click()
            try:
                if self.driver.find_element_by_id("bt_start_game1").is_displayed():
                    print ("校验到分支")
                    clock()
            except Exception as e:
                print(e)
                print ("正常点击")
        self.driver.get_screenshot_as_file(r"D:\test_jietu\d2.png")

    def tearDown(self):
        self.driver.quit()
        sleep(2)


if __name__ == '__main__':
    unittest.main()

# import uiautomator2 as u1
# from time import sleep
# d = u1.connect('192.168.1.128')
#
# # 启动App
# d.app_start("d://com.idreamsky.avg.platform_1.0.0_3.apk")
#
# # 搜索
# d(resourceId="com.meizu.mzbbs:id/j0").click()
#
# # 输入关键字
# d(resourceId="com.meizu.mzbbs:id/p9").set_text("flyme")
#
# # 搜索按钮
# d(resourceId="com.meizu.mzbbs:id/tp").click()
#
# sleep(2)
#
# # 停止app
# d.app_stop("com.meizu.mzbbs")