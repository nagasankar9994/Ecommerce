from selenium.webdriver.common.by import By

from PageObjectModel.CountryPage import CountryPage


class ShopPage():

    def __init__(self,driver):
        self.driver=driver
        self.shop_items=(By.XPATH, "//div[@class='card h-100']")
        self.item_text=(By.XPATH, "div/h4")
        self.add_cart=(By.XPATH,"div/button")
        self.shop_checkout=(By.XPATH, "//a[@class='nav-link btn btn-primary']")
        self.item_checkout=(By.CSS_SELECTOR, "button[class='btn btn-success']")




    def shop_item(self,mobile_item):

        # =================================================SHOPPage=============
        mobiles = self.driver.find_elements(*self.shop_items)

        for mobile in mobiles:
            mobile_text = mobile.find_element(*self.item_text).text
            if mobile_text == mobile_item:
                mobile.find_element(*self.add_cart).click()
                break
        shop_checkout = self.driver.find_element(*self.shop_checkout).text
        checkout_text = int(
            shop_checkout.replace("Checkout (", "").strip().replace(")", "").strip().replace("(current", "").strip())

        if checkout_text <= 0:
            print("Mobile is not add the cart")
        else:
            self.driver.find_element(*self.shop_checkout).click()
            print("Mobile is add the cart successfully")

        self.driver.find_element(*self.item_checkout).click()
        return CountryPage(self.driver)
