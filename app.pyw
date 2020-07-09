import time
from datetime import datetime as datetime
#hostPath = "hosts"
hostPath = "C:\\Windows\\System32\\drivers\\etc\\hosts"
redirect = "127.0.0.1"
websiteList = ["www.gmail.com", "gmail.com", "skype.com", "www.skype.com"]

while True:
    if  8 < datetime.now().hour < 19:
        print("Working Hours")
        with open(hostPath, 'r+') as file:
            content = file.read()
            file.seek(0,2)
            for i in websiteList:
                if i in content:
                    pass
                else:
                    file.write(redirect + "\t" + i + "\n")
    else:
        print("Fun Hours...")
        with open(hostPath, 'r+') as file:
            content = file.readlines()
            file.seek(0)
            for i in content:
                if not any(j in i for j in websiteList):
                    file.write(i)
            file.truncate()
    time.sleep(5)