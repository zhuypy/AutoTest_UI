# -*- coding:utf-8 -*-
'''
@File   : JCWAutoTest0018.py
@Author : zhuy
@Date   : 2019/7/17 9:18
@Desc   :
'''

import unittest
from framework.superClass.jcwCase import JcwCase
from testJCW.action.loginPage import LoginPage
from testJCW.action.system.role.roleMainPage import RoleMainPage


class JCWAutoTest0019(JcwCase, unittest.TestCase):
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
        
        roleMainPage = RoleMainPage()
        roleMainPage.enterFunction()
        row = {'rolename': self.data.get('createRole').get('roleName')}
        roleMainPage.search(self.data.get('createRole').get('roleName'))
        if not roleMainPage.checkupTableData(row):
            roleMainPage.createRole(self.data.get('createRole'))

    
    def custom_step(self):
        roleMainPage = RoleMainPage()
        roleMainPage.enterFunction()
        roleMainPage.search(self.data.get('queryRole').get('roleName'))
        return roleMainPage.checkupTableData(self.data.get('queryRole'))
        

    def custom_tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
    
