from configparser import ConfigParser

class Config:

    __path=r"E:\studies\huice06\shopsn\config\config.ini"

    def __init__(self):
        configs = ConfigParser()
        configs.read(self.__path)
        self.__chromedriver=configs.get('driverpath','chromedriver')
        # 获取火狐浏览器driver
        self.__firefoxdriver=configs.get('driverpath','firefoxdrier')
        self.__iedriver=configs.get('driverpath','iedriver')
        # 获取元素定位信息文件路径
        self.__elementslocation=configs.get('elementslocation','locationpath')
        self.__broswertype=configs.get('broswertype','type')
        self.__baseurl=configs.get('baseurl','baseurl')

    @property
    def chromedriver(self):
        return self.__chromedriver

    @property
    def firefoxdriver(self):
        return self.__firefoxdriver

    @property
    def iedriver(self):
        return self.__iedriver

    @property
    def locations(self):
        return self.__elementslocation

    @property
    def broswertype(self):
        return self.__broswertype

    @property
    def baseurl(self):
        return self.__baseurl


if __name__ == '__main__':
    config=Config()
    print(config.chromedriver)
