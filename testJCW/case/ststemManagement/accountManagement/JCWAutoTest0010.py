# -*- coding:utf-8 -*-
'''
@File   : JCWAutoTest0010.py
@Author : zhuy
@Date   : 2019/6/10 16:36
@Desc   :
'''

import unittest
from framework.superClass.jcwCase import JcwCase
from testJCW.action.loginPage import LoginPage
from testJCW.action.system.user.accountMainPage import AccountMainPage

class JCWAutoTest0010(JcwCase, unittest.TestCase):
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
        accountMainPage = AccountMainPage()
        accountMainPage.enterFunction()
        accountMainPage.search(self.data.get('create_userData').get('accountUsername'))
        if accountMainPage.checkupTableData({'accountUsername': self.data.get('create_userData').get('accountUsername')}):
            pass
        else:
            accountMainPage.createAccount(self.data.get('create_userData'))

    def custom_step(self):
        accountMainPage = AccountMainPage()
        accountMainPage.enterFunction()
        accountMainPage.modifyAccount(self.data.get('modify_userData'))
        accountMainPage.search(self.data.get('modify_userData').get('accountUsername'))
        return accountMainPage.checkupTableData(self.data.get('modify_userData'))

    def custom_tearDown(self):
        accountMainPage = AccountMainPage()
        accountMainPage.enterFunction()
        accountMainPage.modifyAccount(self.data.get('recovery_userData'))
        accountMainPage.search(self.data.get('recovery_userData').get('accountUsername'))
        return accountMainPage.checkupTableData(self.data.get('recovery_userData'))


if __name__ == '__main__':
    unittest.main()
