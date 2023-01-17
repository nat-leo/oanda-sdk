# Intrument Class

Get historical prices of currency pairs and order books.

## Usage

### Import

```
from oanda.instrument import Instrument
```

### Interface
Set these properties in your code.

```
Instrument(
    client = Client()
)
```

Call these methods in your code.

```
Instrument().get_candles()
Instrument().get_order_book()
Instrument().get_position_book()
```

## Properties

### REQUIRED Client(): client

A Client Object is required to create an instance of Instrument. See the docs for the [Client Class](client.md) to learn more.

## Methods

### get_candles():

Returns a request objects containing a list of OHLC formatted currency data (A.K.A. candles.)

**Arguments**

 - **instrument:** String (Required) Get the historical data for this currency pair.

 - **price:** String (Default="M"). The type of historical data: Bids ("B"), Asks ("A"), Both ("BA"), or Midpoint ("M").

 - **granularity:** String (Default="S5"). Timescale for formatting data. "M5" would be a new OHLC data point every 5 minutes.

 - **count:** String (Default="500"). The number of OHLC datapoints to be returned. 

 - **from_datetime:** String (Default=None). The start time for the data. The datetime of the first OHLC datapoint. 

 - **to_datetime:** String (Default=None). The end time for the data. The datetime of the last OHLC datapoint.

 - **smooth:** String Boolean (Default="False"). If "True", the next OHLC datapoint uses the previous close as its opening price. If "False", the next OHLC datapoint uses the first price of the time range.

 - **include_first:** String (Default=None)

 - **daily_alignment:** String (Default="17"). If using "D" for granularity, this picks which hour of the day the OHLC data aligns to. 17 would means days are from 5pm to 5pm.

 - **alignment_timezone:** String (Default="America/New_York") The timezone for daily_alignment.

 - **weekly_alignment:** String (Default="Friday") If using "W" for granularity, this picks which day of the week the OHLC data aligns to. "Friday" means the week starts and ends on Friday.

Calling the method returns a [requests.Response](https://requests.readthedocs.io/en/latest/api/#requests.Response) object:
```
>>> instrument = Instrument(client).get_candles("EUR_USD")
<Response [200]>
```

The status code for the REST API call can be accessed as an integer as well:
```
>>> instrument.get_candles().status_code
200
```

Get 2 points of historical data for EUR/USD in JSON format:
```
>>> instrument.get_candles("EUR_USD", count="2").json()
{'instrument': 'EUR_USD', 
 'granularity': 'S5', 
 'candles': 
    [{'complete': True, 
      'volume': 4, 
      'time': '2023-01-17T06:00:05.000000000Z', 
      'mid': 
        {'o': '1.08308', 
         'h': '1.08308', 
         'l': '1.08306', 
         'c': '1.08306'}}, 
     {'complete': False, 
      'volume': 2, 
      'time': '2023-01-17T06:00:10.000000000Z', 
      'mid': 
        {'o': '1.08304', 
         'h': '1.08304', 
         'l': '1.08302', 
         'c': '1.08302'}}]}
```

### get_order_book()

Get a snapshot of the order book for the given currency at the given time.

**Arguments**

 - **instrument:** String (Required). Get the order book for this currency pair.
 - **time:** String. The time of the order book snapshot to fetch.

Returns a [requests.Response](https://requests.readthedocs.io/en/latest/api/#requests.Response) object from the Requests library:
```
>>> instrument = Instrument(client).get_order_book()
<Response [200]>
```

The status code for the REST API call can be accessed as an integer as follows:
```
>>> instrument.get_order_book().status_code
200
```
Get the summary for the account as JSON:
```
>>> instrument.get_order_book().json()
TODO
```
### get_position_book()

TODO

**Arguments**

 - **instrument:** String (Required). Get the position book for this currency pair.
 - **time:** String. The time of the order book snapshot to fetch.

Returns a [requests.Response](https://requests.readthedocs.io/en/latest/api/#requests.Response) object from the Requests library:
```
>>> instrument.get_position_book()
<Response [200]>
```
Status codes can be accessed  as an integer:
```
>>> instrument.get_position_book().status_code
200
```
Getting the list of tradeable instruments as JSON:
```
>>> instrument.get_position_book().json()
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
