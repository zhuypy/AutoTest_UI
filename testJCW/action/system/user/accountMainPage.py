# -*- coding:utf-8 -*-
'''
@File   : accountMainPage.py
@Author : 
@Date   : 2019/5/20 15:37
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
class AccountMainPage(SystemMainPage):
    def __init__(self):
        super(AccountMainPage,self).__init__()
        self.leftMenu = 'user'

    def enterFunction(self):
        self.enterTopMenu('系统管理')
        if not self.enterLeftMenu('账号管理'):
            raise Exception('enter page failed')

    def clickAddBtn(self):
        selector = ['id',self.getIdSuffix('button','addAccount')]
        HtmlButton(selector1=selector).clickBtn()

    def clickAbleBtn(self):
        selector = ['id', self.getIdSuffix('button', 'ableAccount')]
        HtmlButton(selector1=selector).clickBtn()

    def clickDisAbleBtn(self):
        selector = ['id', self.getIdSuffix('button', 'disableAccount')]
        HtmlButton(selector1=selector).clickBtn()

    def clickSaveBtn(self):
        selector = ['id',self.getIdSuffix('button','accountSave')]
        HtmlButton(selector1=selector).clickBtn()

    def clickclose(self):
        # selector = ['xpath','/html/body/div[1]/div/div[2]/section/section/section/main/div/div/div[3]/div/div[1]/button']
        selector = ['css_selector','#system_user_modal_showAddAccount > div:nth-child(1) > div:nth-child(1) > button:nth-child(2)']
        HtmlButton(selector1=selector).clickBtn()

    def search(self,keyword):
        logger.info('search %s'%(keyword))
        selector_text = ['id',self.getIdSuffix('input','text')]
        selector_btn = ['id',self.getIdSuffix('button','search')]
        HtmlText(selector1=selector_text).setText(keyword)
        HtmlButton(selector1=selector_btn).clickBtn()

    def editRow(self,key_value):
        self.search(key_value[1])
        HtmlButton(selector1=['name',self.getIdSuffix('buttons','0_editUser')]).clickBtn()

    def selectRow(self,row):
        self.search(row.get('accountUsername'))
        HtmlCheckbox(selector1=['xpath',"//button[@name='system_user_buttons_0_editUser']/../../../td[1]/div[1]/label"]).check()

    def waitForDialog(self,expect_title):
        for i in range(10):
            try:
                title = HtmlModule(selector1=['xpath',"//div[@id='system_user_modal_showAddAccount']/div/div[1]/span"]).element.text
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

    def setDialog(self,testData):
        accountType_selector = ['id', self.getIdSuffix('select','accountType')]
        accountOrgId_selector = ['id', self.getIdSuffix('select','accountOrgId')]
        accountUsername_selector = ['id', self.getIdSuffix('input','accountUsername')]
        accountName_selector = ['id', self.getIdSuffix('input','accountName')]
        accountPassword_selector = ['id', self.getIdSuffix('input','accountPassword')]
        accountConfiremPassword_selector = ['id', self.getIdSuffix('input','accountConfiremPassword')]
        accountIdcard_selector = ['id', self.getIdSuffix('input','accountIdcard')]
        accountMobile_selector = ['id', self.getIdSuffix('input','accountMobile')]
        accountEmail_selector = ['id', self.getIdSuffix('input','accountEmail')]
        accountAddress_selector = ['id', self.getIdSuffix('input','accountAddress')]
        accountMemo_selector = ['id', self.getIdSuffix('input','accountMemo')]

        for key in testData:
            if key == 'accountType':
                HtmlSelect(selector1=accountType_selector).element.click()
                ret = HtmlSelect(selector1=['xpath',"//li[@name='system_user_options_0_accountType']/.."]).selectLiByText(testData.get(key))
                if ret:
                    logger.info('set %s:%s success'%(key,testData.get(key)))
                else:
                    logger.error('set %s:%s fail'%(key,testData.get(key)))
            elif key == 'accountOrgId':
                HtmlSelect(selector1=accountOrgId_selector).element.click()
                ret = HtmlSelect(selector1=['xpath',"//li[@name='autotest_system_user_options_0_accountOrgId']/.."]).selectLiByText(testData.get(key))
                # ret = HtmlSelect(selector1=['xpath',"/html/body/div[3]/div[1]/div[1]/ul"]).selectLiByText(testData.get(key))
                if ret:
                    logger.info('set %s:%s success'%(key,testData.get(key)))
                else:
                    logger.error('set %s:%s fail'%(key,testData.get(key)))
            elif key == 'accountUsername':
                ret = HtmlText(selector1=accountUsername_selector).setText(testData.get(key))
                if ret:
                    logger.info('set %s:%s success'%(key,testData.get(key)))
                else:
                    logger.error('set %s:%s fail'%(key,testData.get(key)))
            elif key == 'accountName':
                ret = HtmlText(selector1=accountName_selector).setText(testData.get(key))
                if ret:
                    logger.info('set %s:%s success'%(key,testData.get(key)))
                else:
                    
                    logger.error('set %s:%s fail'%(key,testData.get(key)))
            elif key == 'accountPassword':
                ret = HtmlText(selector1=accountPassword_selector).setText(testData.get(key))
                if ret:
                    logger.info('set %s:%s success'%(key,testData.get(key)))
                else:
                    logger.error('set %s:%s fail'%(key,testData.get(key)))
            elif key == 'accountConfiremPassword':
                ret = HtmlText(selector1=accountConfiremPassword_selector).setText(testData.get(key))
                if ret:
                    logger.info('set %s:%s success'%(key,testData.get(key)))
                else:
                    logger.error('set %s:%s fail'%(key,testData.get(key)))
            elif key == 'accountIdcard':
                ret = HtmlText(selector1=accountIdcard_selector).setText(testData.get(key))
                if ret:
                    logger.info('set %s:%s success'%(key,testData.get(key)))
                else:
                    logger.error('set %s:%s fail'%(key,testData.get(key)))
            elif key == 'accountMobile':
                ret = HtmlText(selector1=accountMobile_selector).setText(testData.get(key))
                if ret:
                    logger.info('set %s:%s success'%(key,testData.get(key)))
                else:
                    logger.error('set %s:%s fail'%(key,testData.get(key)))
            elif key == 'accountEmail':
                ret = HtmlText(selector1=accountEmail_selector).setText(testData.get(key))
                if ret:
                    logger.info('set %s:%s success'%(key,testData.get(key)))
                else:
                    logger.error('set %s:%s fail'%(key,testData.get(key)))
            elif key == 'accountAddress':
                ret = HtmlText(selector1=accountAddress_selector).setText(testData.get(key))
                if ret:
                    logger.info('set %s:%s success'%(key,testData.get(key)))
                else:
                    logger.error('set %s:%s fail'%(key,testData.get(key)))
            elif key == 'accountMemo':
                ret = HtmlText(selector1=accountMemo_selector).setText(testData.get(key))
                if ret:
                    logger.info('set %s:%s success'%(key,testData.get(key)))
                else:
                    logger.error('set %s:%s fail'%(key,testData.get(key)))
            else:
                logger.error('invalid parameter %s'%(key))

    def createAccount(self,testData):
        self.clickAddBtn()
        self.waitForDialog('添加账号')
        self.setDialog(testData)
        self.clickSaveBtn()
        try:
            self.clickclose()
        except:
            logger.debug('close dialog failed')
        
    def modifyAccount(self,testData):
        self.editRow(['accountUsername',testData.get('accountUsername')])
        self.waitForDialog('编辑账号')
        self.setDialog(testData)
        self.clickSaveBtn()

    def ableRow(self,row):
        self.selectRow(row)
        self.clickAbleBtn()

    def disableRow(self,row):
        self.selectRow(row)
        self.clickDisAbleBtn()
        
    def getTableData(self,):
        table_selector = ['id',self.getIdSuffix('table','accountList')]
        table = HtmlTable(selector1=table_selector)
        return table.getTableData()

    def checkupTableData(self,expect_data):
        conversionRules = {'账号':'accountUsername','姓名':'accountName','身份证':'accountIdcard','手机号':'accountMobile','E-mail':'accountEmail','所属组织':'accountOrgId','备注':'accountMemo','状态':'accountState'}
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










