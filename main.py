from aiogram import Bot, Dispatcher, types, executor
from conflig import TELEGRAM_TOKEN

bot = Bot(token = TELEGRAM_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands="start")
async def start(message: types.Message):
    await message.reply('Привет, я твой первый БОТ')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)