import pandas as pd
import json

class lists():
    def __init__(self):
        self.file_path = 'lists.csv'
        self.database = pd.read_csv(self.file_path)

    def search(self, content, keyword):
        result = self.database[(self.database[keyword] == content)]
        result = json.dumps(result.values.tolist())
        return result

    def get_full_list(self):
        result = json.dumps(self.database.values.tolist())
        return result