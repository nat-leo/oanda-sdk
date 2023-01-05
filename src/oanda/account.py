import requests

class Account:
    def __init__(self, client) -> None: 
        self.client = client
        # we added self.uri mostly so we can test client.write_url(), and therefore verify that 
        # urls are being written properly and avoid the dreaded 400 Status Code.
        self.uri = ""
    
    # Get list of all accounts authorized with the API token provided by the client object.
    def get_accounts(self) -> requests.Response:
        self.uri = f"/v3/accounts"
        url = self.client.write_url(self.uri)
        response = requests.get(url, headers=self.client.header)
        return response

    # Get the summary for the account provided by the client object.
    def get_summary(self) -> requests.Response:
        self.uri = f"/v3/accounts/{self.client.account_id}/summary"
        url = self.client.write_url(self.uri)
        response = requests.get(url, headers=self.client.header)
        return response

    # Get all the instruments that the account can trade.
    def get_instruments(self) -> requests.Response:
        self.uri = f"/v3/accounts/{self.client.account_id}/instruments"
        url = self.client.write_url(self.uri)
        response = requests.get(url, headers=self.client.header)
        return response
    
    # Get all changes in the account since the transaction ID.
    # The transaction ID is required, otherwise you get a 400 Status Code
    def get_changes(self, transaction_id) -> requests.Response:
        # This might break if transaction ID is anything but a string AND an actual transaction id.
        # Also, might be a security flaw is the user input is not validated.
        self.uri = f"/v3/accounts/{self.client.account_id}/changes?sinceTransactionID={transaction_id}"
        url = self.client.write_url(self.uri)  
        response = requests.get(url, headers=self.client.header)
        return response
   