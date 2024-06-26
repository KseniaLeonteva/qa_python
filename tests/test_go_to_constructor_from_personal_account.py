from data import Data, Url
from locators import Locators
from conftest import driver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestConstructorCross:
    #Переход по клику на "Конструктор"
    def test_go_to_constructor_from_account_by_click_on_constructor(self, driver):
        driver.get(Url.main_page)
        driver.find_element(*Locators.account_button).click()
        driver.find_element(*Locators.input_email).send_keys(Data.email)
        driver.find_element(*Locators.input_password).send_keys(Data.password)
        driver.find_element(*Locators.login_button_login_page).click()
        driver.find_element(*Locators.account_button).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(Locators.header_profile))
        driver.find_element(*Locators.constructor_button).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.pack_burger))
        assert driver.find_element(*Locators.pack_burger).is_displayed()


    #Переход по клику на лого "Stellar Burgers"
    def test_go_to_constructor_from_account_by_click_on_logo(self, driver):
        driver.get(Url.main_page)
        driver.find_element(*Locators.account_button).click()
        driver.find_element(*Locators.input_email).send_keys(Data.email)
        driver.find_element(*Locators.input_password).send_keys(Data.password)
        driver.find_element(*Locators.login_button_login_page).click()
        driver.find_element(*Locators.account_button).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(Locators.header_profile))
        driver.find_element(*Locators.logo).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.pack_burger))
        assert driver.find_element(*Locators.pack_burger).is_displayed()

