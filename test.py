from instagram.client import InstagramAPI
import sys

with open("client_info.txt", 'r') as f:
    s = f.readlines()
    access_token = s[0].rstrip()
    client_secret= s[1].rstrip()

api = InstagramAPI(access_token = access_token, client_secret=client_secret )

user_search = api.user_search(q = sys.argv[1], count = 5)

for i in user_search:
    print type(i)
    print '*' * 20
    print i.username
    print i.profile_picture
    print i.id
    

