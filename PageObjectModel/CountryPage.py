import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class CountryPage():

    def __init__(self,driver):
        self.driver=driver
        self.country_text=(By.ID, "country")
        self.countries_text=(By.XPATH, "//div[@class='suggestions']/ul/li")
        self.check_label=(By.XPATH, "//label[@for='checkbox2']")
        self.purchase_button=(By.XPATH, "//input[@value='Purchase']")
        self.delivered_message=(By.CSS_SELECTOR, "div[class='alert alert-success alert-dismissible']")

    def country(self,expected_name,actual_name):
        # ==============================================Countrypage==============================

        self.driver.find_element(*self.country_text).send_keys(expected_name)
        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.presence_of_element_located((self.countries_text)))
        country_list = self.driver.find_elements(*self.countries_text)
        for country in country_list:
            country_name = country.text.strip()
            if country_name.lower() == actual_name:
                time.sleep(2)
                country.click()
                break
        print(country_name)

        self.driver.find_element(*self.check_label).click()
        self.driver.find_element(*self.purchase_button).click()

        success_text = self.driver.find_element(*self.delivered_message).text
        assert "Thank you! Your order will be delivered" in success_text
        print(success_text)
