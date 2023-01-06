import json
import requests

class Position:
    def __init__(self, client):
        self.client = client 

    def get_positions(self):
        path = f"/v3/acounts/{self.client.account_id}/positions"
        response = requests.get(self.client.base_url+path, headers=self.client.header)
        return response

    def get_open_positions(self):
        path = f"/v3/acounts/{self.client.account_id}/openPositions"
        response = requests.get(self.client.base_url+path, headers=self.client.header)
        return response

    def get_position_for(self, instrument):
        path = f"/v3/acounts/{self.client.account_id}/positions/{instrument}"
        response = requests.get(self.client.base_url+path, headers=self.client.header)
        return response

    def close_position_for(self, instrument, units="ALL"):
        path = f"/v3/accounts/{self.client.account_id}/positions/{instrument}/close"
        
        if units[0]=="-":
            params = {"shortUnits": units}
        else:
            params = {"longUnits": units}

        data = json.dumps(params)
        response = requests.put(self.client.base_url+path, headers=self.client.header, data=data)
        return response
