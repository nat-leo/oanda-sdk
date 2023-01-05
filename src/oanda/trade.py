import requests
import json

class Trade:
    def __init__(self, client) -> None:
        self.client = client

    def get_trades(self, instrument, ids=None, state="OPEN", count="50", before_id=None):
        path = f"/v3/accounts/{self.client.account_id}/trades"
        params = (
            ("ids", ids),
            ("instrument", instrument),
            ("state", state),
            ("count", count),
            ("beforeID", before_id)
        )
        response = requests.get(self.client.base_url+path, headers=self.client.header, params=params)
        return response
    
    # get all open trades from the client.
    def get_open_trades(self):
        path = f"/v3/accounts/{self.client.account_id}/openTrades"
        response = requests.get(self.client.base_url+path, headers=self.client.header)
        return response

    def get_trade_by_id(self, trade_id):
        path = f"/v3/accounts/{self.client.account_id}/trades/{trade_id}"
        params = (
            ("tradeSpecifier", trade_id),
        )
        response = requests.get(self.client.base_url+path, headers=self.client.header, params=params)
        return response
    
    def close_trade_by_id(self, trade_id, units="ALL"):
        path = f"/v3/accounts/{self.client.account_id}/trades/{trade_id}/close"
        params = {
            "order": {
                "units": units,
            }
        }
        data = json.dumps(params)
        response = requests.put(self.client.base_url+path, headers=self.client.header, data=data)
        return response
    
    def set_client_extensions(self, trade_id, client_extensions):
        path = f"/v3/accounts/{self.client.account_id}/trades/{trade_id}/clientExtensions"
        params = {
            "clientExntensions": client_extensions
        }
        data = json.dumps(params)
        response = requests.put(self.client.base_url+path, headers=self.client.header, data=data)
        return response
