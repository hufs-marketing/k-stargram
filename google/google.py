# -*- coding:utf-8 -*-
import requests
import json
import time
import gdata
from oauth_hook import OAuthHook


def post_pic(name, img_url, google_id, comment=" "):
    
    client_id = ""
    client_seceret = ""
    site = "https://www.googleapis.com"

    url = "https://www.googleapis.com/blogger/v3/blogs/485055035283972076/posts?fetchBody=true&fetchImages=true&isDraft=true&fields=author%2Cblog%2Ccontent%2Cimages%2Ctitle&key=Hywf81H5E3ydOzYwQ0LT-gTx"

    img_tag = "<img src=\"%s\">" %(img_url)
    body = "%s \n %s"%(img_tag, comment)
    date = time.strftime("%Y-%m-%d")
    title = "%s, %s" %(name, date)


    payload = {
            "blog" : {"id" : "485055035283972076"},
            "author" : {"id" : google_id},
            "content" : body, 
            "title" : title,
            "kind": "blogger#post",
            "images" : {
                "url" : img_url
                }
            }

    r = requests.post(url, data = json.dumps(payload))
    print r.text


if __name__ == "__main__":
    url = "https://scontent.cdninstagram.com/hphotos-xat1/t51.2885-15/s640x640/sh0.08/e35/11348117_900427746699234_2027816491_n.jpg"
    post_pic("adel", url, "leesunkeuy2@gmail.com")

    
