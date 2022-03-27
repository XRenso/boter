import config as conf
import parser as pars
import aiogram
import asyncio
import logging
import aiogram.utils.markdown as md
from aiogram import Bot, types
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.dispatcher import Dispatcher, FSMContext
from aiogram.utils import executor
from aiogram.utils.markdown import text
from aiogram.contrib.fsm_storage.memory import MemoryStorage


bot = Bot(token = conf.token)
dp = Dispatcher(bot, storage=MemoryStorage())

logging.basicConfig(level=logging.INFO)



class book(StatesGroup):
    whick_book = State()


@dp.message_handler(state=book.whick_book)
async def books(message: types.Message, state:FSMContext):
    book = message.text[11:]

    await state.update_data(bookers=book)
    pars.get_url(book)
    await  bot.send_message(message.chat.id, pars.debbug())
    await state.finish()

@dp.message_handler(commands = ['start'])
async def start(message: types.Message):

    await message.answer('Ну че хочешь книжку по-бырому почитать? Тогда пиши ее название')



@dp.message_handler(commands=['find_book'])
async def get_text(message: types.Message):
    await book.whick_book.set()

if __name__ == '__main__':
	# loop = asyncio.get_event_loop()
	# loop.create_task(check_updates(120))
	executor.start_polling(dp, skip_updates = True)