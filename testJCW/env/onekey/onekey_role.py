# -*- coding:utf-8 -*-
'''
@File   : onekey_role.py
@Author : 
@Date   : 2019/8/13 9:59
@Desc   :
'''

from testJCW.action.loginPage import LoginPage
from testJCW.action.system.role.roleMainPage import RoleMainPage
from framework.logger.logger import logger

class EnvInt_role():
    
    role_list = [{'roleName': '内勤', 'roleDesc': '内勤', 'roleLevel': '1'},
                {'roleName': '科员', 'roleDesc': '科员', 'roleLevel': '2'},
                {'roleName': '主任', 'roleDesc': '主任', 'roleLevel': '3'},
                {'roleName': '分管常委', 'roleDesc': '分管常委', 'roleLevel': '4'},
                {'roleName': '分管书记', 'roleDesc': '分管书记', 'roleLevel': '5'},
                {'roleName': '书记', 'roleDesc': '书记', 'roleLevel': '9'}]
    
    def create_role(self):
        LoginPage().loginSu()
        roleMainPage = RoleMainPage()
        roleMainPage.enterFunction()
        for role in self.role_list:
            try:
                roleMainPage.createRole(role)
            except:
                pass
            finally:
                try:
                    roleMainPage.clickclose()
                except:
                    pass
if __name__ == '__main__':
    EnvInt_role().create_role()




