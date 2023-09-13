import logging
from aiogram import types, Bot, Dispatcher, executor

from environs import Env

env = Env()
env.read_env()
TOKEN = env.str('BOT_TOKEN')

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start(mess: types.Message):
    await mess.answer('Бот запущен')


@dp.message_handler(content_types=['text'])
async def hello(mess: types.Message):
    if mess.text.lower() == 'привет':
        await mess.answer('Здравствуйте!')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)