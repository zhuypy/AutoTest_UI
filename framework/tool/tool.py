import time
import xlrd
import os
# ==========================wait======================
def sleep(sleepTime):
    '''
    waiting
    :param sleepTime: specify waiting time
    :return:None
    '''

    time.sleep(sleepTime*1)

# ================current time======================
def getCurrentTime():
    '''
    get current time
    :return: Y_m_d_H_M_S
    '''
    return time.strftime('%Y_%m_%d_%H_%M_%S',time.localtime())

def getCurrentDate():
    '''
    get current date
    :return: Y_m_d
    '''
    return time.strftime('%Y_%m_%d',time.localtime())


#=====================file==========================

def findFileinDir(file_name,dir):
    if not os.path.isfile(os.path.join(dir,file_name)):
        for subFile in os.listdir(dir):
            if os.path.isdir(os.path.join(dir,subFile)) and findFileinDir(file_name,os.path.join(dir,subFile)):
                return findFileinDir(file_name,os.path.join(dir,subFile))
    else:
        return os.path.join(dir,file_name)
    return None

def findAllSubFile(dir):
    fileList = []
    for subFile in os.listdir(dir):
        if os.path.isfile(os.path.join(dir, subFile)):
            fileList.append(os.path.join(dir, subFile))
        else:
            subFileList = findAllSubFile(os.path.join(dir, subFile))
            fileList += subFileList
    return fileList

def getDataFromProperties(file):
    '''
    read test data from x.propertie file
    :param file:
    :return: dict
    '''
    data = {}
    with open(file,'r',encoding='UTF-8') as fb:
        lines = fb.readlines()
        for line in lines:
            line = line.strip()
            key = line.split('=')[0]
            value = line.split('=')[1]
            if key not in  data.keys():
                data[key] =value
    return data

def getDataFromExcel(file):
    '''
    read test data from x.xlsx of x.xls
    :param file: Excel file path
    :param pageMark:sheet index or name
    :return: dict
    '''

    data = {}
    table = xlrd.open_workbook(file)
    names = table.sheet_names()
    for name in names :
        sheet = table.sheet_by_name(name)
        d = {}
        for i in range(sheet.nrows):
            k = sheet.cell_value(i,0)
            if k not in d.keys():
                v = sheet.cell_value(i,1)
                # if

                d[k] = v
        data[name] = d
    return data


def compareDict(dict1,dict2,keyword = None):
    '''

    :param dict1:
    :param dict2:
    :param keyword:the necessary element, if not in sanmeDict,fails to determine the comparison
    :return:result_code: -1,0,1 ,samedict:intersection of two dictionaries
    '''
    dictSame = {}
    ret = 0
    for key in dict1.keys():
        if key in dict2.keys():
            if dict1.get(key) == dict2.get(key):
                dictSame[key] = dict1.get(key)
                continue
            elif dict1.get(key) in dict2.get(key):
                dictSame[key] = dict2.get(key)
                ret = 1
                continue
            elif dict2.get(key) in dict1.get(key):
                dictSame[key] = dict1.get(key)
                ret = 1
                continue
            else:
                return -1,{'expect':dict1.get(key),'actual':dict2.get(key)}
        else:
            continue
    if keyword and (keyword not in dictSame.keys()):
        return -2,None
    return ret,dictSame


def convertDict(dict,rule):
    '''

    :param dict:
    :param rule:
    :return:
    '''
    ret_dict = {}
    for key in dict.keys():
        if key in rule.keys():
            ret_dict[rule.get(key)] = dict.get(key)
    return ret_dict





