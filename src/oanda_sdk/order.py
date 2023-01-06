import requests
import json

class Order:
    def __init__(self, client) -> None:
        self.client
    
    # PUT an order for the client
    def create_order(self, units, instrument, time_in_force="FOK", fill_type="MARKET", position_fill="DEFAULT"):
        path = f"/v3/accounts/{self.client.account_id}/orders"
        params = {
            "order": {
                "units": units,
                "instrument": instrument,
                "timeInForce": time_in_force,
                "type": fill_type,
                "positionFill": position_fill,
            }
        }
        data = json.dumps(params)
        response = requests.post(self.client.base_url+path, headers=self.client.header, data=data)
        return response
    
    def get_orders(self, instrument):
        path = f"/v3/accounts/{self.client.account_id}/orders"
        params = {
           ("instrument", instrument)
        }
        response = requests.get(self.client.base_url+path, headers=self.client.header, params=params)
        return response

    # gets all pending orders for the client.
    def get_pending_orders(self):
        path = f"/v3/accounts/{self.client.account_id}/pendingOrders"
        response = requests.get(self.client.base_url+path, headers=self.client.header)
        return response

    def get_order_by_id(self, transaction_id):
        path = f"/v3/accounts/{self.client.account_id}/orders/{transaction_id}"
        response = requests.get(self.client.base_url+path, headers=self.client.header)
        return response
    
    # replace the order specified by transaction_id with a new order.
    def replace_order(self, transaction_id, units, instrument, time_in_force="FOK", fill_type="MARKET", position_fill="DEFAULT"):
        path = f"/v3/accounts/{self.client.account_id}/orders/{transaction_id}"
        params = {
            "order": {
                "units": units,
                "instrument": instrument,
                "timeInForce": time_in_force,
                "type": fill_type,
                "positionFill": position_fill,
            }
        }
        data = json.dumps(params)
        response = requests.put(self.client.base_url+path, headers=self.client.header, data=data)
        return response

    def cancel_order(self, transaction_id):
        path = f"/v3/accounts/{self.client.account_id}/orders/{transaction_id}/cancel"
        response = requests.put(self.client.base_url+path, headers=self.client.header)
        return response

    def set_client_extensions(self, transaction_id, client_extensions: dict):
        path = f"/v3/accounts/{self.client.account_id}/orders/{transaction_id}/clientExtensions"
        params = {
            "clientExtensions": client_extensions
        }
        data = json.dumps(params)
        response = requests.put(self.client.base_url+path, headers=self.client.header, data=data)
        return response
