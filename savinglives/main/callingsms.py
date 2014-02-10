from twilio.rest import TwilioRestClient
 
# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = "AC5b4554ce206c4d06dd07b282e8b07790"
auth_token  = "dc0b2014b6f566b7f5f88c802e283305"
client = TwilioRestClient(account_sid, auth_token)
 
message = client.sms.messages.create(body="Yo this Twilio actually works",
    to="+17706174766",    # Replace with your phone number
    from_="+19199487371") # Replace with your Twilio number
print message.sid
