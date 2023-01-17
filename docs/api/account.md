# Account Class

Class matches up with the [account endpoint](https://developer.oanda.com/rest-live-v20/account-ep/) of Oanda. 

Account gets you access to the account numbers available to trade with, a summary of account details, tradeable instruments, and any changes to account holdings.

## Usage

### Import

```
from oanda.account import Account
```

### Interface
Set these properties in your code.

```
Account(
    client = Client()
)
```

Call these methods in your code.

```
Account().get_accounts()
Account().get_summary()
Account().get_instruments()
Account().get_changes(transaction_id)
```

## Properties

### Defaults
```
Account(
    client = REQUIRED
    uri = ""
)
```

### REQUIRED Client(): client

A Client Object is required to create an instance of Account. See the docs for the [Client Class](client.md) to learn more.

### String: uri
```
Account().uri = ""
```
**Don't touch this:** uri is meant to store the uri path after the main url. One of the reasons for this property is to test complete urls and reduce the number 400 Malformed Requests, which are difficult to test.

This property gets set by all of the Account Methods and only replaces the uri after method calls, so uri holds the uri of the most recently called method.

## Methods

### get_accounts():

Takes no arguments.

Calling the method returns a [requests.Response](https://requests.readthedocs.io/en/latest/api/#requests.Response) object:
```
>>> account = Account(client).get_accounts()
<Response [200]>
```

The status code for the REST API call can be accessed as an integer as well:
```
>>> account.get_accounts().status_code
200
```

Get the list of accounts in JSON format:
```
>>> account.get_accounts().json()
{'accounts': [{'id': '000-000-0000000-000', 'tags': []}]}
```

### get_summary()

Get the account summary of the client.

Takes no arguments

Returns a [requests.Response](https://requests.readthedocs.io/en/latest/api/#requests.Response) object from the Requests library:
```
>>> account = Account(client).get_summary()
<Response [200]>
```

The status code for the REST API call can be accessed as an integer as follows:
```
>>> account.get_summary().status_code
200
```
Get the summary for the account as JSON:
```
>>> account.get_summary().json()
{'account': 
    {
        'guaranteedStopLossOrderMode': 'DISABLED', 
        'hedgingEnabled': False, 
        'id': '000-000-0000000-000', 
        'createdTime': '2019-07-25T19:56:49.578908772Z', 
        'currency': 'USD', 
        'createdByUserID': '0000000', 
        'alias': 'Primary', 
        'marginRate': '0.02', 
        'lastTransactionID': '35502', 
        'balance': '1127.4641', 
        'openTradeCount': 0, 
        'openPositionCount': 0, 
        'pendingOrderCount': 0, 
        'pl': '-345.0344', 
        'resettablePL': '-345.0344', 
        'resettablePLTime': '0', 
        'financing': '-436.7715', 
        'commission': '0.0000', 
        'dividendAdjustment': '0', 
        'guaranteedExecutionFees': '0.0000', 
        'unrealizedPL': '0.0000', 
        'NAV': '1127.4641', 
        'marginUsed': '0.0000', 
        'marginAvailable': '1127.4641', 
        'positionValue': '0.0000', 
        'marginCloseoutUnrealizedPL': '0.0000', 
        'marginCloseoutNAV': '1127.4641', 
        'marginCloseoutMarginUsed': '0.0000', 
        'marginCloseoutPositionValue': '0.0000', 
        'marginCloseoutPercent': '0.00000', 
        'withdrawalLimit': '1127.4641', 
        'marginCallMarginUsed': '0.0000', 
        'marginCallPercent': '0.00000'
    }, 
    'lastTransactionID': '35502'
}
```
### get_instruments()

Get an exhaustive list of all tradeable instruments and details.

Takes no arguments.

Returns a [requests.Response](https://requests.readthedocs.io/en/latest/api/#requests.Response) object from the Requests library:
```
>>> account.get_instruments()
<Response [200]>
```
Status codes can be accessed  as an integer:
```
>>> account.get_instruments().status_code
200
```
Getting the list of tradeable instruments as JSON:
```
>>> account.get_instruments().json()
# trust me you don't want to see the output
```

### get_changes()
Get a list of changes in account holdings after and not including a given transaction id, as well as the current state of the account.

Takes a required transaction_id as a string.

Returns a [requests.Response](https://requests.readthedocs.io/en/latest/api/#requests.Response) object from the Requests library:
```
>>> account.get_changes("35502")
<Response [200]>
```
Status codes can be accessed  as an integer:
```
>>> account.get_changes("35502").status_code
200
```
Getting the list of changes and account state as JSON:
```
>>> account.get_changes("35502").json()
{
    'changes': {
        'ordersCreated': [], 
        'ordersCancelled': [], 
        'ordersFilled': [], 
        'ordersTriggered': [], 
        'tradesOpened': [], 
        'tradesReduced': [], 
        'tradesClosed': [], 
        'positions': [], 
        'transactions': []
    }, 
    'state': {
        'unrealizedPL': '0.0000', 
        'NAV': '1127.4641', 
        'marginUsed': '0.0000', 
        'marginAvailable': '1127.4641', 
        'positionValue': '0.0000', 
        'marginCloseoutUnrealizedPL': '0.0000', 
        'marginCloseoutNAV': '1127.4641', 
        'marginCloseoutMarginUsed': '0.0000', 
        'marginCloseoutPercent': '0.00000', 
        'withdrawalLimit': '1127.4641', 
        'marginCallMarginUsed': '0.0000', 
        'marginCallPercent': '0.00000', 
        'orders': [], 
        'trades': [], 
        'positions': []
    }, 
    'lastTransactionID': '35502'
}
```
