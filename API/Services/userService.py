import json
import requests
from API.Models.user import User
from API.Services.apiService import ApiService
from utils.config import API_ROUTE


class UserService:
    apiService = ApiService()

    def getUser(self,id) -> User:
        result = self.apiService.get(f'/api/user/user?id={id}')
        if result.ok:
            json = result.json()
            user = User.from_json(json)
            return user
        
        return None

    def getUsers(self) -> list[User]:
        result = self.apiService.get(f'/api/user/user')
        if result.ok:
            json = result.json()
            user_list = [User.from_json(item) for item in json]
            return user_list
            
        return None
    

    def register(self, model):
        body = json.dumps(vars(model))
        response = requests.post(f"{API_ROUTE}/api/user/user", data=body, headers={'Content-Type': 'application/json'})
        #print(response)

        return response
    
    def login(self, model):
        return self.apiService.auth(model)