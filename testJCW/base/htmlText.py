# -*- coding:utf-8 -*-
'''
@File   : htmlText.py
@Author : 
@Date   : 2019/5/13 14:49
@Desc   :
'''

from framework.superClass.htmlElement import HtmlElement
from framework.tool.tool import *
from framework.logger.logger import *
class HtmlText(HtmlElement):


    # def setText(self,value):
    #     if self.element.is_displayed() and self.element.is_enabled():
    #         self.element.clear()
    #         sleep(0.5)
    #         self.element.send_keys(value)
    #         sleep(0.5)
    #         return True
    #     else:
    #         return False


    def setText(self,value):
        if self.element.is_displayed() and self.element.is_enabled():
            for i in range(3):
                self.element.clear()
                sleep(0.5)
                self.element.send_keys(value)
                sleep(0.5)
                if self.element.get_attribute('value') == value:
                    return True
                else:
                    sleep(0.5)
            return False
        else:
            return False


    def isText(self,):
        return self.element.tag_name == 'input'









