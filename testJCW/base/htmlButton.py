# -*- coding:utf-8 -*-
'''
@File   : htmlButton.py
@Author : 
@Date   : 2019/5/13 14:45
@Desc   :
'''

from framework.superClass.htmlElement import HtmlElement
from framework.tool.tool import *
class HtmlButton(HtmlElement):


    def clickBtn(self):
        for i in range(3):
            if self.element.is_displayed() and self.element.is_enabled():
                self.element.click()
                sleep(0.5)
                break
            else :
                raise Exception('element not displayed')

    def clickBtnByText(self,text,selector=None):
        if not selector:
            elements = self.getElements(['tag_name','button'])
        else:
            elements = self.getElements(selector)
        for element in elements:
            if (element.text == text) or (element.get_attribute('link_text') == text):
                self.element = element
        self.clickBtn()
#
# if __name__ == '__main__':
#     selector = ['id','SYSTEM_USER_button_addAccount']
#     HtmlButton(selector1=selector).clickBtn()



