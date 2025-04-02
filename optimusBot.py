from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram import F
import random
import asyncio
from yoomoney import Quickpay

token = "7827731072:AAEjVP5qSTyizjurSTHmL_jMO4t4hL28Iys"
wallet = "4100119079609641"
access_token = "4100119079609641.753F9FAF302F212692018D3E6A0328788B6AC4DB75E9AA7B8E449D451CA14FF2FD27757FE65CD601385BA266034F0A354FFAB6A883C70E22D9BFEDE95B60025E8FCE12352230E947593B4AB05481273DF80F4AB9277CCF6D4EB0545C915E7390F81FA2BC0B5EA40961700618B36CF88DF71F5F5F376190CF88B520D9B3536488"

bot = Bot(token)
dp = Dispatcher()

def generatePaymentLink(userID, price):
    global wallet
    quickpay = Quickpay(
        receiver=wallet,
        quickpay_form="small",
        targets="Optimus VPN",
        paymentType="SBPP",
        sum=5,
        label=f"{userID}_{random.randrange(1, 100000)}"
    )
    return quickpay.redirected_url 

def generateMainMenu():
    builder = InlineKeyboardBuilder()
    builder.row(
        types.InlineKeyboardButton(text="🌟 Получить ключ", callback_data="menu-subs"),
    )
    builder.row(
        types.InlineKeyboardButton(text="👤 Мой аккаунт", callback_data="my-account"),
        types.InlineKeyboardButton(text="🆘 Нужна помощь", url="https://t.me/OptimusVpnSupportBot"),
    )
    builder.row(
        types.InlineKeyboardButton(text="🗣 Перейти в чат", url="https://t.me/+uk0I8AZikGM3NzVi")
    )
    return builder

def generateButtonOnRow(builder: InlineKeyboardBuilder, text, action):
    builder.row(
        types.InlineKeyboardButton(text=text, callback_data=action)
    )

@dp.message(Command('start'))
async def start(message: types.Message):
    builder = generateMainMenu()
    await message.answer(
        "🔒 Приватность — не роскошь, а стандарт.",
        reply_markup=builder.as_markup()
    )

@dp.callback_query(F.data == "menu-subs")
async def getMenuSubs(callback: types.CallbackQuery):
    builder = InlineKeyboardBuilder()
    generateButtonOnRow(builder, "1 мес. | 99 р. | ~99p/мес.", "chekingBalance99")
    generateButtonOnRow(builder, "2 мес. | 189 р. | ~94p/мес.", "chekingBalance189")
    generateButtonOnRow(builder, "3 мес. | 269 р. | ~89p/мес.", "chekingBalance269")
    generateButtonOnRow(builder, "6 мес. | 499 р. | ~83p/мес.", "chekingBalance499")
    generateButtonOnRow(builder, "12 мес. | 899 р. | ~74p/мес.", "chekingBalance899")
    builder.row(
        types.InlineKeyboardButton(text="🔙 Назад", callback_data="back")
    )
    await callback.message.edit_text(
        "🛠 Чтобы получить ключ, необходима подписка.\n\n🔥 Доступные тарифы: ",
        reply_markup=builder.as_markup(),
    )

@dp.callback_query(F.data.startswith('chekingBalance'))
async def check(callback: types.CallbackQuery):
    builder = InlineKeyboardBuilder()
    data = callback.data
    price = data.replace("chekingBalance", "")
    balance = 0
    text = ""
    payLink = generatePaymentLink(callback.message.chat.id, price)
    if balance < int(price):
        text = f"⚠️ Пополните, пожалуйста, баланс!\n\n💰 Баланс: {balance} руб.\n✨ Стоимость: {price} руб."
        builder.row(types.InlineKeyboardButton(text="💳 Пополнить баланс", url=payLink))
    else:
        text = f"💰 Баланс: {balance} руб.\n✨ Стоимость: {price} руб."
        builder.row(types.InlineKeyboardButton(text="💳 Купить", callback_data="buy"))
    builder.row(types.InlineKeyboardButton(text="🔙 Назад", callback_data="backTarifs"))
    await callback.message.edit_text(
        text=text,
        reply_markup=builder.as_markup()
    )
                

@dp.callback_query(F.data == "backTarifs")
async def back(callback: types.CallbackQuery):
    builder = InlineKeyboardBuilder()
    generateButtonOnRow(builder, "1 мес. | 99 р. | ~99p/мес.", "chekingBalance99")
    generateButtonOnRow(builder, "2 мес. | 189 р. | ~94p/мес.", "chekingBalance189")
    generateButtonOnRow(builder, "3 мес. | 269 р. | ~89p/мес.", "chekingBalance269")
    generateButtonOnRow(builder, "6 мес. | 499 р. | ~83p/мес.", "chekingBalance499")
    generateButtonOnRow(builder, "12 мес. | 899 р. | ~74p/мес.", "chekingBalance899")
    builder.row(
        types.InlineKeyboardButton(text="🔙 Назад", callback_data="back")
    )
    await callback.message.edit_text(
        "🛠 Чтобы получить ключ, необходима подписка.\n\n🔥 Доступные тарифы: ",
        reply_markup=builder.as_markup(),
    )

@dp.callback_query(F.data == "back")
async def back(callback: types.CallbackQuery):
    builder = generateMainMenu()
    await callback.message.edit_text(
        "🔒 Приватность — не роскошь, а стандарт.",
        reply_markup=builder.as_markup()
    )


@dp.callback_query(F.data == "main-menu")
async def returnMainMenu(callback: types.CallbackQuery):
    builder = generateMainMenu()
    await callback.message.edit_text(
        "🔒 Приватность — не роскошь, а стандарт.",
        reply_markup=builder.as_markup()
    )

@dp.callback_query(F.data == "my-account")
async def getCustomAccount(callback: types.callback_query):
    builder = InlineKeyboardBuilder()
    builder.row(
        types.InlineKeyboardButton(text="🔙 Назад", callback_data="back")
    )
    id = callback.message.chat.id
    balance = 100
    days = 0

    info = f"🤫  ID: {id}\n\n⏳ Осталось: {days} дней \n\n💰 Баланс: {balance} р\n\n"

    await callback.message.edit_text(
        text=info,
        reply_markup=builder.as_markup()
    )


async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())


