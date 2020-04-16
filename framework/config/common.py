import os
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

def getSubDict(dict,list):
    subDict = {}
    for li in list:
        subDict[li] = dict[li]
    return subDict

TestRunProperties = os.path.join(os.path.dirname(os.path.abspath(__file__)),'testRun.properties')
TestEnvProperties = os.path.join(os.path.dirname(os.path.abspath(__file__)),'testEnv.properties')
TestDebugProperties = os.path.join(os.path.dirname(os.path.abspath(__file__)),'testDebug.properties')

# propertiesDict = getDataFromProperties(TestEnvProperties)
propertiesDict = getDataFromProperties(TestRunProperties)

ALL_PATH = getSubDict(propertiesDict,['case_path','data_path','log_path','report_path'])
ALL_PARAM = getSubDict(propertiesDict,['browser_type','current_version','login_address','home_address','user','pwd'])
