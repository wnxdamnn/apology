import asyncio
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# === ВСТАВЬ СЮДА НОВЫЙ ТОКЕН ===
TOKEN = "8720622769:AAEhAY6D0Nr5qsQTZW78biilkNe_aD1fgnU"

bot = Bot(token=TOKEN)
dp = Dispatcher()

keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="мои извинения")],
        [KeyboardButton(text="причины почему я тебя люблю")]
    ],
    resize_keyboard=True
)

reasons = """
• ты самая красивая
• с тобой тепло и спокойно
• люблю твой голос
• ты меня понимаешь как никто
• рядом с тобой я становлюсь лучше
• люблю твои глаза
• ты умеешь меня поддерживать
• с тобой даже молчать приятно
• ты моё самое родное
• люблю как ты улыбаешься
• ты делаешь мои дни светлее
• просто люблю тебя всей душой
"""

@dp.message(Command("start"))
async def start(message: types.Message):
    await message.answer(
        "я сделал это для тебя.\nвыбери что хочешь прочитать:",
        reply_markup=keyboard
    )

@dp.message(F.text == "мои извинения")
async def apology(message: types.Message):
    await message.answer(
        "прости меня за то, что бешу тебя, я не хочу тебя злить, но мне неприятно и от твоих слов тоже"
    )

@dp.message(F.text == "причины почему я тебя люблю")
async def love_reasons(message: types.Message):
    await message.answer(reasons)

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
