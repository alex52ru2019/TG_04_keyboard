import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, FSInputFile, CallbackQuery

from config import TOKEN
import kb_dz as kb

bot = Bot(token=TOKEN) # https://t.me/aio_bot_my_bot
dp = Dispatcher()

@dp.message(CommandStart())
async def start(message: Message):
    await message.answer("Бот запущен", reply_markup=kb.rep_kb)

@dp.message(F.text == "Привет")
async def test_button(message: Message):
    await message.answer(f"Привет, {message.from_user.first_name}")

@dp.message(F.text == "Пока")
async def test_button(message: Message):
    await message.answer(f"Пока, {message.from_user.first_name}")

@dp.message(Command("links"))
@dp.message(F.text == "links")
async def links_kb(message: Message):
    await message.answer("Вот ссылки", reply_markup=kb.links_kb)

@dp.message(Command("dynamic"))
@dp.message(F.text == "dynamic")
async def dynamic_kb(message: Message):
    await message.answer("Хочешь больше?", reply_markup=kb.dynamic_kb1)

@dp.callback_query(F.data == "next")
async def next_kb(сallback: CallbackQuery):
    await сallback.message.edit_text("Выбери опцию", reply_markup= await kb.dynamic_kb2())

@dp.callback_query(F.data.startswith("press_"))
async def press_key(сallback: CallbackQuery):
    await сallback.answer("button pressed")
    await сallback.message.answer(f"Ты выбрал: {сallback.data[6:]} ")




async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())