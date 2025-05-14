import telebot

API_TOKEN = '7705828331:AAES0Sp5mAFYQA11qinCmdZcraMgvRgI1nY'
SOURCE_CHAT_ID = '-1002690977824'
DESTINATION_CHAT_ID = '-1002650951724'

bot = telebot.TeleBot(API_TOKEN)
@bot.message_handler(content_types=['text', 'photo', 'document', 'audio', 'video'])
def forward_message(message):
bot.forward_message(DESTINATION_CHAT_ID, message.chat.id, message.message_id)
bot.polling(none_stop=True)
