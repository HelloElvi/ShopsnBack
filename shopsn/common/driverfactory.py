from shopsn.config.readConfig import Config
from selenium import webdriver



class DriverFactory:

    __config=Config()
    __type=__config.broswertype
    __firefox=__config.firefoxdriver
    __chrome=__config.chromedriver
    __ie=__config.iedriver

    def driver(self):
        if self.__type:
            if self.__type.lower()=="chrome":
                driver=webdriver.Chrome(executable_path=self.__chrome)
            elif self.__type.lower()=="firefox":
                driver=webdriver.Firefox(executable_path=self.__firefox)
            elif self.__type.lower()=='ie':
                driver=webdriver.Ie(executable_path=self.__ie)
            else:
                raise Exception("输入的类型暂不支持，请输入chrome或firefox或ie")
        return driver


