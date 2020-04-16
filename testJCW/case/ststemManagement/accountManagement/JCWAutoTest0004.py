# -*- coding:utf-8 -*-
'''
@File   : JCWAutoTest0004.py
@Author : zhuy
@Date   : 2019/6/2 19:48
@Desc   :
'''

import unittest
from framework.superClass.jcwCase import JcwCase
from testJCW.action.loginPage import LoginPage
from testJCW.action.system.user.accountMainPage import AccountMainPage

class JCWAutoTest0004(JcwCase, unittest.TestCase):
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
        accountMainPage.search(self.data.get('user_re').get('accountUsername'))
        if accountMainPage.checkupTableData({'accountUsername':self.data.get('user_re').get('accountUsername')}):
            pass
        else:
            accountMainPage.createAccount(self.data.get('user_re'))
    
    def custom_step(self):
        # LoginPage().loginSu()
        accountMainPage = AccountMainPage()
        accountMainPage.enterFunction()
        accountMainPage.modifyAccount(self.data.get('user_modify'))
        accountMainPage.search(self.data.get('user_modify').get('accountUsername'))
        return accountMainPage.checkupTableData(self.data.get('user_modify'))

    def custom_tearDown(self):
        # LoginPage().loginSu()
        accountMainPage = AccountMainPage()
        accountMainPage.enterFunction()
        accountMainPage.modifyAccount(self.data.get('user_re'))
        accountMainPage.search(self.data.get('user_re').get('accountUsername'))
        return accountMainPage.checkupTableData(self.data.get('user_re'))

if __name__ == '__main__':
    unittest.main()
