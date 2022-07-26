import pandas as pd
import json

class steps():
    def __init__(self):
        self.file_path = 'steps.csv'
        self.database = pd.read_csv(self.file_path)

    def get_recipe_detail(self, recipe_name):
        recipe = self.database[self.database["recipe_name"] == recipe_name].loc[:,["step", "ingredient", "quantity", "unit", "description"]]
        recipe = recipe.sort_values(by='step').values.tolist()
        result = []
        for step in recipe:
            row = []
            row.append(step[0])
            row.append(zip(step[1].split(','), step[2].split(','), step[3].split(',')))
            row.append(step[4])
            result.append(row)
        return result

step = steps()
print(step.get_recipe_detail("Curry"))