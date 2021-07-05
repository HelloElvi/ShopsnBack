from shopsn.common.driverfactory import DriverFactory

class BasePage:


    '''初始化driver，如果传入的driver存在则使用传入的driver，如果不存在使用创建的chromedriver'''
    def __init__(self,driver=None):
        if driver:
            self.driver=driver
        else:
            self.driver=DriverFactory().driver()

    def open_url(self,url=None):
        if url is None:
            '''这边的self.url，当调用页面没有url值得时候，就必须传入一个url，否则就会报错'''
            self.driver.get(self.url)
        else:
            self.driver.get(url)

    def findelement(self,*element):
        self.driver.find_element(element)

    def findelements(self,*element):
        self.driver.find_elements(element)

    def closebroswer(self):
        self.driver.close()

    def quitbroswer(self):
        self.driver.quit()






