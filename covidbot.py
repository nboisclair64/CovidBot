import twitter 

access_token = '1282041831409291267-TItwyHEvye8Doo4HLRVspUXVtXwsAu'
access_secret = '62eqCUBuELZzneZGrWm1P4hjJrBR0kK4aapLbpk4shH7Q'
consumer_secret = 'uPaksCO6XJNt6coTyO4tg9KLBd3Aoapktafkw3y7lAtWKM8vBa'
consumer_key = '0xe5EEREi3Y9SpxC0x1vXjDhp'
 
auth = tp.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tp.API(auth)