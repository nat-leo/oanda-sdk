# API Reference 

## Welcome to the API Reference for Oanda-SDK!

Oanda-SDK is built to be an exact mapping of the REST api for [Oanda](https://developer.oanda.com). Here you'll find a reference of Oanda-SDK's classes, properties, and methods in great detail. 

Check out [Getting Started](../getting-started.md) for a installation, walk-through, and a broad overview of the project, or read on for a deep dive into Oanda-SDK.

## Design Pattern

The builder design pattern is the basis for Oanda-SDK: You've gotta create an instance of the [Client Class](client.md) before using the main classes that make REST api calls: Account, Instrument, Order, Trade, Position, Transaction, and Pricing. Each of which takes an instance of the [Client Class](client.md) as an argument to make the API calls. 

Only the [Client Class](client.md) holds data relating to API tokens, account numbers, and headers.