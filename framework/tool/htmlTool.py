from framework.driver.driver import DR

def screenshot(picture_file):
    '''
    browser screenshots
    :param picture_file: picture file
    :return:None
    '''
    DR.get_screenshot_as_file(picture_file)


def highlightElement(element):
    '''
    highlight the found element
    :param driver:browser driver
    :param element:element on the browser
    :return:None
    '''
    DR.execute_script("arguments[0].setAttribute('style',arguments[1]);", element,
                          "background:green; border:2px solid red")


def getInnerHTML(element):
    element.get_attribute('innerHTML')

def write(msg,file = r'D:\test2.html'):
    with open(file, 'a+') as fb:
        fb.write(msg)



