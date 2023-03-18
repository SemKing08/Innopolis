import logging
from config import TOKEN
from aiogram import Bot, Dispatcher, executor, types

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


# async def on_startup

@dp.message_handler()
async def echo(msg: types.Message):
    await msg.reply(msg.text)


if __name__ == '__main__':
    from aiogram import executor

    executor.start_polling(dp, skip_updates=True)
