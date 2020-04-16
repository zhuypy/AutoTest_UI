# -*- coding:utf-8 -*-
'''
@File   : onekey_organize.py
@Author : 
@Date   : 2019/8/13 10:00
@Desc   :
'''

from testJCW.action.loginPage import LoginPage
from testJCW.action.system.organize.organizeMainPage import OrganizeMainPage
from framework.logger.logger import logger


class EnvInt_organize():
    
    table_oganize = {'hb': '湖北', 'wh': '武汉', 'ez': '鄂州', 'hy': '汉阳', 'wc': '武昌', 'hr': '华容', 'qs': '青山'}

    info_oganize = {'hb':{'name':'湖北省纪律检查委员会','superior':{'superior1':'无',},'number':'001','desc':'湖北省纪律检查委员会','telephone':'13888888888','address':'湖北省','addressCode':'湖北'},
                    'wh':{'name':'武汉市纪律检查委员会','superior':{'superior1':'湖北',},'number':'002','desc':'武汉市纪律检查委员会','telephone':'13888888888','address':'武汉市','addressCode':'武汉'},
                    'ez':{'name':'鄂州市纪律检查委员会','superior':{'superior1':'湖北',},'number':'003','desc':'鄂州市纪律检查委员会','telephone':'13888888888','address':'鄂州市','addressCode':'鄂州'},
                    'hy':{'name':'汉阳区纪律检查委员会','superior':{'superior1':'湖北','superior2':'武汉'},'number':'004','desc':'汉阳区纪律检查委员会','telephone':'13888888888','address':'汉阳区','addressCode':'汉阳'},
                    'wc':{'name':'武昌区纪律检查委员会','superior':{'superior1':'湖北','superior2':'武汉'},'number':'005','desc':'武昌区纪律检查委员会','telephone':'13888888888','address':'武昌区','addressCode':'武昌'},
                    'hr':{'name':'华容区纪律检查委员会','superior':{'superior1':'湖北','superior2':'鄂州'},'number':'006','desc':'华容区纪律检查委员会','telephone':'13888888888','address':'华容区','addressCode':'华容'},
                    'qs':{'name':'青山区纪律检查委员会','superior':{'superior1':'湖北','superior2':'武汉'},'number':'007','desc':'青山区纪律检查委员会','telephone':'13888888888','address':'青山区','addressCode':'青山'}}

    def __init__(self,organize=None):
        if organize:
            self.data = self.info_oganize.get(organize)
    
    def addOrganize(self):
        LoginPage().loginSu()
        organizeMainPage = OrganizeMainPage()
        organizeMainPage.enterFunction()
        organizeMainPage.addOrganize(self.data)
        organizeMainPage.closePopWin()
    
    def createAll(self):
        LoginPage().loginSu()
        organizeMainPage = OrganizeMainPage()
        organizeMainPage.enterFunction()
        for key in self.info_oganize.keys():
            organizeMainPage.addOrganize(self.info_oganize.get(key))
            organizeMainPage.closePopWin()
        # organizeMainPage.addOrganize(self.info_oganize.get('wc'))
    
if __name__ == '__main__':
    EnvInt_organize().createAll()
    
    
    
    

    

