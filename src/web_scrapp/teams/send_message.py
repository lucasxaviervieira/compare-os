from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

from src import secret as sct


import time


class MessageTeams:
    def __init__(self, many_os):
        self.many_os = many_os

        self.driver = webdriver.Chrome()
        self.driver.minimize_window()

    def get_page(self, url, time_await):
        self.driver.get(url)
        self.driver.implicitly_wait(time_await)

    def script(self):
        url = "https://login.microsoftonline.com/common/oauth2/v2.0/authorize?response_type=id_token&scope=openid%20profile&client_id=5e3ce6c0-2b1f-4285-8d4b-75ee78787346&redirect_uri=https%3A%2F%2Fteams.microsoft.com%2Fgo&state=eyJpZCI6IjA1MTQ4MzZiLTAwYTUtNDUyZi05OWEwLWE3OTJiNzZlN2JiMCIsInRzIjoxNzE2OTIyNTEyLCJtZXRob2QiOiJyZWRpcmVjdEludGVyYWN0aW9uIn0%3D&nonce=7809573f-988e-4ab6-a766-6e8e62be67bd&client_info=1&x-client-SKU=MSAL.JS&x-client-Ver=1.3.4&client-request-id=5cb15e35-1c1e-4abe-ada8-ccb5e8a94e9b&response_mode=fragment&sso_reload=true"

        self.get_page(url, 2)

        time.sleep(0.5)

        self.login()

        time.sleep(20)

        self.new_chat()

        self.tear_down()

    def login(self):

        secret = sct.Secret()
        secret_user, secret_pass = secret.extract_credentials()

        username = self.driver.find_element(by=By.XPATH, value='//*[@id="i0116"]')
        username.send_keys(secret_user + "@aguasdejoinville.com.br")

        advance_button = self.driver.find_element(
            by=By.XPATH, value='//*[@id="idSIButton9"]'
        )
        advance_button.click()

        time.sleep(1)

        password = self.driver.find_element(by=By.XPATH, value='//*[@id="i0118"]')
        password.send_keys(secret_pass)

        time.sleep(0.5)

        submit_button = self.driver.find_element(
            by=By.XPATH, value='//*[@id="idSIButton9"]'
        )
        submit_button.click()

        time.sleep(1.5)

        btn_always_conn = self.driver.find_element(
            by=By.XPATH, value='//*[@id="idBtn_Back"]'
        )
        btn_always_conn.click()

        time.sleep(1.5)

        btn_select_account = self.driver.find_element(
            by=By.XPATH,
            value='//*[@id="tilesHolder"]/div[1]/div/div[1]',
        )
        btn_select_account.click()

        time.sleep(20)

        btn_migrate_v2 = self.driver.find_element(
            by=By.XPATH,
            value='//*[@id="ngdialog1"]/div[2]/div/div/div/div[2]/div/div/button',
        )
        btn_migrate_v2.click()

    def new_chat(self):

        ActionChains(self.driver).key_down(Keys.ALT).send_keys("n").key_up(
            Keys.ALT
        ).perform()

        ActionChains(self.driver).send_keys("osvaldo.silva").perform()

        time.sleep(0.5)

        ActionChains(self.driver).key_down(Keys.ENTER).key_up(Keys.ENTER).perform()
        ActionChains(self.driver).key_down(Keys.ENTER).key_up(Keys.ENTER).perform()

        time.sleep(0.5)

        ActionChains(self.driver).send_keys(
            f"Quantidade de OS: {self.many_os}"
        ).key_down(Keys.ENTER).key_up(Keys.ENTER).perform()

    def tear_down(self):
        if self.driver != None:
            time.sleep(90)
            self.driver.close()
            self.driver.quit()
