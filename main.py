import vk_api #For work with VK
import datetime #Date and time
import time

#Autorization for one-step verification

vk_session = vk_api.VkApi(login, password)
try:
        vk_session.auth()
except vk_api.AuthError as error_msg:
        print(error_msg)

vk = vk_session.get_api()

#Set difference from UTC
diff = datetime.timedelta(hours=5, minutes=0)
t = (datetime.datetime.now(datetime.timezone.utc) + diff)
#Current time and date
nowTime = t.strftime("%H:%M")
nowDate = t.strftime("%d.%m.%Y")
#We get id friends in online
on = vk.friends.getOnline()
#Count number of items in list
count = len(on)
#Text in the status
clock = nowTime + " ● " + nowDate + " ● "
status = clock + "Друзей онлайн: " + str(count)
#Set status
vk.status.set(str(status))
#Stop the script so that do not have a captcha
