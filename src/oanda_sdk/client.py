class Client:
    def __init__(self, account_id="", api_token="", is_paper_trading = True):
        self.account_id = account_id
        self.api_token = api_token
        self.is_paper_trading = is_paper_trading
        self.base_url = "https://api-fxpractice.oanda.com" if is_paper_trading else "https://api-fxtrade.oanda.com"
        self.header = {
            'Content-Type': 'application/json',
            'Authorization': api_token,
        }

    def set_account_id(self, account_id: str) -> None:
        self.account_id = account_id
    
    # CODE SMELL
    # header doesn't update when the api token is set with set_api_token(),
    # which results in a 400 error is the api-token doesn't match the header's
    # api-token. The header is really what matters - it's the thing getting called.
    def set_api_token(self, api_token: str) -> None:
        self.api_token = api_token
        self.set_header(api_token)
    
    def set_header(self, api_token: str) -> None:
        self.header = {
            'Content-Type': 'application/json',
            'Authorization': api_token,
        }

    # CODE SMELL
    # Same as the set_api_token() method.
    def set_is_paper_trading(self, is_paper_trading: bool) -> None:
        self.is_paper_trading = is_paper_trading
        self.set_base_url(is_paper_trading)

    def set_base_url(self, is_paper_trading: bool) -> None:
        if is_paper_trading:
            self.base_url = "https://api-fxpractice.oanda.com" 
        else:
            self.base_url =  "https://api-fxtrade.oanda.com"

    # HELPERS
    # build_uri is so that we can test to make sure the uri is created as expected
    def write_url(self, uri: str) -> str:
        return self.base_url + uri