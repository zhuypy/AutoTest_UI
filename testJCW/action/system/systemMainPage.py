# -*- coding:utf-8 -*-
'''
@File   : systemMainPage.py
@Author : 
@Date   : 2019/5/20 14:28
@Desc   :
'''
from testJCW.action.mainPage import MainPage
from testJCW.base.htmlMenu import HtmlMenu
from framework.tool.tool import *
from framework.logger.logger import logger
class SystemMainPage(MainPage):

    def __init__(self):
        super(SystemMainPage,self).__init__()
        self.leftMenu_selector = ['class_name', 'el-menu']
        self.topMenu = 'system'

    def enterLeftMenu(self,menuName):
        menu = HtmlMenu(element = self.leftMenu_selector)
        for i in range(3):
            selector = ['class_name','menu-title']
            menu.enterMenu(menuName,selector)
            if self.isEnterMenuSuccess(menuName):
                return True
            sleep(0.5)
        return False

        