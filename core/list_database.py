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

    def get_listnames(self):
        result = self.database['list_name'].unique().tolist()
        return result

    def get_recipe_detail(self, recipe_name):
        result = self.database[self.database["recipe_name"] == recipe_name].loc[:,["list_name", "description", "photo_path", "total_time", "calories"]].values[0]
        return result

    def add_recipe(self, list_name, recipe_name, total_time, description, calories):
        record = {'list_name':list_name, 'recipe_name':recipe_name, 'stars':0, 'creator':'Haoyu Lu', 
                  'total_time':total_time, 'description':description, 'photo_path':None, 'calories':calories}
        self.database = self.database.append(record, ignore_index=True)
        self.database.to_csv(self.file_path, index=False)

    def delete_list(self,recipe_name):
         for i in range(len(self.database.loc[self.database.recipe_name == recipe_name,"list_name"])):
           self.database.drop(self.database.loc[self.database.recipe_name == recipe_name,"list_name"][i])
         for i in range(len(self.database.loc[self.database.recipe_name == recipe_name,"description"])):
           self.database.drop(self.database.loc[self.database.recipe_name == recipe_name,"description"][i])
         for i in range(len(self.database.loc[self.database.recipe_name == recipe_name,"photo_path"])):
           self.database.drop(self.database.loc[self.database.recipe_name == recipe_name,"photo_path"][i])
         for i in range(len(self.database.loc[self.database.recipe_name == recipe_name,"total_time"])):
           self.database.drop(self.database.loc[self.database.recipe_name == recipe_name,"total_time"][i])
         for i in range(len(self.database.loc[self.database.recipe_name == recipe_name,"calories"])):
           self.database.drop(self.database.loc[self.database.recipe_name == recipe_name,"calories"][i])
         
         