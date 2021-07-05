import xml.etree.ElementTree as ET

from shopsn.config.readConfig import Config

path = Config().locations
tree = ET.parse(source=path)


class LoginElements:

    @property
    def loginpage_username(self):
        property=tree.find("./登录页面/用户名").get('property')
        value=tree.find("./登录页面/用户名").get('value')
        return {property:value}

    @property
    def loginpage_password(self):
        property = tree.find("./登录页面/密码").get('property')
        value = tree.find("./登录页面/密码").get('value')
        return {property:value}

    @property
    def loginpage_submit(self):
        property=tree.find("./登录页面/登录按钮").get('property')
        value=tree.find("./登录页面/登录按钮").get('value')
        return {property:value}

    @property
    def loginpage_login_success(self):
        property=tree.find("./登录页面/登录成功").get('property')
        value=tree.find("./登录页面/登录成功").get('value')
        return {property:value}

    @property
    def loginpage_login_fail(self):
        property=tree.find("./登录页面/登录失败").get('property')
        value=tree.find("./登录页面/登录失败").get('value')
        return {property:value}

login_elements=LoginElements()






if __name__ == '__main__':
    location=ReadLocation()
    print(location.loginpage_username)

