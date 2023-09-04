from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler

# Задайте состояния (если вам нужны)
STATE_1 = 1
STATE_2 = 2

# Обработчик команды /start
def start(update, context):
    update.message.reply_text("Привет! Я эхо-бот. Отправь мне что-нибудь, и я повторю.")

# Обработчик текстовых сообщений
def echo(update, context):
    text = update.message.text
    update.message.reply_text(f"Вы сказали: {text}")

# Обработчик неизвестных команд
def unknown(update, context):
    update.message.reply_text("Извините, я не понимаю эту команду.")

def main():
    # Замените 'YOUR_BOT_TOKEN' на ваш токен, который вы получили от @BotFather
    updater = Updater(token='6492517339:AAHdrxJ0qyoSDbgrfBVoxlyPKN3zlZUTNsg', use_context=True)

    dp = updater.dispatcher

    # Добавьте обработчики команды /start и текстовых сообщений
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

    # Добавьте обработчик неизвестных команд
    dp.add_handler(MessageHandler(Filters.command, unknown))

    # Запустите бота
    updater.start_polling()

    # Бот будет работать до принудительной остановки
    updater.idle()

if __name__ == '__main__':
    main()