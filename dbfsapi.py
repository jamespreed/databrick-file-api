import requests

class DatabricksFileAPI:
    def __init__(self, host, token, api_route='/api/2.0/dbfs/'):
        self.host = host
        self.api_route = api_route
        self.api_url = host + api_route
        self.session = requests.Session()
        self.set_token(token)

    def set_token(self, token):
        self.token = token
        self.session.headers.update(
            {
                'Authorization': 'Bearer' + token
            }
        )
        
    def api_action(self, action, method, params: dict, body=None):
        res = self.session.request(
            method=method,
            url=self.api_url + action,
            params=params,
            json=body)
        return res.json()
    
    def Add_Block(self, handle: int, data: bytes):
        action = 'add-block'
        params = {'handle': handle, 'data': data}
        return self.api_action(action, 'POST', params)
        
    def Close(self, handle: int):
        action = 'close'
        params = {'handle': handle}
        return self.api_action(action, 'POST', params)
        
    def Create(self, path: str, overwrite: bool):
        action = 'create'
        params = {'path': path, 'overwrite': overwrite}
        return self.api_action(action, 'POST', params)
        
    def Delete(self, path: str, recursive: bool):
        action = 'delete'
        params = {'path': path, 'recursive': recursive}
        return self.api_action(action, 'POST', params)
        
    def Get_Status(self, path: str):
        action = 'get-status'
        params = {'path': path}
        return self.api_action(action, 'GET', params)
        
    def List(self, path: str):
        action = 'list'
        params = {'path': path}
        return self.api_action(action, 'GET', params)
        
    def Mkdirs(self, path: str):
        action = 'mkdirs'
        params = {'path': path}
        return self.api_action(action, 'POST', params)
        
    def Move(self, source_path: str, destination_path: str):
        action = 'move'
        params = {'source_path': source_path, 'destination_path': destination_path}
        return self.api_action(action, 'POST', params)
        
    def Put(self, path: str, contents: bytes, overwrite: bool):
        action = 'put'
        params = {'path': path, 'contents': contents, 'overwrite': overwrite}
        return self.api_action(action, 'POST', params)
        
    def Read(self, path: str, offset: int, length: int):
        action = 'read'
        params = {'path': path, 'offset': offset, 'length': length}
        return self.api_action(action, 'GET', params)

