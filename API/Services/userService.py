import json
import requests
from API.Models.user import User


class UserService:
    def register(self, model):
        body = json.dumps(vars(model))
        response = requests.post("http://26.90.89.142:5047/user", data=body, headers={'Content-Type': 'application/json'})
        print(response)
        return response
    
    def login(self, model):
        body = json.dumps(vars(model))
        response = requests.post("http://26.90.89.142:5047/api/auth?tokenlifitime=60*24", data=body, headers={'Content-Type': 'application/json'})
        if response.ok:
            res = response.content.decode()
            print(res)
            token = json.loads(res)["access_token"]
            print("token: " +  token)
            return token, True
        else:
            return response.content.decode(), False