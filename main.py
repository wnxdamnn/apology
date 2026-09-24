import asyncio
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# === ВСТАВЬ СЮДА СВОЙ ТОКЕН ===
TOKEN = "8720622769:AAEhAY6D0Nr5qsQTZW78biilkNe_aD1fgnU"

bot = Bot(token=TOKEN)
dp = Dispatcher()

# Кнопки
keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="мои извинения")],
        [KeyboardButton(text="причины почему я тебя люблю")],
        [KeyboardButton(text="1"), KeyboardButton(text="2")],
        [KeyboardButton(text="3"), KeyboardButton(text="4")],
        [KeyboardButton(text="поддержка по оценкам и егэ")]
    ],
    resize_keyboard=True
)

# Причины
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

# ASCII-арты
art1 = """
  ♥     ♥
♥   ♥   ♥
  ♥   ♥
    ♥
"""

art2 = """
    ♥♥
  ♥    ♥
 ♥  люблю  ♥
  ♥    ♥
    ♥♥
"""

art3 = """
♥     ♥     ♥
  ♥  ♥  ♥
    ♥♥♥
     ♥
"""

art4 = """
   ♥♥♥♥
 ♥      ♥
♥  тебе  ♥
 ♥      ♥
   ♥♥♥♥
"""

# Поддержка
support = """
по поводу оценок и егэ

я знаю что тебе сейчас тяжело
и всего очень много

но ты справишься
я в тебя верю

не дави на себя слишком сильно
ты умная
всё получится

если станет совсем плохо всегда пиши
я рядом

просто помни что я тебя люблю
и всегда поддержу(если ты конечно меня не переебашишь)
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

@dp.message(F.text == "1")
async def send_art1(message: types.Message):
    await message.answer(f"<pre>{art1}</pre>", parse_mode="HTML")

@dp.message(F.text == "2")
async def send_art2(message: types.Message):
    await message.answer(f"<pre>{art2}</pre>", parse_mode="HTML")

@dp.message(F.text == "3")
async def send_art3(message: types.Message):
    await message.answer(f"<pre>{art3}</pre>", parse_mode="HTML")

@dp.message(F.text == "4")
async def send_art4(message: types.Message):
    await message.answer(f"<pre>{art4}</pre>", parse_mode="HTML")

@dp.message(F.text == "поддержка по оценкам и егэ")
async def send_support(message: types.Message):
    await message.answer(support)

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
