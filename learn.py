

import requests
import json

def login():
    url = 'http://192.168.0.94/qbxxpt/auth/login'
    
    header = {
        'Referer': 'http://192.168.0.94/',
    }
    
    data = {
        'captchaText':'11111',
        'loginId':'990-1567064706462',
        'passwd':'11',
        'user_name':'su'
    }
    
    ret = requests.post(url=url,headers=header,data=data)
    print(ret.status_code)
    print(ret.headers)
    print(ret.headers.get('authorization'))
    return ret.headers.get('authorization')
    


def test(auth):
    url = 'http://192.168.0.93/qbxxpt/roles/list'

    header = {
        'authorization':auth,
        'Referer': 'http://192.168.0.93/'
    }

    
    data = {
        'currentPageNo':1,
        'pageSize':10,
        'searchContent':''
    }
    
    print(header)
    ret = requests.post(url=url, headers=header,data=json.dumps(data))
    print(ret.text)

def fun1():
    import xlrd
    fun_file = xlrd.open_workbook('D:\test.xlsx')
    fun_sheet = fun_file.sheet_by_index(0)
    fun_sheet.dump()

auth = login()
# test(auth)









# import os
# def findAllSubFile(dir):
#     fileList = []
#     for subFile in os.listdir(dir):
#         if os.path.isfile(os.path.join(dir, subFile)):
#             fileList.append(os.path.join(dir, subFile))
#         else:
#             subFileList = findAllSubFile(os.path.join(dir, subFile))
#             fileList += subFileList
#     return fileList

# from framework.tool.tool import *
# import re
# path = r'D:\workspace\JCWAutoTest\testJCW\data'
# l = findAllSubFile(path)
# # pattern = re.compile('[JCWAutoTest]([0012]|[0013])')
# # pattern = re.compile('[JCWAutoTest]')
# pattern = re.compile('[JCWAutoTest](0012|0014|0018)')
# for li in l :
#     if re.search(pattern=pattern,string=li):
#         print(li)
#
#




