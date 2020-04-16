# -*- coding:utf-8 -*-
'''
@File   : deptMainPage.py
@Author : 
@Date   : 2019/7/26 15:07
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
class DeptMainPage(SystemMainPage):
    def __init__(self):
        super(DeptMainPage, self).__init__()
        self.leftMenu = 'dept'

    def enterFunction(self):
        self.enterTopMenu('系统管理')
        if not self.enterLeftMenu('部门管理'):
            raise Exception('enter page failed')

    def search(self, keyword):
        logger.info('search %s' % (keyword))
        selector_text = ['id', self.getIdSuffix('input', 'text')]
        selector_btn = ['id', self.getIdSuffix('button', 'search')]
        HtmlText(selector1=selector_text).setText(keyword)
        HtmlButton(selector1=selector_btn).clickBtn()
    
    def addLeader(self,userReaName,userRole):
        self.editRow('领导班子')
        
    def editRow(self,key_value):
        self.search(key_value[1])
        HtmlButton(selector1=['name',self.getIdSuffix('buttons','0_editDept')]).clickBtn()
    
    def addRoleToCurrentDept(self,role):
        self.clickAddRoleBtn()
        self.checkUpRole(role)
        self.waitForDialog_addRole()
    
    def createDept(self,testData):
        self.clickAddDept()
        self.waitForDialog_addDept('添加部门')
        self.setDialog_addDept(testData)
        self.clickSaveBtn()
    
    def ableDept(self,row):
        self.selectRow(row)
        self.clickAbleBtn()
        self.clickConfirmBtn()
        
    def disableDept(self,row):
        self.selectRow(row)
        self.clickDisAbleBtn()
        self.clickConfirmBtn()
    
    def clickConfirmBtn(self):
        HtmlButton(selector1=['xpath','/html/body/div[2]/div/div[3]/button[2]']).clickBtn()
    
    def selectRow(self,row):
        self.search(row.get('deptName'))
        HtmlCheckbox(selector1=['xpath',"//button[@name='system_dept_buttons_0_editDept']/../../../td[1]/div[1]/label"]).check()
    
    def checkUpRole(self,role):
        pass
    
    def clickAddRoleBtn(self):
        addRoleBtn_selector = ['id',self.getIdSuffix('input', 'addRoleGroup')]
        HtmlButton(selector1=addRoleBtn_selector).clickBtn()
        
    def clickAddDept(self):
        addRoleBtn_selector = ['id', self.getIdSuffix('button', 'addDept')]
        HtmlButton(selector1=addRoleBtn_selector).clickBtn()
    
    def clickSaveBtn(self):
        addRoleBtn_selector = ['id', self.getIdSuffix('button', 'deptSave')]
        HtmlButton(selector1=addRoleBtn_selector).clickBtn()
        
    def clickAbleBtn(self):
        addRoleBtn_selector = ['id', self.getIdSuffix('button', 'ableDept')]
        HtmlButton(selector1=addRoleBtn_selector).clickBtn()
    
    def clickDisAbleBtn(self):
        addRoleBtn_selector = ['id', self.getIdSuffix('button', 'disableDept')]
        HtmlButton(selector1=addRoleBtn_selector).clickBtn()
    
    def waitForDialog_addDept(self,expect_title):
        for i in range(10):
            try:
                title = HtmlModule(selector1=['xpath',"//div[@id='system_dept_model_addDept']/div/div[1]/span"]).element.text
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
    
    def waitForDialog_addRole(self,expect_title):
        for i in range(10):
            try:
                title = HtmlModule(selector1=['xpath',"//div[@id='system_editDept_modal_showAddPersonModel']/div/div[1]/span"]).element.text
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

    def setDialog_addDept(self,testData):
        deptName_selector = ['id', self.getIdSuffix('input', 'deptName')]
        deptLeader_selector = ['xpath', '/html/body/div[1]/div/div[2]/section/section/section/main/div/div/div[2]/div/div[2]/div/form/div[2]/div/div/div[2]/input']
        deptTel_selector = ['id', self.getIdSuffix('input', 'tel')]
        deptAddress_selector = ['id', self.getIdSuffix('input', 'address')]
        deptDesc_selector = ['id', self.getIdSuffix('input', 'desc')]
    
        for key in testData:
            if key == 'deptName':
                ret = HtmlText(selector1=deptName_selector).setText(testData.get(key))
            elif key == 'deptLeader':
                HtmlButton(selector1=deptLeader_selector).clickBtn()
                ret = HtmlSelect(selector1=['xpath','/html/body/div[3]/div[1]/div[1]/ul']).selectLiByText(testData.get(key))
            elif key == 'tel':
                ret = HtmlText(selector1=deptTel_selector).setText(testData.get(key))
            elif key == 'address':
                ret = HtmlText(selector1=deptAddress_selector).setText(testData.get(key))
            elif key == 'desc':
                ret = HtmlText(selector1=deptDesc_selector).setText(testData.get(key))
            else:
                ret = False
                logger.error('invalid parameter %s' % (key))
        
            if ret:
                logger.info('set %s:%s success' % (key, testData.get(key)))
            else:
                logger.error('set %s:%s fail' % (key, testData.get(key)))
    
    def getTableData(self,):
        table_selector = ['id',self.getIdSuffix('table','deptList')]
        table = HtmlTable(selector1=table_selector)
        return table.getTableData()

    def checkupTableData(self,expect_data):
        conversionRules = {'部门名称':'deptName','部门电话':'tel','分管领导':'deptLeader','地址':'address','备注':'desc','所属单位':'deptOrgId','状态':'deptState'}
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
    
    
    
    
    
    