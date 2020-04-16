# -*- coding:utf-8 -*-
'''
@File   : JCWAutoTest0012.py
@Author : zhuy
@Date   : 2019/6/2 19:31
@Desc   :
'''

import unittest
from framework.superClass.jcwCase import JcwCase
from testJCW.action.loginPage import LoginPage
from testJCW.action.system.user.accountMainPage import AccountMainPage

class JCWAutoTest0012(JcwCase, unittest.TestCase):
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
    
    def custom_step(self):
        LoginPage().login_data(self.data.get('login'))
        accountMainPage = AccountMainPage()
        accountMainPage.enterFunction()
        accountMainPage.createAccount(self.data.get('userData'))
        accountMainPage.search(self.data.get('userData').get('accountUsername'))
        return accountMainPage.checkupTableData(self.data.get('userData'))


if __name__ == '__main__':
    unittest.main()
