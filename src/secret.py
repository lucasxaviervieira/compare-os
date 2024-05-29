import json


class Secret:
    def __init__(self):
        self.file_path = "secret.json"
        self.data = None
        self.read_json()

    def read_json(self):
        try:
            with open(self.file_path, "r") as file:
                self.data = json.load(file)
        except FileNotFoundError:
            print(f"File '{self.file_path}' not found.")
        except json.JSONDecodeError:
            print(f"Error decoding JSON in file '{self.file_path}'.")

    def secret_manager(self, item):
        for secret in self.data:
            for i in secret["secret"]:
                if i == item:
                    secret_dict = secret["secret"]
                    break
        username = secret_dict[item][0]["username"]
        password = secret_dict[item][1]["password"]
        return username, password

    def teams_manager(self):
        return self.secret_manager("teams")

    def email_manager(self):
        return self.secret_manager("email")
