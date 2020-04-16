# -*- coding:utf-8 -*-
'''
@File   : JCWAutoTest0003.py
@Author : zhuy
@Date   : 2019/6/10 9:40
@Desc   :
'''

import unittest
from framework.superClass.jcwCase import JcwCase
from testJCW.action.loginPage import LoginPage
from testJCW.action.system.user.accountMainPage import AccountMainPage

class JCWAutoTest0003(JcwCase, unittest.TestCase):
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
        LoginPage().loginSu()
        accountMainPage = AccountMainPage()
        accountMainPage.enterFunction()
        row = {'accountUsername': self.data.get('userData').get('accountUsername')}
        accountMainPage.search(row.get('accountUsername'))
        if not accountMainPage.checkupTableData(row):
            accountMainPage.createAccount(self.data.get('create_userData'))
    
        accountMainPage.search(row.get('accountUsername'))
        if accountMainPage.checkupTableData(self.data.get('userData')):
            accountMainPage.ableRow(row)

    def custom_step(self):
        accountMainPage = AccountMainPage()
        accountMainPage.enterFunction()
        row = {'accountUsername': self.data.get('userData').get('accountUsername')}
        accountMainPage.disableRow(row)
        accountMainPage.search(row.get('accountUsername'))
        return accountMainPage.checkupTableData(self.data.get('userData'))

    def custom_tearDown(self):
        accountMainPage = AccountMainPage()
        accountMainPage.enterFunction()
        row = {'accountUsername': self.data.get('userData').get('accountUsername')}
        accountMainPage.search(row.get('accountUsername'))
        if accountMainPage.checkupTableData(self.data.get('userData')):
            accountMainPage.ableRow(row)


if __name__ == '__main__':
    unittest.main()
