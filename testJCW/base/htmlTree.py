# -*- coding:utf-8 -*-
'''
@File   : htmlTree.py
@Author : 
@Date   : 2019/7/26 11:19
@Desc   :
'''
from framework.superClass.htmlElement import HtmlElement
from framework.tool.tool import *

class HtmlTree(HtmlElement):
    def selectDivByText(self,text):
        '''
        select by text
        :param text:
        :return:
        '''
        list = self.element.find_elements_by_tag_name('div')
        for li in list :
            if li.text == text:
                li.click()
                sleep(0.5)
                return True
        return False
