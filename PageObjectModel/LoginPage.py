from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from PageObjectModel.ShopPage import ShopPage
class LoginPage():

    def __init__(self,driver):
        self.driver=driver
        self.input_text=(By.NAME, "name")
        self.trigger_validation=(By.CSS_SELECTOR, "input[name='email']")
        self.error_message_name=(By.XPATH, "//div[contains(text(),'Name is required')]")
        self.email_text=(By.NAME, "email")
        self.email_mesage=(By.XPATH, "//div[text()='Email is required']")
        self.password=(By.ID, "exampleInputPassword1")
        self.check_button=(By.ID, "exampleCheck1")
        self.dropdown=(By.ID, "exampleFormControlSelect1")
        self.radio_button=(By.NAME, "inlineRadioOptions")
        self.submit=(By.CSS_SELECTOR, "input[type='submit']")
        self.success_message=(By.CSS_SELECTOR, "div[class='alert alert-success alert-dismissible']")
        self.shop_link=(By.LINK_TEXT, "Shop")

    def login(self,name,email):
        # =======================================LoginPage======================
        # Name Field

        name_field = self.driver.find_element(*self.input_text)
        if name.strip():  # If name is not empty after trimming whitespace
            name_field.send_keys(name)
        else:
            name_field.send_keys('')  # Send empty input
            # Trigger validation
            self.driver.find_element(*self.trigger_validation).click()
            # Fetch and print the error
            error_text = self.driver.find_element(*self.error_message_name).text
            print("Validation Error:", error_text)
        # Email Field
        email_field = self.driver.find_element(*self.email_text)

        if email.strip():
            if email.endswith("@gmail.com"):
                # If name is not empty after trimming whitespace
                email_field.send_keys(email)
                print("email is valid")
            else:
                email_field.send_keys(email)
                self.driver.find_element(*self.input_text).click()
                print("email is not valid")
        else:
            email_field.send_keys('')  # Send empty input
            # Trigger validation
            self.driver.find_element(*self.input_text).click()
            # Fetch and print the error
            error_text = self.driver.find_element(*self.email_mesage).text
            print("Validation Error:", error_text)

        self.driver.find_element(*self.password).send_keys("1234")
        self.driver.find_element(*self.check_button).click()
        select = Select(self.driver.find_element(*self.dropdown))
        select.select_by_index(1)
        radio_buttons = self.driver.find_elements(*self.radio_button)
        for raio_button in radio_buttons:
            if raio_button.get_attribute("value") == 'option2':
                raio_button.click()

        self.driver.find_element(*self.submit).click()

        message = self.driver.find_element(*self.success_message).text
        assert "Success!" in message
        print(message)
        self.driver.find_element(*self.shop_link).click()
        return ShopPage(self.driver)