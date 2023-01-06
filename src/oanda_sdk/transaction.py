import json
import requests

class Transaction:
    def __init__(self, client):
        self.client = client

    def get_transaction(self, transaction_id):
        path = f"/v3/accounts/{self.client.account_id}/transactions/{transaction_id}"
        response = requests.get(self.client.base_url+path, headers=self.client.header)
        return response

    def get_transactions(self, from_id, to_id):
        path = f"/v3/accounts/{self.client.account_id}/transactions/idrange"
        params = {
           ("from", from_id),
           ("to", to_id)
        }
        response = requests.get(self.client.base_url+path, headers=self.client.header, params=params)
        return response

    def get_transactions_since(self, transaction_id):
        path = f"/v3/accounts/{self.client.account_id}/transactions/sinceid"
        params = {
           ("id", transaction_id),
        }
        response = requests.get(self.client.base_url+path, headers=self.client.header, params=params)
        return response

