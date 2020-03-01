from plaid import Client as PlaidClient
from twilio.rest import Client as TwilioClient
import json
import os

def nook_number(event, lambda_context):
  PLAID_CLIENT_ID = os.environ['plaid_client_id']
  PLAID_SECRET = os.environ['plaid_secret']
  PLAID_PUBLIC_KEY = os.environ['plaid_public_key']
  PLAID_ACCESS_TOKEN = os.environ['plaid_access_token']

  TWILIO_ACCOUNT_SID = os.environ['twilio_account_sid']
  TWILIO_AUTH_TOKEN = os.environ['twilio_auth_token']

  plaid_client = PlaidClient(client_id=PLAID_CLIENT_ID,
                  secret=PLAID_SECRET,
                  public_key=PLAID_PUBLIC_KEY,
                  environment='development')

  response = plaid_client.Accounts.balance.get(PLAID_ACCESS_TOKEN)

  account_balance_data = response['accounts'][0]['balances']

  account_limit = account_balance_data['limit']
  account_available = account_balance_data['available']
  account_balance = '%.2f'%(account_limit - account_available)

  account_balance_string = f'You currently have a balance of ${account_balance} on your credit card.'
  print(account_balance_string)

  twilio_client = TwilioClient(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

  print(twilio_client)

  message = twilio_client.messages.create(
                              body=account_balance_string,
                              from_=os.environ['from_number'],
                              to=os.environ['to_number']
                          )

  print(message)