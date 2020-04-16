# -*- coding:utf-8 -*-
'''
@File   : roleMainPage.py
@Author : 
@Date   : 2019/6/5 14:49
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
class RoleMainPage(SystemMainPage):
    def __init__(self):
        super(RoleMainPage,self).__init__()
        self.leftMenu = 'role'
        
    def enterFunction(self):
        self.enterTopMenu('系统管理')
        if not self.enterLeftMenu('角色管理'):
            raise Exception('enter page failed')

    def clickAddBtn(self):
        selector = ['id',self.getIdSuffix('button','addRole')]
        HtmlButton(selector1=selector).clickBtn()
        
    def clickSaveBtn(self):
        selector = ['id', self.getIdSuffix('button', 'roleSave')]
        HtmlButton(selector1=selector).clickBtn()
        
        
    def clickclose(self):
        selector = ['css_selector','#system_role_modal_showAddRole > div:nth-child(1) > div:nth-child(1) > button:nth-child(2)']
        HtmlButton(selector1=selector).clickBtn()
    
    def waitForDialog(self,expect_title):
        for i in range(10):
            try:
                title = HtmlModule(selector1=['xpath',"//div[@id='system_role_modal_showAddRole']/div/div[1]/span"]).element.text
                logger.debug('dialog title is %s'%(title))
            except:
                sleep(0.5)
                continue

            if title == expect_title:
                logger.info('open dailog of %s success' % (expect_title))
                return True
            else:
                sleep(0.5)
        logger.error('open dailog of %s fail'%(expect_title))
        return False

        
    def editRow(self,key_value):
        self.search(key_value[1])
        HtmlButton(selector1=['name', self.getIdSuffix('buttons', '0_editRole')]).clickBtn()
        
    def search(self,keyword):
        logger.info('search %s'%(keyword))
        selector_text = ['id',self.getIdSuffix('input','text')]
        selector_btn = ['id',self.getIdSuffix('button','search')]
        HtmlText(selector1=selector_text).setText(keyword)
        HtmlButton(selector1=selector_btn).clickBtn()

    def modifyRole(self, testData):
        self.editRow(['roleName', testData.get('roleName')])
        # self.waitForDialog('编辑角色')
        self.waitForDialog('添加角色')
        self.setDialog(testData)
        self.clickSaveBtn()

    def setDialog(self, testData):
        roleName_selector = ['id', self.getIdSuffix('input','roleName')]
        roleDesc_selector = ['id', self.getIdSuffix('input','roleDesc')]
        roleLevel_selector = ['id', self.getIdSuffix('input','roleLevel')]
        
        for key in testData:
            if key == 'roleName':
                ret = HtmlText(selector1=roleName_selector).setText(testData.get(key))
            elif key == 'roleDesc':
                ret = HtmlText(selector1=roleDesc_selector).setText(testData.get(key))
            elif key == 'roleLevel':
                ret = HtmlText(selector1=roleLevel_selector).setText(testData.get(key))
            else:
                ret = False
                logger.error('invalid parameter %s' % (key))

            if ret:
                logger.info('set %s:%s success' % (key, testData.get(key)))
            else:
                logger.error('set %s:%s fail' % (key, testData.get(key)))
        
    
    def createRole(self,testData):
        self.clickAddBtn()
        self.waitForDialog('添加角色')
        self.setDialog(testData)
        self.clickSaveBtn()
    
    def getTableData(self,):
        table_selector = ['id',self.getIdSuffix('table','roleList')]
        table = HtmlTable(selector1=table_selector)
        return table.getTableData()

    def checkupTableData(self,expect_data):
        conversionRules = {'角色名称':'roleName','角色描述':'roleDesc','角色级别':'roleLevel'}
        actual_datas = self.getTableData()
        for actual_data in actual_datas:
            ret,sameDict = compareDict(expect_data,convertDict(actual_data,conversionRules))
            if ret != -1 and ret != -2:
                logger.info('sameDict is : %s'%(sameDict))
                return True
            elif ret == -1:
                logger.info('diffDict is : %s'%(sameDict))
                return False
            else:
                pass # placeholder
        return False