#-*- coding:utf-8 -*-
from instagram.client import InstagramAPI
import sys

with open("client_info.txt", 'r') as f:
    s = f.readlines()
    access_token = s[0].rstrip()
    client_secret= s[1].rstrip()

api = InstagramAPI(access_token = access_token, client_secret=client_secret )
dic = {}
recent = {}
flag = 1
with open("userid_list.txt", 'r') as f:
    p = f.readlines()

for i in p:
    user, name = i.split()[0], i.split()[1]
    dic[user] = {"name" : name, "photos_url" : []}
    recent[user] = {"name" : name, "photos_url" : []}

for k in dic.keys():
    recent_media, next_ = api.user_recent_media(user_id = k)
    for media in recent_media:
        if media.caption:
            dic[k]["photos_url"].append((media.images["standard_resolution"].url, media.caption))
        else:
            dic[k]["photos_url"].append((media.images["standard_resolution"].url, None))

r = open("recent_url.txt", 'r')
u = open("upload_url.txt", 'w')
for k in dic.keys():
    print "*" * 50
    print dic[k]["name"]
    u.write(dic[k]["name"] + "\n")
    r.readline()  # first line(name) read
    line = r.readline() # second line(recent url) read
    flag = 1
    for i in dic[k]["photos_url"]:
        if line == (i[0] + "\n"):
			#print "There are no new photos\n"
            if flag == 1:
                recent[k]["photos_url"] = i
                flag = 0
            break
        print i
        u.write(i[0] + "\n")
        if flag == 1:
            recent[k]["photos_url"] = i
            flag = 0
u.close() #upload_url close
r.close() #recent_url close
	
f = open("recent_url.txt", 'w')

for k in recent.keys():
#   print "------------------------------------------------------"
#   print recent[k]["name"]
    f.write(recent[k]["name"] + "\n")#recent[k]["photos_url"][0] + "\n")
#	f.write("\n")
#    print recent[k]["photos_url"][0]
    f.write(recent[k]["photos_url"][0] + "\n")

f.close()


