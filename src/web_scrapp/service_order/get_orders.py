from selenium import webdriver
from selenium.webdriver.common.by import By
from src import secret as sct
import time


class ServiceOrder:
    def __init__(self):
        self.orders = 0
        self.driver = webdriver.Chrome()
        # self.driver.minimize_window()

    def main(self):
        self.script()
        return self.orders

    def script(self):
        url = "http://192.168.60.203/"
        self.driver.get(url)
        self.login()

        time.sleep(1)

        url = "http://192.168.60.203/licenciamento"
        self.driver.get(url)
        time.sleep(3)
        self.many_orders()

        self.tear_down()

    def login(self):
        username = self.driver.find_element(by=By.NAME, value="username")
        password = self.driver.find_element(by=By.NAME, value="password")
        submit_button = self.driver.find_element(by=By.TAG_NAME, value="button")

        secret = sct.Secret()
        secret_user, secret_pass = secret.extract_credentials()

        username.send_keys(secret_user)
        password.send_keys(secret_pass)

        submit_button.click()

    def many_orders(self):
        info = self.driver.find_element(by=By.XPATH, value='//*[@id="loading-total"]')
        value = info.text
        self.orders = value

    def tear_down(self):
        if self.driver != None:
            time.sleep(5)
            self.driver.close()
            self.driver.quit()
