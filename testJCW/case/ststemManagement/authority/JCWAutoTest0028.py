# -*- coding:utf-8 -*-
'''
@File   : JCWAutoTest0028.py
@Author : zhuy
@Date   : 2019/7/25 9:38
@Desc   :
'''

import unittest
from framework.superClass.jcwCase import JcwCase
from testJCW.action.system.authority.authorityMainPage import AuthorityMainPage
from testJCW.action.loginPage import LoginPage

class JCWAutoTest0028(JcwCase, unittest.TestCase):
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
        authorityMainPage = AuthorityMainPage()
        authorityMainPage.enterFunction()
    
    def custom_step(self):
        authorityMainPage = AuthorityMainPage()
        authorityMainPage.selectOrganize(self.data.get('organize'))
        authorityMainPage.selectUser(self.data.get('user').get('userName'))
        authorityMainPage.setAllAuthority()

        authorityMainPage.selectOrganize(self.data.get('organize'))
        authorityMainPage.selectUser(self.data.get('user').get('userName'))
        return authorityMainPage.checkUpAllAuthority()
    
    def custom_tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
