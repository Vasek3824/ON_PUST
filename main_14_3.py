import logging

from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage

import texts_14_3
from config_14_3 import *
from keyboards_14_3 import *

logging.basicConfig(level=logging.INFO)
bot = Bot(token=API)
dp = Dispatcher(bot, storage=MemoryStorage())



@dp.message_handler(commands=['start'])
async def start(message):
    await message.answer(f'ДОбро пожаловать {message.from_user.username}' + texts_14_3.start, reply_markup=start_kb)

@dp.message_handler(text='О нас')
async def price(message):
    await message.answer(texts_14_3.abaut, reply_markup=start_kb)


@dp.message_handler(text='Купить')
async def get_buying_list(message):
    for i, j in enumerate(texts_14_3.products):
        imag_pr = texts_14_3.image_product[i]
        with open(imag_pr, 'rb') as img:
            opisanie = ', '.join(texts_14_3.vol[i])
            priceFin = ', '.join(price_kb[i])
            await message.answer(f'Название: {texts_14_3.products[i]}| \nОписание: {opisanie}|'
                                                    f'\nЦена: {priceFin}', )
            await message.answer_photo(img,)
    await message.answer('Выберите продукт для покупки: ', reply_markup=catalog_kb)

@dp.callback_query_handler(text='buy_jamCh')
async def buy_l(call):
    await call.message.answer(text='Выберите объем', reply_markup=buyJam1)
    await call.answer()

@dp.callback_query_handler(text='buy_jamCh1')
async def send_confirm_message(call):
    await call.message.answer('Вы успешно приобрели продукт!',)
    await call.answer()

@dp.callback_query_handler(text='buy_jamCh2')
async def send_confirm_message(call):
    await call.message.answer('Вы успешно приобрели продукт!',)
    await call.answer()

@dp.callback_query_handler(text='buy_jamCh3')
async def send_confirm_message(call):
    await call.message.answer('Вы успешно приобрели продукт!',)
    await call.answer()

@dp.callback_query_handler(text='buy_jamV') #'buy_jamE'])
async def buy_l(call):
    await call.message.answer(text='Выберите объем', reply_markup=buyJam2)# buyJam3, buyJam4)
    await call.answer()

@dp.callback_query_handler(text='buy_jamV1')
async def send_confirm_message(call):
    await call.message.answer('Вы успешно приобрели продукт!',)
    await call.answer()

@dp.callback_query_handler(text='buy_jamV2')
async def send_confirm_message(call):
    await call.message.answer('Вы успешно приобрели продукт!',)
    await call.answer()

@dp.callback_query_handler(text='buy_jamV3')
async def send_confirm_message(call):
    await call.message.answer('Вы успешно приобрели продукт!',)
    await call.answer()

@dp.callback_query_handler(text='buy_jamK') #buy_jamE
async def buy_l(call):
    await call.message.answer(text='Выберите объем', reply_markup=buyJam3)#buyJam4)
    await call.answer()

@dp.callback_query_handler(text='buy_jamK1')
async def send_confirm_message(call):
    await call.message.answer('Вы успешно приобрели продукт!',)
    await call.answer()

@dp.callback_query_handler(text='buy_jamK2')
async def send_confirm_message(call):
    await call.message.answer('Вы успешно приобрели продукт!',)
    await call.answer()

@dp.callback_query_handler(text='buy_jamK3')
async def send_confirm_message(call):
    await call.message.answer('Вы успешно приобрели продукт!',)
    await call.answer()

@dp.callback_query_handler(text='buy_jamE')
async def buy_l(call):
    await call.message.answer(text='Выберите объем', reply_markup=buyJam4)
    await call.answer()

@dp.callback_query_handler(text='buy_jamE1')
async def send_confirm_message(call):
    await call.message.answer('Вы успешно приобрели продукт!',)
    await call.answer()

@dp.callback_query_handler(text='buy_jamE2')
async def send_confirm_message(call):
    await call.message.answer('Вы успешно приобрели продукт!',)
    await call.answer()

@dp.callback_query_handler(text='buy_jamE3')
async def send_confirm_message(call):
    await call.message.answer('Вы успешно приобрели продукт!',)
    await call.answer()

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)