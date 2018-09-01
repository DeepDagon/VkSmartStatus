import vk_api #For work with VK
import datetime #Date and time
import time

#Autorization for one-step verification
vk = vk_api.VkApi(login = 'your login', password = 'your password')
vk.auth()

while True:
    #Set difference from UTC
    diff = datetime.timedelta(hours=5, minutes=0)
    t = (datetime.datetime.now(datetime.timezone.utc) + diff)

    #Current time and date
    nowTime = t.strftime("%H:%M")
    nowDate = t.strftime("%d.%m.%Y")

    #We get id friends in online
    on = vk.method("friends.getOnline") 

    #Count number of items in list
    count = len(on) 

    #Text in the status
    clock = nowTime + " ● " + nowDate + " ● "    
    status = clock + "Друзей онлайн: " + str(count)

    #Set status
    vk.method("status.set", {"text": str(status)}) 

    #Stop the script so that do not have a captcha
    time.sleep(45) 
