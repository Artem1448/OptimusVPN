from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command 
import asyncio
from datetime import datetime
import re

token = "8007679967:AAHPPuAaIBolbMLinyu0sO1chIwzyAQEOGk"
adminID = 2145885581

bot = Bot(token)
dp = Dispatcher()
 
@dp.message(Command('start'))
async def start(message: types.Message):
    await message.answer(
        text="🆘 Расскажи о своей проблеме и мы сразу начнём её решать!"
    )

@dp.message(lambda message: message.text and message.chat.id != adminID)
async def shareToAdmin(message: types.Message):
    
    senderName = f"{message.chat.first_name} {message.chat.last_name}"
    senderID = message.chat.id
    request = message.text
    time = datetime.now()

    ticket = f"Отправитель: <b>{senderName}</b>\nID клиента: {senderID}\nВремя: {time}\nСообщение:\n\n{request}"
    
    await bot.send_message(
        chat_id=adminID,
        text=ticket,
        parse_mode="HTML"
    )

@dp.message(
    lambda message: (
        message.reply_to_message and
        message.chat.id == adminID and
        message.reply_to_message.from_user.id == bot.id
    )
)
async def answerToClient(message: types.Message):
    text = message.reply_to_message.text
    needRow = re.search(r'ID клиента: (\d+)', text)
    senderID = needRow.group(1)

    await bot.send_message(
        chat_id=senderID,
        text=message.text
    )

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())