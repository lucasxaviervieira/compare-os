from src.web_scrapp.teams import send_message as sm

from selenium import webdriver
from selenium.webdriver.common.by import By
from src import secret as sct
import time


class ServiceOrder:
    def __init__(self):
        self.driver = webdriver.Chrome()
        # self.driver.minimize_window()

    def get_page(self, url, time_await):
        self.driver.get(url)
        self.driver.implicitly_wait(time_await)

    def script(self):
        url = "http://192.168.60.203/licenciamento"
        self.get_page(url, 0.5)
        self.login()

        time.sleep(2)

        url = "http://192.168.60.203/painel"
        self.get_page(url, 1.5)
        self.alteracoes()

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

    def alteracoes(self):
        last_info = self.driver.find_element(
            by=By.XPATH, value="/html/body/div/div[2]/div/div/div[2]/div[1]"
        )
        value = last_info.text

        send_message = sm.MessageTeams(value)
        send_message.script()

    def tear_down(self):
        if self.driver != None:
            time.sleep(5)
            self.driver.close()
            self.driver.quit()
