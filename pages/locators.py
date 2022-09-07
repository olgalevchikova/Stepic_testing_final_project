from selenium.webdriver.common.by import By

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

#class MainPageLocators():
#    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class ProductPageLocators():
    BUSKET = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    NAME = (By.TAG_NAME, "h1")
    PRICE = (By.CSS_SELECTOR, ".row .product_main .price_color")
    ALLERT_NAME = (By.CSS_SELECTOR, "#messages>.alert:nth-child(1)>.alertinner>strong")
    ALLERT_PRICE = (By.CSS_SELECTOR, "#messages>.alert:nth-child(3)>.alertinner>p>strong") 

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")