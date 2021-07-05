import pytest
from shopsn.common.driverfactory import DriverFactory
from shopsn.pages.commonactions.loginpage import LoginPage


'''conftest是tests文件下的配置文件的存在，且命名只能是conftest，
driver是下面的driverfactory生成的默认driver，
login的driver使用的是默认的driver'''

@pytest.fixture(scope='function')
def login(driver):
    login=LoginPage(driver)
    login.login('admin','admin1234')

@pytest.fixture(scope='class')
def driver():
    # open driver
    driver=DriverFactory().driver()
    # 暂停
    yield driver
    # 退出driver
    driver.close()