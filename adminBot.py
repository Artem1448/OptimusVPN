from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram import F
import asyncio
import paramiko

token = "7933765657:AAFLFYOSUubQl4xs926MuHQ-J-hdaerv4v8"
adminID = 2145885581

host = "194.87.87.21"
p = 22
user = "root"
passw = "zaqxsw123"

bot = Bot(token=token)
dp = Dispatcher()

def generateMainMenu():
    builder = InlineKeyboardBuilder()
    builder.row(
        types.InlineKeyboardButton(text="Статистика", callback_data="state")
    )
    builder.row(
        types.InlineKeyboardButton(text="Пользователи", callback_data="users")
    )
    builder.row(
        types.InlineKeyboardButton(text="Сервер", callback_data="server")
    )
    return builder.as_markup()

@dp.message(Command("start"))
async def start(message: types.Message):
    if message.chat.id == adminID:
        await message.answer(
            text="Добро пожаловать, Артём Игоревич!",
            reply_markup=generateMainMenu()
        )

@dp.callback_query(F.data == "state")
async def state(callback: types.CallbackQuery):
    builder = InlineKeyboardBuilder()
    builder.row(
        types.InlineKeyboardButton(text="Общий трафик", callback_data="totalTraffic"),
        types.InlineKeyboardButton(text="Трафик клиента", callback_data="clientTraffic")
    )
    builder.row(
        types.InlineKeyboardButton(text="Назад", callback_data="back")
    )
    await callback.message.edit_text(
        text="Выберите какую статистику вам нужно узнать:",
        reply_markup=builder.as_markup()
    )

@dp.callback_query(F.data == "users")
async def users(callback: types.CallbackQuery):
    builder = InlineKeyboardBuilder()
    builder.row(
        types.InlineKeyboardButton(text="Данные пользователя", callback_data="user"),
        types.InlineKeyboardButton(text="Данные детектора", callback_data="detector")
    )
    builder.row(
        types.InlineKeyboardButton(text="Добавить пользователя", callback_data="addUser"),
        types.InlineKeyboardButton(text="Удалить пользователя", callback_data="removeUser")
    )
    builder.row(
        types.InlineKeyboardButton(text="Заблокировать", callback_data="blockUser"),
        types.InlineKeyboardButton(text="Назад", callback_data="back")
    )
    await callback.message.edit_text(
        text="Выберите действие над пользователем:",
        reply_markup=builder.as_markup()
    )

@dp.callback_query(F.data == "back")
async def back(callback: types.CallbackQuery):
    await callback.message.edit_text(
        text="Добро пожаловать, Артём Игоревич!",
        reply_markup=generateMainMenu()
    )

@dp.callback_query(F.data == "server")
async def server(callback: types.CallbackQuery):
    builder = InlineKeyboardBuilder()
    builder.row(
        types.InlineKeyboardButton(text="Статистика сервера", callback_data="stateServer"),
        types.InlineKeyboardButton(text="Отдать команду", callback_data="commandServer")
    )
    builder.row(
        types.InlineKeyboardButton(text="Назад", callback_data="back")
    )
    await callback.message.edit_text(
        text="Выберите действие над сервером: ",
        reply_markup=builder.as_markup()
    )

@dp.callback_query(F.data == "totalTraffic")
async def totalTraffic(callback: types.CallbackQuery):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname=host, port=p, username=user, password=passw)
    stdin, stdout, stderr = ssh.exec_command(command="xray api statsquery --server=127.0.0.1:10085")
    output = stdout.read().decode('UTF-8')
    print(output)

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())