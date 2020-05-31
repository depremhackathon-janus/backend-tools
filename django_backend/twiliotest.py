from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "ACe3a7ebbd5491edd44f9e02ec809b8a56"
# Your Auth Token from twilio.com/console
auth_token  = "aa4cb3bc4c3c1861dd64251b6e2ad2a8"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+905379125657", 
    from_="+12017338419",
    body="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.")

print(message.sid)