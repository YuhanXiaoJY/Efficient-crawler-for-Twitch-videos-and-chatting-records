from sinVidCom import *
from serverff import *

anslist1 = []
anslist2 = []

listpath = "videoList"

with open(listpath) as p1:
    ururl = p1.read()
    uurl = ururl.split()

i = 1
while uurl[i] != "NBA:":
    tmp = filter(str.isdigit,uurl[i])
    anslist1.append(mergeSingleVedio(tmp))
    dovideo("GTA:",tmp)
    i += 1
with open("Data/ansGTA.json","w")as p1:
    p1.write(json.dumps(anslist1))


i += 1
while i < len(uurl):
    tmp = filter(str.isdigit,uurl[i])
    anslist2.append(mergeSingleVedio(tmp))
    dovideo("NBA:",tmp)
    i += 1
with open("Data/ansNBA.json","w")as p2:
    p2.write(json.dumps(anslist2))
