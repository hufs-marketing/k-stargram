#-*- coding:utf-8 -*-
from instagram.client import InstagramAPI
import sys
import payload
from oauth2client import client
from googleapiclient import sample_tools
import json
from __future__ import print_function

with open("client_info.txt", 'r') as f:
    s = f.readlines()
    access_token = s[0].rstrip()
    client_secret= s[1].rstrip()

api = InstagramAPI(access_token = access_token, client_secret=client_secret )
dic = {}

with open("userid_list.txt", 'r') as f:
    p = f.readlines()

for i in p:
    user, name = i.split()[0], i.split()[1]
    dic[user] = {"name" : name, "photos_url" : []}



for k in dic.keys():
    recent_media, next_ = api.user_recent_media(user_id = k)
    for media in recent_media:
        if media.caption:
            dic[k]["photos_url"].append((media.images["standard_resolution"].url, media.caption))
        else:
            dic[k]["photos_url"].append((media.images["standard_resolution"].url, None))

for k in dic.keys():
    print "*" * 50
    print dic[k]["name"]
    for i in dic[k]["photos_url"]:
        print i 


#payload : can make make_payload method
def upload(payload):
    service, flags = sample_tools.init(
      argv, 'blogger', 'v3', __doc__, __file__,
      scope='https://www.googleapis.com/auth/blogger')
    posts = service.posts()
    request = posts.insert(blogId="485055035283972076", body=payload, isDraft = True, fetchImages = True)
    request.execute()
