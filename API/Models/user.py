class User:
    def __init__(self, id=None, email=None, login=None, password=None, phone=None):
        self.id = id
        self.email = email
        self.login = login
        self.password = password
        self.phone = phone


    @classmethod
    def from_json(cls, json):
        return cls(json['Id'], json['Email'], json['Login'], json['Password'], json['Phone'])