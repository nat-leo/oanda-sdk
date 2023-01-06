import pytest
import os
from dotenv import load_dotenv
from oanda_sdk.client import Client

@pytest.fixture
def client():
    load_dotenv()
    ACCOUNT_ID = os.getenv("ACCOUNT_ID")
    API_TOKEN = os.getenv("API_TOKEN")
    client = Client()
    client.set_account_id(ACCOUNT_ID)
    client.set_api_token(API_TOKEN)
    yield client

@pytest.fixture
def client_fake():
    client_fake = Client()
    client_fake.set_account_id("account-fake")
    client_fake.set_api_token("api-token-fake")
    yield client_fake