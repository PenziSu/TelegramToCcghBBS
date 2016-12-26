# coding=UTF-8
import telegram
#------------------------------------#
bot = telegram.Bot(token='239286896:AAHslOboDCVFX0NARtR_qyeBsbN9OmWtg8M')
updates = bot.getUpdates()
for i in (-3,-2,-1,0,1,2):
    print "i= ",i
    chat_id = bot.getUpdates()[i].message.chat_id
    print "Chat_id= ",chat_id
#從-3~2都可以取得Chat_id值。

file_id = 'AgADBQADtKcxG4kaIg7HyOv7yBbo_jksyjIABD3uyx_7znpHW0wBAAEC'
newFile = bot.getFile(file_id)
#newFile.download('.\data\download456.jpg')