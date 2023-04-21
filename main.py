from aiogram import Bot, Dispatcher, executor, types
from private import TOKEN_API
from random import choice
from string import ascii_lowercase


HELP_COMMAND = '''
/help - список комманд
/start - начать работу с ботом
/description - описание бота
/count - счетчик самовызова
'''
DESCRIPTION = '''
Бот AxEsseNse
Здарова бродяги'''
count = 0


bot = Bot(TOKEN_API)
dp = Dispatcher(bot)


# @dp.message_handler()
# async def echo(message: types.Message):
#     if len(message.text.split()) > 2:
#         await message.answer(text=message.text.upper()) # написать в ответ сообщение text
@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.answer(text='Welcome to the club, buddy!')
    await message.delete()

@dp.message_handler(commands=['help'])
async def help_command(message: types.Message):
    await message.reply(text=HELP_COMMAND)

@dp.message_handler(commands=['description'])
async def description_command(message: types.Message):
    await message.reply(text=DESCRIPTION)

@dp.message_handler(commands=['count'])
async def count_command(message: types.Message):
    global count
    await message.answer(text=str(count))
    count += 1

@dp.message_handler()
async def main_event(message: types.Message):
    if '0' in message.text:
        await message.answer(text='YES')
    else:
        await message.answer(text='NO')
    await message.answer(text=choice(ascii_lowercase))


if __name__ == '__main__':
    executor.start_polling(dp)
