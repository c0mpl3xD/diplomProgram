import json
import requests
from API.Models.user import User
from utils.config import API_ROUTE
from http import HTTPStatus

class ApiService:

    __AUTH_ROUTE = '/api/auth'
    __user:User
    __token = ''


    def post(self, route, body):
        res = requests.post(f"{API_ROUTE}{route}", data=body, headers={'Content-Type': 'application/json', 'Authorization' : f'Bearer {self.__token}'})

        if res.status_code == HTTPStatus.UNAUTHORIZED:
            hhtpRes = self.__get_token()
            result = hhtpRes.content.decode()
            if res.ok:
                self.__token = json.loads(result)["access_token"]
                return self.post(route,body)
            else:
                raise result
        return res



    def get(self, route):
        res = requests.get(f"{API_ROUTE}{route}", headers={'Content-Type': 'application/json', 'Authorization' : f'Bearer {self.__token}'})

        if res.status_code == HTTPStatus.UNAUTHORIZED:
            hhtpRes = self.__get_token()
            result = hhtpRes.content.decode()
            if res.ok:
                self.__token = json.loads(result)["access_token"]
                return self.get(route)
            else:
                raise result
        return res
    
    
    def auth(self, user:User) -> bool:
        self.__user = user
        res = self.__get_token()
        result = res.content.decode()

        if res.ok:
            self.__token = json.loads(result)["access_token"]
            print(self.__token)

        return res.ok



    def __get_token(self):
        body = json.dumps(vars(self.__user))
        return requests.post(f"{API_ROUTE}/api/auth?tokenlifitime={60*24}", data=body, headers={'Content-Type': 'application/json'})

    
    def delete(self, route):
        res = requests.delete(f"{API_ROUTE}{route}", headers={'Content-Type': 'application/json', 'Authorization' : f'Bearer {self.__token}'})

        if res.status_code == HTTPStatus.UNAUTHORIZED:
            hhtpRes = self.__get_token()
            result = hhtpRes.content.decode()
            if res.ok:
                self.__token = json.loads(result)["access_token"]
                return self.get(route)
            else:
                raise result
        return res
