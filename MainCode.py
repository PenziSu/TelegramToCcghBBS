import telegram
#------------------------------------#
bot = telegram.Bot(token='239286896:AAHslOboDCVFX0NARtR_qyeBsbN9OmWtg8M')
updates = bot.getUpdates()
chat_id = bot.getUpdates()[-1].message.chat_id
file_id = 'AgADBQADtKcxG4kaIg7HyOv7yBbo_jksyjIABD3uyx_7znpHW0wBAAEC'
newFile = bot.getFile(file_id)
newFile.download('.\data\download456.jpg')
