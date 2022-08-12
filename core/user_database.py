import pandas as pd
import json

class users():
    def __init__(self):
        self.file_path = 'users.csv'
        self.database = pd.read_csv(self.file_path)

    def login(self, email, password):
        if len(self.database.loc[self.database["email"] == email]["password"].values)== 0:
            return False  
        elif password == self.database.loc[self.database["email"] == email]["password"].values[0]:
            return True
        else:
            return False

    def append(self, record):
        if len(self.database.loc[self.database["email"] == record["email"]])!= 0:
                return False
        elif len(self.database.loc[self.database["robot_id"] == record["robot_id"]])!= 0:
                return False
        else: 
           self.database = self.database.append(record, ignore_index=True)
           self.database.to_csv("users.csv")

    def username(self,email):
        name = self.database.loc[self.database["email"] == email]["name"].values[0]
        return name
    
    def robot_id(self,email):
        robot_id = self.database.loc[self.database["email"] == email]["robot_id"].values[0]
        return robot_id
        
    def update(self,name,password,robot_id,email):
     self.database.loc[self.database.email==email,"name"]=name
     self.database.loc[self.database.email==email,"password"]=password
     self.database.loc[self.database.email==email,"robot_id"]=robot_id
     self.database.to_csv(self.file_path, index=False)
