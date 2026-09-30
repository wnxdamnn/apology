import asyncio
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# === ВСТАВЬ СЮДА СВОЙ ТОКЕН ===
TOKEN = "8720622769:AAEhAY6D0Nr5qsQTZW78biilkNe_aD1fgnU"

bot = Bot(token=TOKEN)
dp = Dispatcher()

# Кнопка
keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="любимой жене")]
    ],
    resize_keyboard=True
)

# ASCII
art1 = """
    ✿    ✿
  ✿  ♥  ✿
 ✿   ♥   ✿
  ✿  ♥  ✿
    ✿✿✿
"""

art2 = """
   ♥✿♥✿♥
  ✿      ✿
 ✿  люблю  ✿
  ✿      ✿
   ♥✿♥✿♥
"""

art3 = """
     ✿
   ✿ ♥ ✿
  ✿  ♥  ✿
 ✿   ♥   ✿
✿    ♥    ✿
"""

@dp.message(Command("start"))
async def start(message: types.Message):
    await message.answer(
        "‎",  # пустое сообщение, чтобы просто показать кнопку
        reply_markup=keyboard
    )

@dp.message(F.text == "любимой жене")
async def for_wife(message: types.Message):
    # ASCII
    await message.answer(f"<pre>{art1}</pre>", parse_mode="HTML")
    await message.answer(f"<pre>{art2}</pre>", parse_mode="HTML")
    await message.answer(f"<pre>{art3}</pre>", parse_mode="HTML")

    # Картинки с букетами
    photos = [
        "https://images.unsplash.com/photo-1490750967868-88aa4486c936?w=800",
        "https://images.unsplash.com/photo-1519378058457-4c29a0a2efac?w=800",
        "https://images.unsplash.com/photo-1462275646964-a0e7786aa827?w=800",
        "https://images.unsplash.com/photo-1455659817273-f96807779a8a?w=800",
    ]

    for photo in photos:
        await message.answer_photo(photo)

    # Финальная надпись
    await message.answer("я тебя люблю, прости")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
