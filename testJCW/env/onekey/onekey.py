# -*- coding:utf-8 -*-
'''
@File   : onekey.py
@Author : 
@Date   : 2007/8/23 15:36
@Desc   :
'''

from testJCW.env.onekey.onekey_admin import EnvInt_admin
from testJCW.env.onekey.onekey_user import EnvInt_user
from testJCW.env.onekey.onekey_role import EnvInt_role
from testJCW.env.onekey.onekey_organize import EnvInt_organize


organize_list = ['hb','wh','ez','hy','wc','hr','qs']


# EnvInt_organize().createAll()
# EnvInt_role().create_role()
EnvInt_admin().createAll()

for li in organize_list:
    EnvInt_user(li).createAll()








