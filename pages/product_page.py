from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_product_to_busket(self):
        can_add_product_to_busket()
   
    def can_add_product_to_busket(self):
        assert self.is_element_present(*ProductPageLocators.BUSKET), "Busket button is not presented"
        self.browser.find_element(*ProductPageLocators.BUSKET).click()
    
    def know_price_and_name(self):
        self.name = self.browser.find_element(*ProductPageLocators.NAME).text        
        self.price = self.browser.find_element(*ProductPageLocators.PRICE).text
    
    def is_name_correct(self):
        assert self.name == self.browser.find_element(*ProductPageLocators.ALLERT_NAME).text, "Name of book is different"


    def is_price_correct(self): 
        assert self.price == self.browser.find_element(*ProductPageLocators.ALLERT_PRICE).text, "Price of book is different"
       
    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.ALLERT_NAME), \
        "Success message is presented, but should not be"

    def should_be_dissapear_message(self):
        assert self.is_disappeared(*ProductPageLocators.ALLERT_NAME), \
        "Success message is not disappeared, but should be"