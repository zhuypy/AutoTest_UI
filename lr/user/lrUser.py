# -*- coding:utf-8 -*-
'''
@File   : lrUser.py
@Author : 
@Date   : 2007/8/29 15:41
@Desc   :
'''

import requests

HOST = "192.168.0.191:3000"

def login():
    
    url = "http://"+HOST+"/qbxxpt/auth/login"
    querystring = {"user_name": "hbadmin", "passwd": "11", "captchaText": "11111", "loginId": "1541-1568096354263"}
    headers = {
        'Referer': "http://"+HOST+"/",
        'Host': HOST,
        'User-Agent': "PostmanRuntime/7.13.0",
        'Accept': "*/*",
        'Cache-Control': "no-cache",
        'Postman-Token': "883caa05-079f-4ed8-965a-d66174537886,b0fcf648-b7ec-4386-b0db-28c36fb68476",
        'accept-encoding': "gzip, deflate",
        # 'content-length': "",
        'Connection': "keep-alive",
        'cache-control': "no-cache"
    }
    response = requests.request("POST", url, headers=headers, params=querystring)
    # print(response.headers)
    return response.headers.get("authorization")

def addUser(authorization,number):
    url =  "http://"+HOST+"/qbxxpt/dept/addDeptRoleUserNew"
    payload = "{\"user_name\":\"per"+number+"\",\"name\":\"per"+number+"\",\"id_card\":\"\",\"user_no\":\"\",\"mobile\":\"\",\"passwd\":\"11\",\"city_no\":\"\",\"email\":\"\",\"confirmPasswd\":\"11\",\"address\":\"\",\"memo\":\"\",\"is_valid\":1,\"duty\":\"\",\"is_admin\":0,\"org_id\":\"\",\"score\":26,\"deptId\":\"125\",\"roleId\":\"2\"}"
    headers = {
        'Content-Type': "application/json",
        'authorization': "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoiMTQwIiwiZXhwIjoxNTY4NzE0NDEzfQ.8yHdLpMEzXIpUXCjfWYxSWgLSr1veYhW_BDUiDQD840",
        'Referer': "http://"+HOST+"/",
        'cache-control': "no-cache",
        'Postman-Token': "86ece049-0826-4926-b3fe-2d06f21f3945"
    }
    response = requests.request("POST", url, data=payload, headers=headers)
    

def enableUser(authorization,user_id):
    url = "http://"+HOST+"/qbxxpt/users/batchUpdate"
    payload = "ids="+str(user_id)+"&is_valid=1"
    headers = {
        'authorization': authorization,
        'Referer': "http://"+HOST+"/",
        'Content-Type': "application/x-www-form-urlencoded",
        'User-Agent': "PostmanRuntime/7.13.0",
        'Accept': "*/*",
        'Cache-Control': "no-cache",
        'Postman-Token': "fb51b8e4-beb4-47e2-a6c9-d1b23186f5fb,578892ae-c4b4-4681-aff5-a29860f6a0bf",
        'Host': HOST,
        'accept-encoding': "gzip, deflate",
        'content-length': "18",
        'Connection': "keep-alive",
        'cache-control': "no-cache"
    }
    response = requests.request("POST", url, data=payload, headers=headers)
    print(response.json().get("msg"))

def getUserIdByOrgId(authorization,username):
    import requests
    url = "http://"+HOST+"/qbxxpt/users/list"
    payload = "{\"searchContent\":\"\",\"pageSize\":20000,\"currentPageNo\":1,\"org_id\":-1}"
    headers = {
        'authorization': authorization,
        'Referer': "http://"+HOST+"/",
        'Content-Type': "application/json",
        'User-Agent': "PostmanRuntime/7.13.0",
        'Accept': "*/*",
        'Cache-Control': "no-cache",
        'Postman-Token': "2db17b11-03fa-40c7-ab06-fa70d99c58f7,daa81f52-5a73-475a-addd-a9e9e1d16f9d",
        'Host': HOST,
        'accept-encoding': "gzip, deflate",
        'content-length': "67",
        'Connection': "keep-alive",
        'cache-control': "no-cache"
    }
    response = requests.request("POST", url, data=payload, headers=headers)
    users = response.json().get("data").get("dataRows")
    for user in users:
        if user.get("user_name") == username:
            return user.get("user_id")


for i in range(1,20001):
    user_number = str(i).zfill(5)
    authorization = login()
    user_name = "per"+user_number
    print(user_name)
    
    addUser(authorization,user_number)
    # user_id = getUserIdByOrgId(authorization,user_name)
    # enableUser(authorization,user_id)


# print(getUserIdByOrgId(login(),"per0001"))




