# Импортируем библиотеки для бота, а также выполнение комманд
from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text
from Commands import Commands
from dotenv import load_dotenv
import os

# Создаём и иницаилизируем бота
bot = Bot(token=os.getenv('TOKEN'))
dp = Dispatcher(bot)
load_dotenv()

# Создаём запуск бота по команде /start
@dp.message_handler(commands="start")
async def start(message: types.Message):
    # Создаём главные кнопки
    start_buttons = ["Расписание", "Прогноз", "Курс валют", 'Оценки']
    keyboard_main = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard_main.add(*start_buttons)
    # Выводим приветствие
    await message.answer("Привет✌", reply_markup=keyboard_main)


# Создаём ответ на сообщение 'Оценки'
@dp.message_handler(Text(equals="Оценки"))
async def get_marks(message: types.Message):
    await message.answer("Минуточку...⏱")
    Commands.marks()
    await bot.send_photo(282345477, types.InputFile('screenshot_cropped.png'))


# Создаём ответ на сообщение 'Курс валют'
@dp.message_handler(Text(equals="Курс валют"))
async def get_valute(message: types.Message):
    await message.answer(Commands.valute())


# Создаём ответ на сообщение 'Расписание'
@dp.message_handler(Text(equals="Расписание"))
async def get_timetable(message: types.Message):
    await message.answer(Commands.timetable())


# Создаём ответ на сообщение 'Прогноз'
@dp.message_handler(Text(equals="Прогноз"))
async def get_weather(message: types.Message):
    await message.answer(Commands.weather())


def main():
    executor.start_polling(dp)


if __name__ == '__main__':
    main()
