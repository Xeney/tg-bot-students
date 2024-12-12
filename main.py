from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, CallbackQueryHandler, MessageHandler, filters
import logging
import students

TOKEN = "TOKEN"
COMMANDS = ['/add', '/remove', '/list', '/help']
logging.basicConfig(filename='info.log', level=logging.INFO)

class MyBot():
    def __init__(self, token:str):
        self._app = ApplicationBuilder().token(token).build()

    async def command_start(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        message = "Добро пожаловать! Используйте команды:\n" \
                "1. /add <имя> - для добавления студента.\n" \
                "2. /remove <имя> - для удаления студента.\n" \
                "4. /list - для просмотра списка студентов."
        await update.message.reply_text(message)


    async def command_help(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        message = f'Используйте команды:'
        for i in COMMANDS:
            message += f'\n{COMMANDS.index(i)+1}. ' + i
        await update.message.reply_text(message)
    

    async def command_add(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        message = 'Добавление студента'
        if len(context.args) != 1:
            message = 'Должен быть аргумент!\n/add <имя> - для добавления студента.'
        else:
            try:
                message = students.Students().create(context.args[0])
            except Exception as e:
                message = str(e)
        await update.message.reply_text(message)


    async def command_list(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        message = 'Список студентов:'
        for i in students.Students.students:
            message += f'\n{i}'
        await update.message.reply_text(message)
    

    async def command_remove(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        message = f'Удаление студента'
        if len(context.args) != 1:
            message = 'Должен быть аргумент!\n/remove <имя> - для добавления студента.'
        else:
            try:
                message = students.Students().delete(context.args[0])
            except Exception as e:
                message = str(e)
        await update.message.reply_text(message)


    async def text_handler(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        message_text = update.message.text.lower()
        if message_text == "взлом пентагона":
            await update.message.reply_text("пф, это скам😂")
        else:
            await update.message.reply_text(f"Я не понял, что ты хочешь. /help ?\nТвоё сообщение: {message_text}")


    def handlers(self):
        self._app.add_handler(CommandHandler("start", self.command_start))
        self._app.add_handler(CommandHandler("help", self.command_help))
        self._app.add_handler(CommandHandler("add", self.command_add))
        self._app.add_handler(CommandHandler("list", self.command_list))
        self._app.add_handler(CommandHandler("remove", self.command_remove))
        self._app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, self.text_handler))
    
    def start(self):
        self._app.run_polling()


if __name__ == "__main__":
    logging.info("START KASH-BOT")
    bot = MyBot(token=TOKEN)
    bot.handlers()
    bot.start()
