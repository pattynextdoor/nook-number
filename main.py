from plaid import Client
import json
import os

def nook_number():
  PLAID_CLIENT_ID = os.environ['plaid_client_id']
  PLAID_SECRET = os.environ['plaid_secret']
  PLAID_PUBLIC_KEY = os.environ['plaid_public_key']
  PLAID_ACCESS_TOKEN = os.environ['plaid_access_token']

  client = Client(client_id=PLAID_CLIENT_ID,
                  secret=PLAID_SECRET,
                  public_key=PLAID_PUBLIC_KEY,
                  environment='development')

  response = client.Accounts.balance.get(PLAID_ACCESS_TOKEN)

  account_balance_data = response['accounts'][0]['balances']

  account_limit = account_balance_data['limit']
  account_available = account_balance_data['available']
  account_balance = '%.2f'%(account_limit - account_available)

  print(f'You currently have a balance of ${account_balance} on your credit card.')