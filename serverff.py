import os

def dovideo(prfx,video_id):
        tmp1 = "Video/v" + str(video_id) + ".mp4"
        tmp2 = "Video/" + prfx + str(video_id) + ".mp4"
        comm1 = "youtube-dl https://www.twitch.tv/videos/" + str(video_id) + " -o " + tmp1
        comm2 = "ffmpeg -i " + tmp1 + " -r 3 " + tmp2
        #print(comm1)
        #print(comm2)
        os.system(comm1)
        os.system(comm2)

