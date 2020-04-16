# -*- coding:utf-8 -*-
'''
@File   : testInterface.py
@Author : 
@Date   : 2019/8/8 16:04
@Desc   :
'''

import requests

class InterfaceFun():
    def test(self,funType,url,param=None,data=None,json=None):
        if funType == 'get':
            ret = requests.get(url=url,params=param)
        elif type == 'post':
            ret = requests.post(url=url, data=data, json=json)
        else:
            ret = None
        
        return ret
if __name__ == '__main__':
    interfaceFun = InterfaceFun()
    funType = 'get'
    url = 'http://192.168.0.93/#/'
    ret = interfaceFun.test(funType,url)
    print(ret.text)










