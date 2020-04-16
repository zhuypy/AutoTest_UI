from framework.driver.driver import DR
from framework.logger.logger import logger
from framework.tool.tool import *
class HtmlElement():
    '''
    common methds for obtaining elements
    '''

    # def __new__(cls,selector):
    #     obj = cls.find_element(selector)
    #     for func in dir(cls):
    #         if not str(func).startswith('_'):
    #             setattr(obj,func,types.MethodType(getattr(cls,func),func))
    #     return obj

    def __init__(self,element=None,selector1=None,selector2=None):
        if element :
            self.element = element
        else:
            # self.element = self.getElement(selector1, selector2)
            for i in range(10):
                try:
                    self.element = self.getElement(selector1, selector2)
                    break
                except Exception as e:
                    if i == 9:
                        logger.error('finding element by selector1=%s ,selector2=%s failed' % (selector1, selector2))
                        raise e
                    else:
                        logger.info('finding element by selector1=%s ,selector2=%s'%(selector1,selector2))
                        sleep(0.5)
           

    def getElements(self,selector):
        '''
        get the list of elements
        :param selector:[by,value]
        :return:elemnents
        '''
        return self.__find_elements(selector)

    def getElement(self,selector1,selector2=None):
        '''
        get the unique element
        :param selector1:[by1,value1]
        :param selector2:[by2,value2]
        :return:element
        '''
        if not selector2:
            return self.__find_element(selector1)
        else:
            elements = self.__find_elements(selector1)
            for element in elements:
                if element.get_attribute(selector2[0]) == selector2[1]:
                    return element
            return None

    def __find_element(self,selector):
        '''
        private method
        :param selector:key-value list
        :return:element
        '''
        key = selector[0]
        value = selector[1]
        element = None

        if key in ['xpath','link_text','class_name','id','css_selector','name','partial_link_text','tag_name']:
            if key == 'xpath':
                element  = DR.find_element_by_xpath(value)
            elif key == 'link_text':
                element  = DR.find_element_by_link_text(value)
            elif key == 'class_name':
                element  = DR.find_element_by_class_name(value)
            elif key == 'id':
                element  = DR.find_element_by_id(value)
            elif key == 'css_selector':
                element  = DR.find_element_by_css_selector(value)
            elif key == 'name':
                element  = DR.find_element_by_name(value)
            elif key == 'partial_link_text':
                element  = DR.find_element_by_partial_link_text(value)
            elif key == 'tag_name':
                element  = DR.find_element_by_tag_name(value)

            if element :
                return element
            else:
                logger.error('fialed to find element on the current page')
                return None
        else:
            logger.error('invalid key')
            return None



    def __find_elements(self,selector):
        '''
        private method:
        :param selector:key-value list
        :return:element
        '''

        key = selector[0]
        value = selector[1]
        elements = None


        if key in ['xpath', 'link_text', 'class_name', 'id', 'css_selector', 'name', 'partial_link_text',
                   'tag_name']:
            if key == 'xpath':
                elements = DR.find_elements_by_xpath(value)
            elif key == 'link_text':
                elements = DR.find_elements_by_link_text(value)
            elif key == 'class_name':
                elements = DR.find_elements_by_class_name(value)
            elif key == 'id':
                elements = DR.find_elements_by_id(value)
            elif key == 'css_selector':
                elements = DR.find_elements_by_css_selector(value)
            elif key == 'name':
                elements = DR.find_elements_by_name(value)
            elif key == 'partial_link_text':
                elements = DR.find_elements_by_partial_link_text(value)
            elif key == 'tag_name':
                elements = DR.find_elements_by_tag_name(value)

            if elements:
                return elements
            else:
                logger.error('fialed to find elements on the current page')
                return None
        else:
            logger.error('invalid key')
            return None

