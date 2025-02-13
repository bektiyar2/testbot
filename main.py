from telegram.ext import Updater, MessageHandler, Filters

# Функция-обработчик для переадресации сообщений
def forward_message(update, context):
    # ID группы, в которую будут переадресовываться сообщения
    destination_group_id = () #указать ID группы, в которую будет переадресация сообщения
    message = update.message
    if message.text:
        text = message.text.lower()
    if 'заявка' in text:
    # Переадресация сообщения в другую группу
	    context.bot.forward_message(chat_id=destination_group_id, from_chat_id=update.effective_chat.id, message_id=update.message.message_id)

# Функция для обработки ошибок
def error(update, context):
    print(f"Ошибка: {context.error}")

# Создаем экземпляр класса Updater и передаем ему токен вашего бота
updater = Updater(token='номер токена', use_context=True)

# Получаем экземпляр диспетчера, чтобы зарегистрировать обработчики
dispatcher = updater.dispatcher

# Регистрируем обработчик переадресации сообщений
forward_handler = MessageHandler(Filters.all, forward_message)
dispatcher.add_handler(forward_handler)

# Регистрируем обработчик ошибок
dispatcher.add_error_handler(error)

# Запускаем бота
updater.start_polling()

