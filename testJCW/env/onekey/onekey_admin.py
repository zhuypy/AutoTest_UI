# -*- coding:utf-8 -*-
'''
@File   : onkey_admin.py
@Author : 
@Date   : 2019/8/4 14:11
@Desc   :
'''

from testJCW.action.loginPage import LoginPage
from testJCW.action.system.user.accountMainPage import AccountMainPage
from testJCW.action.system.authority.authorityMainPage import AuthorityMainPage
from framework.logger.logger import logger


class EnvInt_admin():
    table_oganize = {'hb': '湖北', 'wh': '武汉', 'ez': '鄂州', 'hy': '汉阳', 'wc': '武昌', 'hr': '华容','qs':'青山'}
    table_oganizeTree = {'hb': {'organize3':'湖北'}, 'wh': {'organize3':'武汉'}, 'ez': {'organize3':'鄂州'}, 'hy': {'organize3':'汉阳'}, 'wc': {'organize3':'武昌'}, 'hr': {'organize3':'华容'},'qs':{'organize3':'青山'}}
    common_pwd = '11'
    
    def __init__(self,):
        pass
        
    def initAdmin(self,oganize):
        oganize_ch = self.table_oganize.get(oganize)
        oganize_tree = self.table_oganizeTree.get(oganize)
        admin_user = oganize + 'admin'
        admin_pwd = '11'
    
        admin = {}
        admin['accountType'] = '用户管理员'
        admin['accountOrgId'] = oganize_ch
        admin['accountUsername'] = oganize + 'admin'
        admin['accountName'] = oganize_ch + '管理员'
        admin['accountPassword'] = self.common_pwd
        admin['accountConfiremPassword'] = admin.get('accountPassword')
        
        admin['oganize_ch'] = oganize_ch
        admin['oganize_tree'] = oganize_tree
        admin['admin_user'] = admin_user
        admin['admin_pwd'] = admin_pwd

        return admin
        
    def takeNotes(self,msg):
        file='D:\测试日志\账号新建结果.txt'
        logger.writeTextFile(msg=msg,file=file,pureMode=True)
        
    def createAccount(self,admin):
        accountPage = AccountMainPage()
        accountPage.enterFunction()
        try :
            accountPage.createAccount(admin)
            accountPage.ableRow({'accountUsername':admin.get('accountUsername')})
            self.takeNotes('create [%s] success'%(admin))
        except:
            self.takeNotes('create [%s] failed'%(admin))
        finally:
            try:
                accountPage.clickclose()
            except:
                pass
            
        authorityMainPage = AuthorityMainPage()
        authorityMainPage.enterFunction()
        try :
            authorityMainPage.selectOrganize(admin.get('oganize_tree'))
            authorityMainPage.selectUser(admin.get('accountUsername'))
            authorityMainPage.setAllAuthority()
            self.takeNotes('create [%s] success'%(admin))
        except:
            self.takeNotes('create [%s] failed'%(admin))
        finally:
            try:
                pass
            except:
                pass
            
    def createAll(self):
        LoginPage().loginSu()
        accountPage = AccountMainPage()
        accountPage.enterFunction()
        for i in self.table_oganize.keys():
            self.createAccount(self.initAdmin(i))
        # self.createAccount(self.initAdmin('qs'))
        
if __name__ == '__main__':
    EnvInt_admin().createAll()