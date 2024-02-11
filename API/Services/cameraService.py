import json

import requests
from API.Models.camera import Camera
from API.Services.apiService import ApiService
from utils.config import API_ROUTE

class CameraService:
    


    def get(self, id = int) -> Camera:
        result = self.apiService.get(f'/api/camera/camera?id={id}')
        if result.ok:
            json = result.json()
            camera = Camera.from_json(json)
            return camera
        
        return None

    def getAll(self) -> list[Camera]:
        result = self.apiService.get(f'/api/camera/camera')
        if result.ok:
            json = result.json()
            camera_list = [Camera.from_json(item) for item in json]
            return camera_list
        return None
    

    def save(self, camera = Camera) -> None:
        body = json.dumps(vars(camera))
        response = requests.post(f"{API_ROUTE}/api/camera/camera", data=body, headers={'Content-Type': 'application/json', 'Authorization' : f'Bearer {self.__token}'})
        print(response)

        return response
        
    def delete(self, id = int):
        response = requests.delete(f"{API_ROUTE}/api/camera/camera?id={id}", headers={'Content-Type': 'application/json', 'Authorization' : f'Bearer {self.__token}'})

        