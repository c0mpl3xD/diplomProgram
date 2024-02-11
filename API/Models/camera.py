from API.Models.user import User
import enum;

class CameraConnection(enum):
    Ethernet = 0
    Cabel = 1
    

class Camera:
    def __init__(self, id=None, userId=None, user=User, name=None, connection=CameraConnection, connectionData=None) -> None:
        self.id = id
        self.userId = userId
        self.user=user
        self.name=name
        self.connection=connection
        self.connectionData=connectionData

    @classmethod
    def from_json(cls, json):
        return cls(json['Id'], json['userId'], json['user'], json['name'], json['connection'], json['connectionData'])