# -*- coding:utf-8 -*-
'''
@File   : JCWAutoTest0020.py
@Author : zhuy
@Date   : 2019/7/26 15:06
@Desc   :
'''

import unittest
from framework.superClass.jcwCase import JcwCase
from testJCW.action.system.dept.deptMainPage import DeptMainPage
from testJCW.action.loginPage import LoginPage
class JCWAutoTest0020(JcwCase, unittest.TestCase):
    '''
        Automated test case 
        setUp(),test_main(),tearDown() These three methods do not support custom editing
        Assemble the steps in the action module into a complete test case under custom_step
    '''
    
    def setUp(self):
        self.envInit()
    
    def test_main(self):
        self.executeTest()
    
    def tearDown(self):
        self.envRecovery()
    
    def custom_setUp(self):
        LoginPage().login_data(self.data.get('login'))
        deptMainPage = DeptMainPage()
        deptMainPage.enterFunction()
        deptMainPage.search(self.data.get('createDept').get('deptName'))
        
    def custom_step(self):
        deptMainPage = DeptMainPage()
        deptMainPage.enterFunction()
        deptMainPage.createDept(self.data.get('createDept'))
        deptMainPage.search(self.data.get('createDept').get('deptName'))
        return deptMainPage.checkupTableData(self.data.get('createDept'))
    
    def custom_tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
