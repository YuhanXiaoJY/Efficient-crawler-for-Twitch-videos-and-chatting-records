#! python
from jsonHandler import *

commpart1 = "curl 'https://api.twitch.tv/v5/videos/"
commpart2 = "/comments?content_offset_seconds=" 
commpart3 = "' -H 'origin: https://www.twitch.tv' -H 'accept-encoding: gzip, deflate, br' -H 'accept-language: en-us' -H 'authorization: OAuth 6kdjkis74wd50ex6rcnx6zouznhqri' -H 'content-type: application/json; charset=UTF-8' -H 'accept: application/vnd.twitchtv.v5+json; charset=UTF-8' -H 'twitch-api-token: 7ab014ea1acf0765417cf4fbd3277a13' -H 'referer: https://www.twitch.tv/videos/"
commpart4 = "' -H 'authority: api.twitch.tv' -H 'x-requested-with: XMLHttpRequest' -H 'client-id: jzkbprff40iqj646a697cyrvl0zt2m6' -H 'user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36' --compressed"

def gencomm(video_id,second):
    comm = commpart1 + str(video_id) + commpart2 + str(second) + commpart3 + str(video_id) + commpart4
    return comm

def mergeSingleVedio(video_id):
    second = 0
    path = "Data/comment.json"
    comm = gencomm(video_id,second) + " > " + path
    os.system(comm)
    #print(comm)
    ans = simjs(path)
    last_time = 0

    if "comments" not in ans :
        return {}

    now_time = ans["comments"][-1]["time"]
    
    while now_time > last_time + 1e-2 :
        last_time = now_time
        second = int(last_time - 1)
        comm = gencomm(video_id,second) + " > " + path
        os.system(comm)
        tmp = simjs(path)
        if "comments" not in tmp:
            break
        cnt = 0
        for item in tmp["comments"] :
            if(item["time"] > last_time):
                ans["comments"].append(item)
                cnt += 1
        ans["messageNumber"] += cnt
        now_time = ans["comments"][-1]["time"]
    
    return ans
        

if __name__ == "__main__":
    print(mergeSingleVedio(328732167))
