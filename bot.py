import logging
from aiogram import Bot, Dispatcher, types
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils import executor

# Tokenni shu yerga yozing
TOKEN = "8179742930:AAFFB50osqvcwu7hArcu9RFYdIX0CeZyFp0"

# Bot va Dispatcher yaratamiz
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

# Klaviatura tugmalari
keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
keyboard.add(KeyboardButton("Salom"))
keyboard.add(KeyboardButton("Hazil ayt"), KeyboardButton("Ob-havo"))
keyboard.add(KeyboardButton("Motivatsiya"))

# /start va /help komandalarini qo'shish
@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: Message):
    await message.answer("Salom! Men Telegram botman. Quyidagi tugmalardan birini tanlashingiz mumkin:", reply_markup=keyboard)

# Oddiy savollarga javob berish
@dp.message_handler()
async def echo_message(message: Message):
    text = message.text.lower()
    
    if "salom" in text:
        await message.answer("Salom! Qanday yordam bera olaman?", reply_markup=keyboard)
    elif "qandaydursan" in text:
        await message.answer("Yaxshi, rahmat! O‘zingchi? 😊")
    elif "hazil ayt" in text:
        await message.answer("🐸 Bir kishi internetdan non sotib olibdi... Lekin u 'cookie' bo‘lib chiqibdi! 😂")
    elif "ob-havo" in text:
        await message.answer("Bugun ob-havo haqida aniq ma’lumot yo‘q, lekin doim yaxshi kayfiyat tilayman! ☀️")
    elif "motivatsiya" in text:
        await message.answer("🔥 Bugun harakat qiling, ertaga natija ko‘rasiz! Oldinga! 💪")
    else:
        await message.answer("Kechirasiz, bu so‘zni tushunmadim. 🤔", reply_markup=keyboard)

# Botni ishga tushiramiz
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True)
