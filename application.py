from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class Application:

    def __init__(self):
        self.wd = webdriver.Chrome()
        self.wd.implicitly_wait(30)
        self.wd.fullscreen_window()

    def select_root_structural_element(self):
        wd = self.wd
        # select root structural element
        wd.find_element_by_xpath(
            u"(.//*[normalize-space(text()) and normalize-space(.)='Удалить'])[1]/following::span[2]").click()

    def select_version_gp(self):
        wd = self.wd
        # select gp type
        wd.find_element_by_xpath("//div[@id='divmenu']/div").click()
        wd.find_element_by_id("GpTypes").click()
        wd.find_element_by_xpath("//a[@id='GpTypesSelector_0']/span").click()
        # select gp
        wd.find_element_by_id("Gps").click()
        wd.find_element_by_xpath("//a[@id='GpsSelector_4']/span").click()
        # select version gp
        wd.find_element_by_id("GpVersions").click()
        wd.find_element_by_xpath("//a[@id='GpVersionsSelector_3']/span").click()

    def open_gov_programs_page(self):
        wd = self.wd
        wd.find_element_by_link_text(u"Ввод данных").click()

    def login(self, username, password):
        wd = self.wd
        wd.get("https://aisgp-core-stage.ntrlab.ru:7001/Membership/Login?ReturnUrl=%2FHome%2FIndex")
        wd.find_element_by_id("userName").click()
        wd.find_element_by_id("userName").clear()
        wd.find_element_by_id("userName").send_keys(username)
        wd.find_element_by_id("userPassword").clear()
        wd.find_element_by_id("userPassword").send_keys(password)
        wd.find_element_by_id("userPassword").send_keys(Keys.ENTER)

    def destroy(self):
        self.wd.quit()