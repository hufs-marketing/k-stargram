# -*- coding:utf-8 -*-
import json
import time

def make_body(name, img_url, google_id, comment=" "):

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
            "labels" : [
                tag
                ]
            "images" : {
                "url" : img_url
                }
            }
    return payload

if __name__ == "__main__":
    url = "https://scontent.cdninstagram.com/hphotos-xat1/t51.2885-15/s640x640/sh0.08/e35/11348117_900427746699234_2027816491_n.jpg"
    post_pic("adel", url, "leesunkeuy2@gmail.com")

    
