import logging

import wikipedia
from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '2001182984:AAG0-62quIqKIBUjEco2ZTQPmgZU0ie1cOY'
wikipedia.set_lang('uz')
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
23    This handler will be called when user sends `/start` or `/help` command
   """
    await message.reply("Hi welcome to bot")


@dp.message_handler(regexp='(^cat[s]?$|puss)')
async def cats(message: types.Message):
    with open('data/cats.jpg', 'rb') as photo:
        await message.reply_photo(photo, caption='Cats are here 😺')


@dp.message_handler()
async def echo(message: types.Message):
   try:
       respond = wikipedia.summary(message.text)
       await message.answer(respond)
   except:
       await message.answer("Article not found")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)