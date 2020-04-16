from framework.superClass.executor import Exexutor
from framework.config.dynamic import *
from framework.tool.tool import *
import unittest

class JCWExecutor(Exexutor):

    def setDiscover(self):
        self.case_path = CASE_PATH
        self.discover = unittest.defaultTestLoader.discover(self.case_path,pattern='JCWAutoTest*.py',top_level_dir=None)
        # self.discover = unittest.defaultTestLoader.discover(self.case_path, pattern='[JCWAutoTest](0012)[.py]', top_level_dir=None)

    def setReportPath(self):
        self.report_file = os.path.join(REPORT_PATH, str(getCurrentTime()) + '_result.html')

if __name__ == '__main__':
    JCWExecutor().executeSuite()









