#coding:utf-8
import sys,unittest,time
reload(sys)
sys.setdefaultencoding('utf8')
from HTMLTestRunner import HTMLTestRunner


# 定义测试用例的目录为当前目录
test_dir = 'D:\\test_Android'
discover = unittest.defaultTestLoader.discover(test_dir, pattern='test*.py')

if __name__ == "__main__":
    # 按照一定的格式获取当前的时间
    now = time.strftime("%Y-%m-%d %H-%M-%S")

    # 定义报告存放路径
    filename = r'E:' + now + 'test_teacher_result.html'

    fp = open(filename, "wb")
    # 定义测试报告
    runner = HTMLTestRunner(stream=fp,
                            title="Android端测试报告",
                            description="测试用例执行情况：")
    # 运行测试
    runner.run(discover)
    fp.close()  # 关闭报告文件