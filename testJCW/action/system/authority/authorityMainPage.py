# -*- coding:utf-8 -*-
'''
@File   : authorityPage.py
@Author : 
@Date   : 2019/7/14 16:14
@Desc   :
'''
from testJCW.action.system.systemMainPage import SystemMainPage
from testJCW.base.htmlButton import HtmlButton
from framework.superClass.htmlElement import HtmlElement
from framework.tool.tool import *
from framework.logger.logger import logger
from testJCW.base.htmlSelect import HtmlSelect
from testJCW.base.htmlText import HtmlText
from framework.driver.driver import DR
from testJCW.base.htmlTable import HtmlTable
from testJCW.base.htmlModule import HtmlModule
from testJCW.base.htmlCheckbox import HtmlCheckbox
from testJCW.base.htmlTree import HtmlTree
from testJCW.base.htmlMenu import HtmlMenu

class AuthorityMainPage(SystemMainPage):
    
    def __init__(self):
        super(AuthorityMainPage, self).__init__()
        self.leftMenu = 'authority'

    def enterFunction(self):
        self.enterTopMenu('系统管理')
        if not self.enterLeftMenu('权限管理'):
            raise Exception('enter page failed')

    def selectOrganize(self,organize):
        oganize_selector = ['id',self.getIdSuffix('select','organize')]
        HtmlButton(HtmlElement(selector1=oganize_selector).element.find_elements_by_tag_name('span')[2]).clickBtn()
    
        oganize1_selector = ['xpath','/html/body/div[2]/ul/li']
        HtmlButton(selector1=oganize1_selector).clickBtn()
        
        oganize2_selector = ['xpath','/html/body/div[2]/ul[2]']
        HtmlSelect(selector1=oganize2_selector).selectLiByText(organize.get('organize3'))

        if HtmlMenu(selector1=oganize2_selector).element.is_displayed():
            HtmlButton(HtmlElement(selector1=oganize_selector).element.find_elements_by_tag_name('span')[2]).clickBtn()
        
    def selectUser(self,userName):
        tree_selector = ['id',self.getIdSuffix('tree','adminDeptUser')]
        tree = HtmlTree(selector1=tree_selector)
        tree.selectDivByText(userName)
        
    def clickEditBtn(self):
        btn_selector = ['id',self.getIdSuffix('button','editAuthority')]
        HtmlButton(selector1=btn_selector).clickBtn()
        sleep(2)
        
    def checkboxAllAuthority(self):
        checkbox_selector = ['id',self.getIdSuffix('checkbox','allAuthority')]
        if self.checkUpAllAuthority():
            HtmlCheckbox(selector1=checkbox_selector).check()
            sleep(1)
            HtmlCheckbox(selector1=checkbox_selector).check()
        else:
            HtmlCheckbox(selector1=checkbox_selector).check()

        sleep(2)
    
    def clickSaveBtn(self):
        btn_selector = ['id', self.getIdSuffix('button', 'saveEditAuthority')]
        HtmlButton(selector1=btn_selector).clickBtn()
        sleep(1)
    
    def setAllAuthority(self):
        self.clickEditBtn()
        self.checkboxAllAuthority()
        self.clickSaveBtn()
    
    def checkUpAllAuthority(self):
        checkbox_selector = ['id', self.getIdSuffix('checkbox', 'allAuthority')]
        return 'is-checked' in HtmlCheckbox(selector1=checkbox_selector).element.get_attribute('innerHTML')
    