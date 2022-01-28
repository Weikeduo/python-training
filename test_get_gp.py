# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class TestGetGp(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Chrome(executable_path=r'')
        self.wd.implicitly_wait(30)

    def test_get_gp(self):
        wd = self.wd
        wd.get("https://aisgp-core-stage.ntrlab.ru:7001/Membership/Login?ReturnUrl=%2FHome%2FIndex")
        wd.find_element_by_id("userName").click()
        wd.find_element_by_id("userName").clear()
        wd.find_element_by_id("userName").send_keys("admin")
        wd.find_element_by_id("userPassword").clear()
        wd.find_element_by_id("userPassword").send_keys("L0giK@17")
        wd.find_element_by_id("userPassword").send_keys(Keys.ENTER)
        wd.find_element_by_link_text(u"Ввод данных").click()
        wd.find_element_by_xpath("//div[@id='divmenu']/div").click()
        wd.find_element_by_id("GpTypes").click()
        wd.find_element_by_xpath("//a[@id='GpTypesSelector_0']/span").click()
        wd.find_element_by_id("Gps").click()
        wd.find_element_by_xpath("//a[@id='GpsSelector_4']/span").click()
        wd.find_element_by_xpath("//a[@id='GpVersionsSelector_3']/span").click()
        wd.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='Удалить'])[1]/following::span[2]").click()
    
    def is_element_present(self, how, what):
        try: self.wd.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.wd.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True

    def tearDown(self):
        self.wd.quit()

if __name__ == "__main__":
    unittest.main()
