
import logging
 
from aiogram import Bot, Dispatcher, executor, types
 
API_TOKEN = '5487503565:AAGu3L2rLxVJAI4O85bG8AnmbDB1ZRu7gdo'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply("Assalomu alaykum men siz bilan suhbatlashishim mumkin!")


@dp.message_handler()
async def echo(message: types.Message):
    # old style:
    # await bot.send_message(message.chat.id, message.text)

    await message.reply(message.text)


if __name__ == '__main__':
    executor.start_polling(dp, )