# -*- coding:utf-8 -*-
'''
@File   : htmlCheckbox.py
@Author : 
@Date   : 2019/5/16 15:18
@Desc   :
'''

from framework.superClass.htmlElement import HtmlElement
from framework.tool.tool import *
class HtmlCheckbox(HtmlElement):
    
    def check(self):
        self.element.click()
        sleep(0.5)