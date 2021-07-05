from shopsn.common.basepage import BasePage

class Pages:

    def __init__(self,**locations):
        if locations is None:
            raise Exception("定位信息不存在")
        if len(locations)>1:
            raise Exception("只能有一个定位信息")
        self.key,self.value=next(iter(locations.items()))

    def __get__(self, instance, owner):
        if instance:
            self.driver=instance.driver
        else:
            return None
        return self

    def __find_element(self):
        return self.driver.find_element(self.key,self.value)

    def __find_elements(self):
        return self.driver.find_elements(self.key,self.value)

    def sendkeys(self,keys):
        self.__find_element().send_keys(keys)

    def click(self):
        self.__find_element().click()

    def swith_to_iframe(self):
        self.driver.switch_to_frame(self.__find_element)


    def get_text(self):
        self.__find_element().text()






