import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# ===== НАСТРОЙКИ =====
BOT_TOKEN = os.getenv("8688539937:AAFryUHUf6sQc5AlNxgIOyTE1zqThO6eMvc")  # Замените на токен от BotFather
VIDEO_FILE_ID = "ВАШ_FILE_ID_КРУЖКА"  # Замените на ID из шага 2
YOUR_TELEGRAM_LINK = "https://t.me/NGtarasova921"  # Ссылка на ваш профиль

logging.basicConfig(level=logging.INFO)
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

# ===== ОБРАБОТЧИКИ =====

@dp.message(CommandStart())
async def start_command(message: types.Message):
    # Отправляем кружок
    try:
        await message.answer_video_note(video_note=VIDEO_FILE_ID)
    except Exception as e:
        await message.answer("Привет! (видео не загрузилось, но это не страшно)")
    
    # Отправляем текст с кнопкой
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Забрать 7 Reels", callback_data="get_7_reels")]
    ])
    await message.answer(
        "Привет! Я Наталья.\n\n"
        "Я помогаю экспертам не просто снимать Reels, а выстраивать блог, "
        "который хочется вести и который помогает продавать.\n\n"
        "Готова? Забирай свои 7 Reels 👇",
        reply_markup=kb
    )

@dp.callback_query(lambda c: c.data == "get_7_reels")
async def process_get_reels(callback: types.CallbackQuery):
    await callback.message.answer(
        "🎬 Твои 7 Reels на ближайшие 7 дней\n\n"
        "Я собрала их так, чтобы тебе не пришлось каждый день придумывать контент с нуля.\n\n"
        "📌 Сохрани это сообщение — здесь весь план на неделю.\n\n"
        "День 1 — Покажи экспертность\n"
        "День 2 — Ответь на вопрос\n"
        "День 3 — Разрушь миф\n"
        "День 4 — Покажи процесс\n"
        "День 5 — Покажи результат\n"
        "День 6 — Покажи себя\n"
        "День 7 — Расскажи, кому нужна твоя услуга"
    )
    
    # Кнопки выбора
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Мне нужен монтаж", callback_data="montage")],
        [InlineKeyboardButton(text="Мне нужен контент", callback_data="content")],
        [InlineKeyboardButton(text="Не понимаю, что мне нужно", callback_data="help")]
    ])
    await callback.message.answer(
        "А теперь скажи честно: где возникла сложность?\n"
        "Выбери, что сейчас актуальнее:",
        reply_markup=kb
    )
    await callback.answer()

@dp.callback_query(lambda c: c.data == "montage")
async def process_montage(callback: types.CallbackQuery):
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Хочу монтаж Reels", url=YOUR_TELEGRAM_LINK)]
    ])
    await callback.message.answer(
        "🎬 Тогда монтаж можно просто делегировать.\n\n"
        "Ты снимаешь исходники — я собираю из них готовый Reels.\n\n"
        "Тебе не нужно тратить время на CapCut, искать музыку, шрифты, "
        "переходы и разбираться, как всё это собрать.\n\n"
        "Ты занимаешься своей работой — я монтажом.",
        reply_markup=kb
    )
    await callback.answer()

@dp.callback_query(lambda c: c.data == "content")
async def process_content(callback: types.CallbackQuery):
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Хочу контент для эксперта", url=YOUR_TELEGRAM_LINK)]
    ])
    await callback.message.answer(
        "📝 У тебя уже есть контент. Ты просто не замечаешь его.\n\n"
        "Мы созваниваемся и разбираем, что происходит в твоей жизни и работе: "
        "клиенты, проекты, встречи, задачи, события, планы, мысли и ситуации.\n\n"
        "Я нахожу в этом темы для твоего блога и превращаю их в 7–10 готовых Reels.\n\n"
        "Для каждого Reels ты получаешь: тему → боль/смысл → хук → сценарий → "
        "что и как снять → СТА.",
        reply_markup=kb
    )
    await callback.answer()

@dp.callback_query(lambda c: c.data == "help")
async def process_help(callback: types.CallbackQuery):
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Написать Наталье", url=YOUR_TELEGRAM_LINK)]
    ])
    await callback.message.answer(
        "🤔 Не понимаешь, как вести блог?\n\n"
        "Давай разберёмся вместе. Напиши мне — я помогу понять, "
        "что и как тебе показывать.",
        reply_markup=kb
    )
    await callback.answer()

# ===== ЗАПУСК =====
async def main():
    print("Бот запущен...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
