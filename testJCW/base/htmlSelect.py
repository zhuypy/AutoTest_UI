# -*- coding:utf-8 -*-
'''
@File   : htmlSelect.py
@Author : 
@Date   : 2019/5/15 20:08
@Desc   :
'''

from framework.superClass.htmlElement import HtmlElement
from framework.tool.tool import *

class HtmlSelect(HtmlElement):

    def selectLiByText(self,text):
        '''
        select by text
        :param text:
        :return:
        '''
        list = self.element.find_elements_by_tag_name('li')
        for li in list :
            # print(li.text)
            try:
                if li.text == text or (text in li.text):
                    li.click()
                    sleep(0.5)
                    return True
            except:
                pass
        return False

    def selectByIndex(self,index):
        '''
        sselect by index
        :param index:int
        :return: None
        '''
        pass

    def selectByValue(self,Value):
        '''
        select by value
        :param Value:
        :return:
        '''
        pass

    def selectByText(self,text):

        if self.element.text == text:
            self.element.click()
            sleep(0.5)



