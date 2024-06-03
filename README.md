# Compare-OS

Sistema para comparar as O.S. de diferentes sistemas, e enviar mensagens de alerta pelo Teams e Email, utilizando Selenium.

## Instalação e Configuração

1 - Certifique-se de ter o [Python](https://www.python.org/) instalado em seu sistema.

2 - Além, é necessário ter o [PDM](https://pdm-project.org/en/latest/) instalado em seu sistema.

3 - Abra o projeto no vscode e execute o terminal.

4 - Crie um ambiente virtual usando o [PDM](https://pdm-project.org/en/latest/):

```
pdm install
```

5 - Execute o o arquivo `main.py`:

```
pdm run main.py
```

## Configuração de Senha

Crie um arquivo 'secret.json', na raíz ` .` do diretório onde o projeto está, com o seguinte formato:

```
[
  {
    "secret": {
      "teams": [
        {
          "username": "user.name"
        },
        {
          "password": "password"
        }
      ]
    }
  },
  {
    "secret": {
      "email": [
        {
          "username": "email@domain.com"
        },
        {
          "password": "password"
        }
      ]
    }
  }
]
```

## Tecnologias Usadas

- [PDM](https://pdm-project.org/en/latest/) Gerenciador de pacotes e ambiente virtual para Python.
- [Selenium](https://www.selenium.dev/) Pacotes de automatização de testes para navegadores.
