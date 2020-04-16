# -*- coding:utf-8 -*-
'''
@File   : organizeMainPage.py
@Author : 
@Date   : 2007/8/23 15:43
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
class OrganizeMainPage(SystemMainPage):
    def __init__(self):
        super(OrganizeMainPage, self).__init__()
        self.leftMenu = 'organize'
    
    def enterFunction(self):
        self.enterTopMenu('系统管理')
        if not self.enterLeftMenu('组织管理'):
            raise Exception('enter page failed')

    def addOrganize(self,testData):
        self.clickEditBtn()
        self.clickAddBtn()
        self.waitForDialog('添加组织架构')
        self.setDialog(testData)
        self.clickSaveBtn()
        self.closePopWin()
        self.clickOK()

    def clickEditBtn(self):
        btn_selector = ['xpath','/html/body/div/div/div[2]/section/section/section/main/div/div/div[1]/div/div[1]/div[1]/span[2]/button']
        HtmlButton(selector1=btn_selector).clickBtn()
    
    def clickAddBtn(self):
        btn_selector = ['xpath', '/html/body/div/div/div[2]/section/section/section/main/div/div/div[1]/div/div[1]/div[1]/span[3]/button']
        HtmlButton(selector1=btn_selector).clickBtn()
    
    def setDialog(self,testData):
        name_selector = ['xpath', '/html/body/div[1]/div/div[2]/section/section/section/main/div/div/div[2]/div/div[2]/div/form/div[1]/div/div/input']
        superior_selector = ['xpath', '/html/body/div[1]/div/div[2]/section/section/section/main/div/div/div[2]/div/div[2]/div/form/div[2]/div/span/span']
        number_selector = ['xpath', '/html/body/div[1]/div/div[2]/section/section/section/main/div/div/div[2]/div/div[2]/div/form/div[3]/div/div/input']
        desc_selector = ['xpath', '/html/body/div[1]/div/div[2]/section/section/section/main/div/div/div[2]/div/div[2]/div/form/div[4]/div/div/input']
        telephone_selector = ['xpath', '/html/body/div[1]/div/div[2]/section/section/section/main/div/div/div[2]/div/div[2]/div/form/div[5]/div/div/input']
        address_selector = ['xpath', '/html/body/div[1]/div/div[2]/section/section/section/main/div/div/div[2]/div/div[2]/div/form/div[6]/div/div/input']
        addressCode_selector = ['xpath','/html/body/div[1]/div/div[2]/section/section/section/main/div/div/div[2]/div/div[2]/div/form/div[7]/div/div/div[1]/input']
        
        for key in testData:
            if key == 'name':
                ret = HtmlText(selector1=name_selector).setText(testData.get(key))
            elif key == 'superior':
                HtmlSelect(selector1=superior_selector).element.click()
                try:
                    ret = HtmlSelect(selector1=['xpath',"/html/body/div[4]/ul"]).selectLiByText(testData.get(key).get('superior1'))
                except:
                    ret = HtmlSelect(selector1=['xpath', "/html/body/div[3]/ul"]).selectLiByText(testData.get(key).get('superior1'))
                
                if testData.get(key).get('superior2'):
                    try:
                        ret = HtmlSelect(selector1=['xpath',"/html/body/div[3]/ul[2]"]).selectLiByText(testData.get(key).get('superior2'))
                    except:
                        ret = HtmlSelect(selector1=['xpath', "/html/body/div[4]/ul[2]"]).selectLiByText(testData.get(key).get('superior2'))
                    
                HtmlSelect(selector1=superior_selector).element.click()
                
            elif key == 'number':
                ret = HtmlText(selector1=number_selector).setText(testData.get(key))
            elif key == 'desc':
                ret = HtmlText(selector1=desc_selector).setText(testData.get(key))
            elif key == 'telephone':
                ret = HtmlText(selector1=telephone_selector).setText(testData.get(key))
            elif key == 'address':
                ret = HtmlText(selector1=address_selector).setText(testData.get(key))
            elif key == 'addressCode':
                HtmlSelect(selector1=addressCode_selector).element.click()
                ret = HtmlSelect(selector1=['xpath',"/html/body/div[4]/div[1]/div[1]/ul"]).selectLiByText(testData.get(key))
            else:
                ret = False
                logger.error('invalid parameter %s' % (key))
    
            if ret:
                logger.info('set %s:%s success' % (key, testData.get(key)))
            else:
                logger.error('set %s:%s fail' % (key, testData.get(key)))
    
    def waitForDialog(self,expect_title):
        for i in range(10):
            try:
                title = HtmlModule(selector1=['xpath',"/html/body/div[1]/div/div[2]/section/section/section/main/div/div/div[2]/div/div[1]/span"]).element.text
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
    
    def clickSaveBtn(self):
        btn_selector = ['xpath', '/html/body/div[1]/div/div[2]/section/section/section/main/div/div/div[2]/div/div[3]/span/button']
        HtmlButton(selector1=btn_selector).clickBtn()
    
    def closePopWin(self):
        try:
            btn_selector = ['xpath','/html/body/div[1]/div/div[2]/section/section/section/main/div/div/div[2]/div/div[1]/button']
            HtmlButton(selector1=btn_selector).clickBtn()
        except:
            pass

    def clickOK(self):
        btn_selector = ['xpath', '/html/body/div[1]/div/div[2]/section/section/section/main/div/div/div[1]/div/div[1]/div[1]/span[4]/button']
        HtmlButton(selector1=btn_selector).clickBtn()
        
        
        
        
        