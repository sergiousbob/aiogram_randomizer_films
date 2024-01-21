from config import config
import random
from aiogram import F
import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from aiogram.client.session.aiohttp import AiohttpSession
from aiogram.types import FSInputFile


logging.basicConfig(level=logging.INFO)
session = AiohttpSession(proxy='http://proxy.server:3128')
bot = Bot(token=config.bot_token.get_secret_value(), session=session)

dp = Dispatcher()

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    kb = [
     
        [
             types.KeyboardButton(text="Комедия"),           
           
        ],

        [
             types.KeyboardButton(text="Мелодрама"),           
           
        ],
        [

            types.KeyboardButton(text="Драма"),
            types.KeyboardButton(text="Боевик"),
            types.KeyboardButton(text="Ужасы")
        ],
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="Выберите какой жанр:"
    )
    await message.answer("Добро пожаловать в наш телеграм-бот! 🐱🐱🐱\n Мы вам посоветуем подобрать фильм на вечер!🐱🐱🐱", reply_markup=keyboard)



@dp.message(F.text.lower() == "комедия")
async def comedy(message: types.Message):
    path = ["sbornik/comedy/1.jpg", 
            "sbornik/comedy/2.jpg",
            "sbornik/comedy/3.jpg",
            "sbornik/comedy/4.jpg",
            "sbornik/comedy/5.jpg"]
    a=random.choice(path)
    image_from_pc = FSInputFile(a)
    print (a)
    await message.reply("Подобрал вот такое🐱🐱🐱\n")
    await message.answer_photo (image_from_pc)
@dp.message(F.text.lower() == "драма")
async def drama(message: types.Message):
    path = ["sbornik/drama/1.jpg", 
            "sbornik/drama/2.jpg",
            "sbornik/drama/3.jpg",
            "sbornik/drama/4.jpg",
            "sbornik/drama/5.jpg"]
    a=random.choice(path)
    image_from_pc = FSInputFile(a)
    print (a)
    await message.reply("Подобрал вот такое🐱🐱🐱\n")
    await message.answer_photo (image_from_pc)

@dp.message(F.text.lower() == "мелодрама")
async def melodrama(message: types.Message):
    path = ["sbornik/melodrama/1.jpg", 
            "sbornik/melodrama/2.jpg",
            "sbornik/melodrama/3.jpg",
            "sbornik/melodrama/4.jpg",
            "sbornik/melodrama/5.jpg"]
    a=random.choice(path)
    image_from_pc = FSInputFile(a)
    print (a)
    await message.reply("Подобрал вот такое🐱🐱🐱\n")
    await message.answer_photo (image_from_pc)
    
@dp.message(F.text.lower() == "боевик")
async def boevik(message: types.Message):
    path = ["sbornik/boevik/1.jpg", 
            "sbornik/boevik/2.jpg",
            "sbornik/boevik/3.jpg",
            "sbornik/boevik/4.jpg",
            "sbornik/boevik/5.jpg"]
    a=random.choice(path)
    image_from_pc = FSInputFile(a)
    print (a)
    await message.reply("Подобрал вот такое🐱🐱🐱\n")
    await message.answer_photo (image_from_pc)
  
@dp.message(F.text.lower() == "ужасы")
async def uzhasy(message: types.Message):
    path = ["sbornik/uzhas/1.jpg", 
            "sbornik/uzhas/2.jpg",
            "sbornik/uzhas/3.jpg",
            "sbornik/uzhas/4.jpg",
            "sbornik/uzhas/5.jpg"]
    a=random.choice(path)
    image_from_pc = FSInputFile(a)
    print (a)
    await message.reply("Подобрал вот такое🐱🐱🐱\n")
    await message.answer_photo (image_from_pc)
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())