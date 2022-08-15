from handlers.base_handler import BaseHandler
import json


class HelloWorld(BaseHandler): 
    
    def initialize(self, data):
        self.data = data
    
    def get(self, id):
        print()
        print(f"Data: {self.data}")
        print()
        
        if id not in self.data:
            self.set_status(404)
            self.write(f"{id} not found in data: {self.data}")
            return
        
        user_data = self.data[id]
        user_data_json = json.dumps(user_data)
        
        self.write(user_data_json)
        
    def post(self):
        request_data = json.loads(self.request.body)
        
        username = request_data['username']
        user_data = request_data['user_data']
        
        print()
        print(f"Data before: {self.data}")
        self.data[username] = user_data
        print(f"Data after: {self.data}")
        print()
