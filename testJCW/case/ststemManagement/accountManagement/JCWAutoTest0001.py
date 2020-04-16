# -*- coding:utf-8 -*-
'''
@File   : JCWAutoTest0001.py
@Author : zhuy
@Date   : 2019/5/19 16:44
@Desc   :
'''

import unittest
from framework.superClass.jcwCase import JcwCase
from testJCW.action.loginPage import LoginPage
from testJCW.action.system.user.accountMainPage import AccountMainPage
from testJCW.action.system.authority.authorityMainPage import AuthorityMainPage

class JCWAutoTest0001(JcwCase, unittest.TestCase):
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
        LoginPage().loginSu()
        accountMainPage = AccountMainPage()
        accountMainPage.enterFunction()
        accountMainPage.createAccount(self.data.get('userData'))
        accountMainPage.search(self.data.get('userData').get('accountUsername'))
        return accountMainPage.checkupTableData(self.data.get('userData'))

    def custom_tearDown(self):
        authorityMainPage = AuthorityMainPage()
        authorityMainPage.enterFunction()
        authorityMainPage.selectOrganize(self.data.get('organize'))
        authorityMainPage.selectUser(self.data.get('user').get('userName'))
        authorityMainPage.setAllAuthority()

if __name__ == '__main__':
    unittest.main()





