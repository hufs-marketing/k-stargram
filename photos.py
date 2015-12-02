#-*- coding:utf-8 -*-
from instagram.client import InstagramAPI
import sys
import payload
from oauth2client import client
from googleapiclient import sample_tools
import json
def upload(payload):
    service, flags = sample_tools.init(
      argv, 'blogger', 'v3', __doc__, __file__,
      scope='https://www.googleapis.com/auth/blogger')
    posts = service.posts()
    request = posts.insert(blogId="485055035283972076", body=payload, isDraft = True, fetchImages = True)
    request.execute()

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
    label = i.split()[2]
    dic[user] = {"name" : name,"label" : label, "photos_url" : []}

for k in dic.keys():
    recent_media, next_ = api.user_recent_media(user_id = k)
    for media in recent_media:
        if media.caption:
            dic[k]["photos_url"].append((media.images["standard_resolution"].url, media.caption))
        else:
            dic[k]["photos_url"].append((media.images["standard_resolution"].url, None))

for k in dic.keys():
    print ("*" * 50)
    print (dic[k]["label"])
    name = dic[k]["label"]
    try:
        with open("insta/"+name, 'r') as f:
            pass
    except Exception as e:
        with open("insta/"+name, 'w') as f:
            json.dump(dic[k], f, ensure_ascii=False)
            continue
        print (e)
    with open("insta/" + name, 'r') as f:
        a = json.loads(f,encoding ="utf-8")

    for pic in dic[k]["photos_url"] :
        if pic not in a["photos_url"] : 
            if pic is None:
                payload = make_payload(dic[k]["label"], pic[0], "leesunkeuy2@gmail.com")
            else:
                payload = make_payload(dic[k]["label"], pic[0], "leesunkeuy2@gmail.com", comment = pic[1])
            upload(payload)
            a["photos_url"].append(pic)
            if len(a["photos_url"]) >= 10:
                a.pop()
    with open("insta/" + name, 'w') as f:
        json.dump(dic[k], f, ensure_ascii=False)
