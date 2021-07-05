from shopsn.pages.commonactions.loginpage import LoginPage
import  pytest


class TestLogin:
    loginpage=LoginPage()

    @pytest.mark.loginsuccess
    def test_login001(self):
        self.loginpage.login("admin","admin1234")
        assert self.loginpage.assertsuccess=="欢迎回来"


    '''只要有错：空输入，用户名或密码不写，提示都是用户名或密码错误'''
    datas=[{"","","用户名或密码错误"},
           {"admin","","用户名或密码错误"},
           {"","admin1234","用户名或密码错误"},
           {"admin","admin","用户名或密码错误"}]
    @pytest.mark.loginfail
    @pytest.mark.parametrize('username,password,expect',datas)
    def test_login002(self,username,password,expect):
        self.loginpage.login(username,password)
        assert self.loginpage.assertfail==expect

