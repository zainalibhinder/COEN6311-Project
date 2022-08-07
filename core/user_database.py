import pandas as pd
import json

class users():
    def __init__(self):
        self.file_path = 'users.csv'
        self.database = pd.read_csv(self.file_path)

    def login(self, email, password):
        if password == self.database.loc[self.database["email"] == email]["password"].values[0]:
            return True
        else:
            return False

    def append(self, record):
        self.database = self.database.append(record, ignore_index=True)
        self.database.to_csv("users.csv")
