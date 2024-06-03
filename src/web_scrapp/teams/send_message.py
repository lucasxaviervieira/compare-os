from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

from src import secret as sct

import time


class MessageTeams:
    def __init__(self, teams_recipient, many_os):
        self.teams_recipient = teams_recipient
        self.many_os = many_os

        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def get_password(self):
        secret_manager = sct.Secret()
        self.username, self.password = secret_manager.teams_manager()

    def script(self):
        self.get_password()
        self.prologue()
        self.end()

    def prologue(self):
        url = "https://login.microsoftonline.com/common/oauth2/v2.0/authorize?response_type=id_token&scope=openid%20profile&client_id=5e3ce6c0-2b1f-4285-8d4b-75ee78787346&redirect_uri=https%3A%2F%2Fteams.microsoft.com%2Fgo&state=eyJpZCI6IjA1MTQ4MzZiLTAwYTUtNDUyZi05OWEwLWE3OTJiNzZlN2JiMCIsInRzIjoxNzE2OTIyNTEyLCJtZXRob2QiOiJyZWRpcmVjdEludGVyYWN0aW9uIn0%3D&nonce=7809573f-988e-4ab6-a766-6e8e62be67bd&client_info=1&x-client-SKU=MSAL.JS&x-client-Ver=1.3.4&client-request-id=5cb15e35-1c1e-4abe-ada8-ccb5e8a94e9b&response_mode=fragment&sso_reload=true"
        self.driver.get(url)

        time.sleep(2)

        self.login()

        time.sleep(2)

        self.add_config_login()

    def end(self):
        # Tempo de espera para o carregamento do Teams
        time.sleep(25)

        self.new_chat()

        time.sleep(2)

        self.write_message()

        self.tear_down()

    def login(self):
        email = self.username + "@aguasdejoinville.com.br"
        # Seleciona o elemento do formulário que se refere ao 'username'
        username = self.driver.find_element(by=By.XPATH, value='//*[@id="i0116"]')
        username.send_keys(email)

        # Selecione o botão para avançar no processo de 'Login'
        advance_button = '//*[@id="idSIButton9"]'
        self.click_button(advance_button)

        time.sleep(2)
        # Seleciona o elemento do formulário que se refere ao 'password'
        password = self.driver.find_element(by=By.XPATH, value='//*[@id="i0118"]')
        password.send_keys(self.password)

        time.sleep(2)
        # Seleciona o botão para avançar no processo de 'Login'
        submit_button = '//*[@id="idSIButton9"]'
        self.click_button(submit_button)

    def add_config_login(self):
        # Seleciona o botão para nunca salvar o usuário no navegador
        btn_always_conn = '//*[@id="idBtn_Back"]'
        self.click_button(btn_always_conn)

        time.sleep(2)
        btn_select_account = '//*[@id="tilesHolder"]/div[1]/div/div[1]'
        self.click_button(btn_select_account)

        # Teams v1 --> Teams v2
        # Esse trecho de código, serve para para ir para a nova versão do Teams
        time.sleep(28)
        btn_migrate_v2 = '//*[@id="ngdialog1"]/div[2]/div/div/div/div[2]/div/div/button'
        self.click_button(btn_migrate_v2)

    def new_chat(self):
        # Inicia uma nova conversa
        ActionChains(self.driver).key_down(Keys.ALT).send_keys("n").key_up(
            Keys.ALT
        ).perform()

        time.sleep(2)

        user_to_send = self.teams_recipient
        # Nome do usuário, ao qual será enviado a mensagem
        ActionChains(self.driver).send_keys(user_to_send).perform()
        # Tempo de espera destinado ao código anterior ser finalizado
        time.sleep(2)

        # Escolhe o primeiro usuário com o nome digitado
        self.press_enter()

        time.sleep(2)

        # Entra no campo de envio de mensagem com a tecla 'Enter'
        self.press_enter()

    def write_message(self):
        # Tempo de espera destinado ao código anterior ser finalizado
        time.sleep(1)

        message = f"Quantidade de Licenças: {self.many_os}"
        # Digita a mensagem
        ActionChains(self.driver).send_keys(message).perform()

        time.sleep(5)
        self.press_enter()
        time.sleep(2)

    def press_enter(self):
        ActionChains(self.driver).key_down(Keys.ENTER).key_up(Keys.ENTER).perform()

    def click_button(self, XPATH_el):
        btn = self.driver.find_element(by=By.XPATH, value=XPATH_el)
        btn.click()

    def tear_down(self):
        if self.driver != None:
            # Tempo de espera destinado ao código anterior ser finalizado
            time.sleep(2)
            self.driver.close()
            self.driver.quit()
