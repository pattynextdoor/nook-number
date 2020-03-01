<img src="https://i.kym-cdn.com/entries/icons/original/000/027/162/tom.jpg" width=500/>

# Nook Number

Sometimes I spend a little bit more each month than I'm supposed to.

This function texts me every day with the balance on my main credit card. That's it.

## Design

The code & its dependencies live in [AWS Lambda](https://aws.amazon.com/lambda/), and is scheduled through [Amazon Eventbridge](https://aws.amazon.com/eventbridge/).

I use the Plaid API to get my account information. It's free since I linked <5 accounts, and Nook Number is only for personal use. Twilio's free tier (Programmable SMS) is used for sending the text message.

## Forking

Interested in using this yourself?

### API Services

Create an account with [Plaid](https://plaid.com/) and navigate to your [Development Dashboard](https://dashboard.plaid.com/overview/development) to fill in some of the environment variables listed below.

Create an account with [Twilio](https://www.twilio.com/) and create a free Programmable SMS number.

### Environment Variables
My personal information and data are set in environment variables in AWS Lambda.

Variable | Description
--- | ---
`PLAID_CLIENT_ID`| Available through Plaid Development Dashboard.
`PLAID_SECRET` | Available through Plaid Development Dashboard.
`PLAID_PUBLIC_KEY` | Available through Plaid Development Dashboard.
`PLAID_ACCESS_TOKEN` | Clone the [Plaid Quickstart Node project](https://github.com/plaid/quickstart/tree/master/node). Run the server with your own variable values and environment as `development` instead of `sandbox`. Then enter the information for the account you wish to track and copy the access token. This token does not expire but you can also regenerate it.
`TWILIO_ACCOUNT_SID` | Available through your Twilio console.
`TWILIO_AUTH_TOKEN` | Available through your Twilio console.
`FROM_NUMBER` | The phone number you generated in Twilio.
`TO_NUMBER` | Your personal phone number.
