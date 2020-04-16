# -*- coding:utf-8 -*-
'''
@File   : htmlMenu.py
@Author : 
@Date   : 2019/5/14 19:19
@Desc   :
'''

from framework.superClass.htmlElement import HtmlElement
from framework.tool.tool import *
from selenium.common.exceptions import ElementClickInterceptedException
class HtmlMenu(HtmlElement):

    def enterMenu(self,menuName,selector=None):
        if not selector :
            self.clickMenu(menuName)
            sleep(0.5)
            self.clickMenu(menuName)
            sleep(0.5)
        else:
            menus = self.getElements(selector)
            for menu in menus:
                if menu.text == menuName:
                    menu.click()
        sleep(1)


    def clickMenu(self,menuName):
        for i in range(10):
            try:
                self.element.find_element_by_link_text(menuName).click()
                return True
            except ElementClickInterceptedException as e:
                sleep(0.5)

if __name__ == '__main__':
    pass


