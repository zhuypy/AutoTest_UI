from selenium import webdriver
from framework.config.dynamic import *
class Driver():
    '''
        singleton mode,ensure that the browser operated by the user is always the same
    '''

    # def __new__(cls,*args,**kw):
    #     '''
    #     :param args:
    #     :param kw:
    #     :return:
    #     '''
    #     if not hasattr(cls,'_instance'):
    #         cls._instance = object.__new__(cls)
    #     return cls._instance

    def __new__(cls, browserType):
        browser = cls.getBrowser(browserType)
        browser.maximize_window()
        return browser

    @classmethod
    def getBrowser(self,browserType):
        if browserType in ['Firefox','F']:
            return webdriver.Firefox()
        elif browserType in ['Ie','I']:
            return webdriver.Ie()
        elif browserType in ['Chrome','C']:
            return webdriver.Chrome()
        else:
            print('invalid DriverType')
            return None

DR = Driver(BROWSER_TYPE)




