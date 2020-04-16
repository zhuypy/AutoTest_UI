# -*- coding:utf-8 -*-
'''
@File   : onekey.py
@Author : 
@Date   : 2019/7/19 11:03
@Desc   :
'''

from testJCW.action.loginPage import LoginPage
from testJCW.action.system.user.accountMainPage import AccountMainPage
from framework.logger.logger import logger

class EnvInt_user():
    
    table_oganize = {'hb':'湖北','wh':'武汉','ez':'鄂州','hy':'汉阳','wc':'武昌','hr':'华容','qs':'青山'}
    
    def __init__(self,oganize):
        oganize_ch = self.table_oganize.get(oganize)

        common_pwd = '11'
        
        self.admin_user = oganize + 'admin'
        self.admin_pwd = common_pwd
        
        
        self.xxnq = {}
        self.xxnq['accountType'] = '普通用户'
        self.xxnq['accountUsername'] = oganize + 'xxnq'
        self.xxnq['accountName'] = oganize_ch + '信息内勤'
        self.xxnq['accountPassword'] = common_pwd
        self.xxnq['accountConfiremPassword'] = self.xxnq.get('accountPassword')
        
        self.xxky1 = {}
        self.xxky1['accountType'] = '普通用户'
        self.xxky1['accountUsername'] = oganize + 'xxky1'
        self.xxky1['accountName'] = oganize_ch + '信息科员1'
        self.xxky1['accountPassword'] = common_pwd
        self.xxky1['accountConfiremPassword'] = self.xxky1.get('accountPassword')
        
        self.xxky2 = {}
        self.xxky2['accountType'] = '普通用户'
        self.xxky2['accountUsername'] = oganize + 'xxky2'
        self.xxky2['accountName'] = oganize_ch + '信息科员2'
        self.xxky2['accountPassword'] = common_pwd
        self.xxky2['accountConfiremPassword'] = self.xxky2.get('accountPassword')
        
        self.xxzr = {}
        self.xxzr['accountType'] = '普通用户'
        self.xxzr['accountUsername'] = oganize + 'xxzr'
        self.xxzr['accountName'] = oganize_ch + '信息主任'
        self.xxzr['accountPassword'] = common_pwd
        self.xxzr['accountConfiremPassword'] = self.xxzr.get('accountPassword')
        
        self.scnq = {}
        self.scnq['accountType'] = '普通用户'
        self.scnq['accountUsername'] = oganize + 'scnq'
        self.scnq['accountName'] = oganize_ch + '审查内勤'
        self.scnq['accountPassword'] = common_pwd
        self.scnq['accountConfiremPassword'] = self.scnq.get('accountPassword')
        
        self.scky1 = {}
        self.scky1['accountType'] = '普通用户'
        self.scky1['accountUsername'] = oganize + 'scky1'
        self.scky1['accountName'] = oganize_ch + '审查科员1'
        self.scky1['accountPassword'] = common_pwd
        self.scky1['accountConfiremPassword'] = self.scky1.get('accountPassword')
        
        self.scky2 = {}
        self.scky2['accountType'] = '普通用户'
        self.scky2['accountUsername'] = oganize + 'scky2'
        self.scky2['accountName'] = oganize_ch + '审查科员2'
        self.scky2['accountPassword'] = common_pwd
        self.scky2['accountConfiremPassword'] = self.scky2.get('accountPassword')
        
        self.sczr = {}
        self.sczr['accountType'] = '普通用户'
        self.sczr['accountUsername'] = oganize + 'sczr'
        self.sczr['accountName'] = oganize_ch + '审查主任'
        self.sczr['accountPassword'] = common_pwd
        self.sczr['accountConfiremPassword'] = self.sczr.get('accountPassword')
        
        self.xxcw = {}
        self.xxcw['accountType'] = '普通用户'
        self.xxcw['accountUsername'] = oganize + 'xxcw'
        self.xxcw['accountName'] = oganize_ch + '信息常委'
        self.xxcw['accountPassword'] = common_pwd
        self.xxcw['accountConfiremPassword'] = self.xxcw.get('accountPassword')
        
        self.sccw = {}
        self.sccw['accountType'] = '普通用户'
        self.sccw['accountUsername'] = oganize + 'sccw'
        self.sccw['accountName'] = oganize_ch + '审查常委'
        self.sccw['accountPassword'] = common_pwd
        self.sccw['accountConfiremPassword'] = self.sccw.get('accountPassword')
        
        self.xxsj = {}
        self.xxsj['accountType'] = '普通用户'
        self.xxsj['accountUsername'] = oganize + 'xxsj'
        self.xxsj['accountName'] = oganize_ch + '信息书记'
        self.xxsj['accountPassword'] = common_pwd
        self.xxsj['accountConfiremPassword'] = self.xxsj.get('accountPassword')
        
        self.scsj = {}
        self.scsj['accountType'] = '普通用户'
        self.scsj['accountUsername'] = oganize + 'scsj'
        self.scsj['accountName'] = oganize_ch + '审查书记'
        self.scsj['accountPassword'] = common_pwd
        self.scsj['accountConfiremPassword'] = self.scsj.get('accountPassword')
        
        self.sj = {}
        self.sj['accountType'] = '普通用户'
        self.sj['accountUsername'] = oganize+'sj'
        self.sj['accountName'] = oganize_ch+'书记'
        self.sj['accountPassword'] = common_pwd
        self.sj['accountConfiremPassword'] = self.sj.get('accountPassword')
        
        LoginPage().login(user=self.admin_user,pwd=self.admin_pwd)
        self.page = AccountMainPage()
        self.page.enterFunction()
        
    def createAccount(self,data):
        try :
            self.page.createAccount(data)
            self.page.ableRow({'accountUsername':data.get('accountUsername')})
            self.takeNotes('create [%s] success'%(data))
        except:
            self.takeNotes('create [%s] failed'%(data))
        finally:
            try:
                self.page.clickclose()
            except:
                pass
    
    def takeNotes(self,msg):
        file='D:\测试日志\账号新建结果.txt'
        logger.writeTextFile(msg=msg,file=file,pureMode=True)
    
    def createAll(self):
        self.createAccount(self.xxnq)
        self.createAccount(self.xxky1)
        self.createAccount(self.xxky2)
        self.createAccount(self.xxzr)
        self.createAccount(self.scnq)
        self.createAccount(self.scky1)
        self.createAccount(self.scky2)
        self.createAccount(self.sczr)
        self.createAccount(self.xxcw)
        self.createAccount(self.sccw)
        self.createAccount(self.xxsj)
        self.createAccount(self.scsj)
        self.createAccount(self.sj)
        
if __name__ == '__main__':
    EnvInt_user('hb').createAll()
    EnvInt_user('wh').createAll()
    EnvInt_user('ez').createAll()
    EnvInt_user('hr').createAll()
    EnvInt_user('wc').createAll()
    EnvInt_user('hy').createAll()
    EnvInt_user('qs').createAll()








