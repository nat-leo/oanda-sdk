import requests

class Instrument:
    def __init__(self, client):
        self.client = client

    # Get pricing data formatted as candlestick data: highest price, lowest price, opening price, and closing price.
    def get_candles(self, instrument, price="M", granularity="S5", count="500", from_datetime=None, to_datetime=None, smooth=False, include_first=True, daily_alignment="17", alignment_timezone="America/New_York", weekly_alignment="Friday"):
        path = f"/v3/instruments/{instrument}/candles"
        params = (
            ("price", price),
            ("from", from_datetime),
            ("to", to_datetime),
            ("granularity", granularity),
            ("count", count),
            ("smooth", smooth),
            ("includeFirst", include_first),
            ("dailyAlignment", daily_alignment),
            ("alignmentTimezone", alignment_timezone),
            ("weeklyAlignment", weekly_alignment)
        )
        response = requests.get(self.client.base_url+path, headers=self.client.header, params=params)
        return response

    # get a snapshot of the order book at the specified time, or the latest snapshot if no time provided.
    def get_order_book(self, instrument, time=None):
        path = f"/v3/instruments/{instrument}/orderBook"
        params = (
            ("time", time),
        )
        response = requests.get(self.client.base_url+path, headers=self.client.header, params=params)
        return response
    
    # the hell is a position book? No one knows what this is. Look into it.
    def get_position_book(self, instrument, time=None):
        path = f"/v3/instruments/{instrument}/positionBook"
        params = (
            ("time", time),
        )
        response = requests.get(self.client.base_url+path, headers=self.client.header, params=params)
        return response       