from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

rep_kb = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Привет"), KeyboardButton(text="Пока")],
    [KeyboardButton(text="links"), KeyboardButton(text="dynamic")]
], resize_keyboard=True)

links_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Новости", url="https://ria.ru/")],
    [InlineKeyboardButton(text="Музыка", url="https://rus.hitmotop.com/artist/1701")],
    [InlineKeyboardButton(text="Видео", url="https://yandex.ru/video/search?text=%D0%B2%D0%B8%D0%B4%D0%B5%D0%BE")],
])

test = ["Опция 1", "Опция 2"]

dynamic_kb1 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Показать Больше", callback_data="next")],
])

async def dynamic_kb2():
    keyboard = InlineKeyboardBuilder()
    for key in test:
        keyboard.add(InlineKeyboardButton(text=key, callback_data=f"press_{key}"))
    return keyboard.as_markup()


