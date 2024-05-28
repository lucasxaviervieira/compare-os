class Secret:
    def __init__(self):
        self.file = "secret.txt"
        self.file_text = ""

    def read_secret(self):
        try:
            with open(self.file, "r") as file:
                self.file_text = file.readlines()
        except FileNotFoundError:
            print(f"Arquivo '{self.file}' não encontrado.")
            return None

    def extract_credentials(self):
        self.read_secret()
        username = self.file_text[0].strip()
        password = self.file_text[1].strip()
        return username, password
