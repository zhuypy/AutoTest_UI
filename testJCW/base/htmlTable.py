# -*- coding:utf-8 -*-
'''
@File   : htmlTable.py
@Author : 
@Date   : 2019/5/22 14:25
@Desc   :
'''

from framework.superClass.htmlElement import HtmlElement
from framework.tool.tool import *
class HtmlTable(HtmlElement):
    def getTableHead(self):
        pass

    def getTableBody(self):
        pass
    
    def getTableData(self):
        data = []
        lis = []
        trs = self.element.find_elements_by_tag_name('tr')
        for tr in trs:
            t_list = []
            if 'row' not in tr.get_attribute('class'):
                ths = tr.find_elements_by_tag_name('th')
                for i in range(1,len(ths)-1):
                    t_list.append(ths[i].text)
            else:
                tds = tr.find_elements_by_tag_name('td')
                for i in range(1,len(tds)):
                    if tds[i].find_element_by_tag_name('div').text:
                        t_list.append(tds[i].find_element_by_tag_name('div').text)
                    else:
                        t_list.append(None)
            lis.append(t_list)

        for i in range(1,len(lis)):
            dict = {}
            for j in range(len(lis[i])):
                dict[lis[0][j]] = lis[i][j]
            data.append(dict)
        return data

    def selectRow(self):
        pass

    def clickCell(self):
        pass

    def getCellValue(self):
        pass

    def getTableRow(self,selector):
        data = {}






        return data














