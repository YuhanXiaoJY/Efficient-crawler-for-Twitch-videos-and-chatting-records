#! python
# -*- coding:utf-8 -*-
import os
import json

def get_path():
    return os.path.dirname(__file__)

def timeHandler(t):
    # m = int(t // 60)
    # h = int(m // 60)
    # d = int(h // 24)
    # s = t - (d*24*60*60 + h*60*60 + m*60)
    # result = str(d).zfill(2)+':'+str(h).zfill(2)+':'+str(m).zfill(2)+':'+ str(s)
    pass

def simjs(path):
    path = get_path() + "/" + path
    with open(path) as p1:
        piles = json.load(p1)
    
    if 'error' in piles:
        return {}
    if len(piles["comments"]) == 0:
        return {}

    videoID = piles["comments"][0]["content_id"]
    diaJson = {}
    diaJson["videoID"] = videoID

    if "comments" not in piles:
        raise IndexError("No comments in this video")
    number = len(piles["comments"])

    diaJson["messageNumber"] = number
    diaJson["comments"] = []
    for pile in piles["comments"]:
        if pile["content_type"] != "video":
            raise IndexError("the type is not video")

        offsetTime = round(pile["content_offset_seconds"],3)
        userInfo = pile["commenter"]
        name = userInfo["name"]
        messageInfo = pile["message"]
        message = messageInfo["body"]
        diaJson["comments"].append({"time":offsetTime,"name":name, "message":message})
    return diaJson


if __name__ == "__main__":
    print(simjs("comment.json"))