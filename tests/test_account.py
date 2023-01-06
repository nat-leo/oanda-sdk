from oanda_sdk.account import Account

# WARNING: FLAKY TESTS
# tests for the Account object are all flaky, since they test whether
# or not an API call to Oanda is successful.

# Change this to non-flaky tests using Mocks, Adaptor Pattern, or VCR in the future.
# Change this is async to make these tests run faster in later versions.


################################
# Account.get_accounts() tests #
################################ 

# Warning: flaky test
# get_accounts() returns 200
def test_get_accounts(client):
    account = Account(client)
    response = account.get_accounts()
    assert response.status_code == 200,  "flaky test failed, 200 Expected"

# get_accounts() rewrites self.uri and we should see the aftermath.
def test_get_accounts_writes_to_uri(client_fake):
    account = Account(client_fake)
    account.get_accounts()
    assert account.uri == "/v3/accounts", "URI not set in Account Class."

# get_accounts() writes the correct URL
def test_get_accounts_writes_to_uri(client_fake):
    account = Account(client_fake)
    account.get_accounts()
    assert client_fake.base_url + account.uri == "https://api-fxpractice.oanda.com/v3/accounts", "Malformed URL in Account Class."


################################
# Account.get_summary() tests  #
################################ 

# Warning: flaky test
# get_summary() returns 200
def test_get_summary(client):
   assert Account(client).get_summary().status_code == 200, "flaky test failed, 200 Expected"

# get_summary() rewrites self.uri and we should see the aftermath.
def test_get_summary_writes_to_uri(client_fake):
    account = Account(client_fake)
    account.get_summary()
    assert account.uri == f"/v3/accounts/account-fake/summary", "URI not set in Account Class."

# get_summary() writes the correct URL
def test_get_summary_writes_to_uri(client_fake):
    account = Account(client_fake)
    account.get_summary()
    assert client_fake.base_url + account.uri == f"https://api-fxpractice.oanda.com/v3/accounts/account-fake/summary", "URI not set in Account Class."


###################################
# Account.get_instruments() tests #
################################### 

# Warning: flaky test
# get_instruments() returns 200
def test_get_instruments(client):
   assert Account(client).get_instruments().status_code == 200, "flaky test failed, 200 Expected"

# get_instruments() rewrites self.uri and we should see the aftermath.
def test_get_instruments_writes_to_uri(client_fake):
    account = Account(client_fake)
    account.get_instruments()
    assert account.uri == f"/v3/accounts/account-fake/instruments", "URI not set in Account Class."

# get_instruments() writes the correct URL
def test_get_instruments_writes_to_uri(client_fake):
    account = Account(client_fake)
    account.get_instruments()
    assert client_fake.base_url + account.uri == f"https://api-fxpractice.oanda.com/v3/accounts/account-fake/instruments", "URI not set in Account Class."


################################
# Account.get_changes() tests  #
################################ 

# Warning: flaky test
# get_changes() returns 200
def test_get_changes(client):
   assert Account(client).get_changes(transaction_id="35502").status_code == 200, "flaky test failed, 200 Expected"

# get_changes() rewrites self.uri and we should see the aftermath.
def test_get_changes_writes_to_uri(client_fake):
    account = Account(client_fake)
    account.get_changes(transaction_id="fake-transaction")
    assert account.uri == f"/v3/accounts/account-fake/changes?sinceTransactionID=fake-transaction", "URI not set in Account Class."

# get_changes() writes the correct URL
def test_changes_writes_to_uri(client_fake):
    account = Account(client_fake)
    account.get_changes("test")
    assert client_fake.base_url + account.uri == f"https://api-fxpractice.oanda.com/v3/accounts/account-fake/changes?sinceTransactionID=test", "URI not set in Account Class."
