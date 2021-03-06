# -*- coding:utf-8 -*-
'''
@File   : JCWAutoTest0006.py
@Author : zhuy
@Date   : 2019/6/10 10:35
@Desc   :
'''

import unittest
from framework.superClass.jcwCase import JcwCase
from testJCW.action.loginPage import LoginPage
from testJCW.action.system.user.accountMainPage import AccountMainPage

class JCWAutoTest0006(JcwCase, unittest.TestCase):
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
        loginPage = LoginPage()
        loginPage.loginSu()
        accountMainPage = AccountMainPage()
        accountMainPage.enterFunction()
        row = {'accountUsername': self.data.get('userData').get('accountUsername')}
        accountMainPage.search(row.get('accountUsername'))
        if not accountMainPage.checkupTableData(row):
            loginPage.reLogin(self.data.get('login'))
            accountMainPage.createAccount(self.data.get('create_userData'))
    
    def custom_step(self):
        loginPage = LoginPage()
        loginPage.loginSu()
        accountMainPage = AccountMainPage()
        accountMainPage.enterFunction()
        row = {'accountUsername': self.data.get('userData').get('accountUsername')}
        accountMainPage.search(row.get('accountUsername'))
        return accountMainPage.checkupTableData(row)
    
    def custom_tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()



