from twilio.rest import rest

# Your Account SID from twilio.com/console
account_sid = "ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
# Your Auth Token from twilio.com/console
auth_token  = "your_auth_token"

client = rest.TwilioRestClient(account_sid, auth_token)

message = client.sms.messages.create(
    to="+15558675309", #replace with your phone number
    from_="+15017250604", #replave with your Twilio number
    body="Hello from Python!")

print(message.sid)
