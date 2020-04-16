from framework.logger.logger import logger
from testJCW.base.htmlButton import *
from testJCW.base.htmlText import *
from framework.driver.driver import DR
from framework.config.dynamic import *
class LoginPage():

    def __init__(self):
        self.address = ''

    def loginSu(self):
        self.login(USER,PWD)

    def login_data(self,data):
        self.login(data.get('user'),data.get('pwd'))

    def reLogin(self,data):
        self.login_data(data)

    def login(self,user,pwd,targetAddress = None):
        DR.get(LOGIN_ADDRESS)
        login_url = DR.current_url
        
        userText = HtmlText(selector1=['css_selector', 'div.input-wrapper:nth-child(3) > input:nth-child(2)'])
        userText.setText(user)

        pwdText = HtmlText(selector1=['css_selector', 'div.input-wrapper:nth-child(4) > input:nth-child(2)'])
        pwdText.setText(pwd)

        try:
            verificationCodeText = HtmlText(selector1=['css_selector','div.input-wrapper:nth-child(6) > input:nth-child(1)'])
            verificationCodeText.setText('11111')
        except:
            pass

        loginBtn = HtmlButton(selector1=['css_selector','.el-button'])
        loginBtn.clickBtn()

        for i in range(30):
            if DR.current_url == login_url:
                logger.info('logging in ,wait pls')
                sleep(0.5)
            else:
                logger.info('successful login ')
                break

        if targetAddress:
            for i in range(3):

                if DR.current_url == targetAddress:
                    logger.info('login to the homepage %s success '%(targetAddress))
                    return True
                else:
                    sleep(2)
            logger.error('login to the homepage failed')
            return False
            # raise Exception('login to the homepage failed')

if __name__ == '__main__':
    DR.get('http://192.168.0.93:81')
    LoginPage().login('su','11')
    DR.quit()
    
    
    
    