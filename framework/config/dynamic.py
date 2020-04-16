import os
from framework.config.common import *


BROWSER_TYPE = ALL_PARAM.get('browser_type')
CURRENT_VERSION = ALL_PARAM.get('current_version')
LOGIN_ADDRESS = ALL_PARAM.get('login_address')
USER = ALL_PARAM.get('user')
PWD = ALL_PARAM.get('pwd')

CASE_PATH = ALL_PATH.get('case_path')
DATA_PATH = ALL_PATH.get('data_path')
LOG_PATH = ALL_PATH.get('log_path')
REPORT_PATH = os.path.join(ALL_PATH.get('report_path'),CURRENT_VERSION)
if not os.path.exists(CASE_PATH):
    os.makedirs(CASE_PATH)
if not os.path.exists(LOG_PATH):
    os.makedirs(LOG_PATH)
if not os.path.exists(REPORT_PATH):
    os.makedirs(REPORT_PATH)