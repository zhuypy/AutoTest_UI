# -*- coding:utf-8 -*-
'''
@File   : mainPage.py
@Author : 
@Date   : 2019/5/20 14:29
@Desc   :
'''

from testJCW.base.htmlMenu import HtmlMenu
from framework.logger.logger import logger
from testJCW.base.htmlModule import HtmlModule
from framework.tool.tool import *
class MainPage():
    def __init__(self):
        self.topMenu_selector = ['class_name', 'menu-list']
        self.pageTag_selector = ['class_name', 'el-breadcrumb']

    def enterTopMenu(self, menuName):
        menu = HtmlMenu(selector1=self.topMenu_selector)
        for i in range(3):
            menu.enterMenu(menuName)
            if self.isEnterMenuSuccess(menuName):
                return True
            sleep(0.5)
        return False

    def isEnterMenuSuccess(self,menuName):
        tags = HtmlModule(selector1=self.pageTag_selector).element.find_elements_by_tag_name('span')
        for tag in tags:
            if tag.text == menuName:
                logger.info('the current page is %s ' % (menuName))
                return True
        logger.info('the enter top Menu fail %s ' % (menuName))
        return False

    def getIdSuffix(self,elementType,operate):
        return self.topMenu+'_'+self.leftMenu+'_'+elementType+'_'+operate

