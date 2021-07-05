from shopsn.locations.readlocation import login_elements
from shopsn.common.basepage import BasePage
from shopsn.common.pages import Pages
from shopsn.config.readConfig import Config



class LoginPage(BasePage):

    __baseurl=Config().baseurl
    __username=Pages(**login_elements.loginpage_username)
    __password=Pages(**login_elements.loginpage_password)
    __submit=Pages(**login_elements.loginpage_submit)
    __loginprompt=Pages(**login_elements.loginpage_login_success)
    __loginfail=Pages(**login_elements.loginpage_login_fail)
    __url="/adminprov.php/Public/login"
    # ----------------------------------
    # 根据方法二进行设置
    # __username=__elements.loginpage_username
    # __password=__elements.loginpage_password
    # __submit=__elements.loginpage_submit

    def openloginurl(self):
        self.open_url(self.__baseurl+self.__url)

    def input_username(self,username):
        self.__username.sendkeys(username)

    def input_password(self,password):
        self.__password.sendkeys(password)

    def sub(self):
        self.__submit.click()

    @property
    def assertsuccess(self):
        return self.__loginsuccess.get_text()
    #
    @property
    def assertfail(self):
        return self.__loginfail.get_text()

    def login(self,username,password):
        self.openloginurl()
        self.__username.sendkeys(username)
        self.__password.sendkeys(password)
        self.__submit.click()
        self.closebroswer()
        # self.
        # driver.implicitly_wait(10)
        # ---------------------------------------------------------------
        # 最原始的查找元素并输入值
        # driver.find_element_by_id("account").send_keys("admin")
        # driver.find_element_by_id("password").send_keys("admin1234")
        # driver.find_element_by_name("submit").click()
        # ---------------------------------------------------------------
        # 设置By的值，根据By值查询并输入
        # driver.find_element(self.__username[0],self.__username[1]).send_keys("admin")
        # driver.find_element(self.__password[0],self.__password[1]).send_keys("admin1234")
        # driver.find_element(self.__submit[0],self.__submit[1]).click()
        # driver.close()

if __name__ == '__main__':
    login=LoginPage()
    login.login('admin',"admin1234")