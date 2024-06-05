# @dp.message(F.text == '')
# async def (message:Message):
#     kb = [
#     [KeyboardButton(text='')]
#     ]
#     keyboard = ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
#     await message.answer('', reply_markup=)

import asyncio, sqlite3
from aiogram import Bot, Dispatcher, F, types
from aiogram.types import Message,  KeyboardButton, ReplyKeyboardRemove, ReplyKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from aiogram.filters import Command
from aiogram.utils.keyboard import InlineKeyboardBuilder

token = '6525200076:AAGFXJAg7fyfixqcxzIiJ-U23IikBgHOgqM'

name = ''
ordd = {}
numdish = 2
numdrink = 1

conn = sqlite3.connect('restaurant.db')

conn.execute('''CREATE TABLE IF NOT EXISTS orderss (
name TEXT,
dish TEXT,
drink TEXT)
''')

bot = Bot(token)
dp = Dispatcher()
@dp.message(Command('start'))
async def start(message:Message):
    kb1 = [
        [KeyboardButton(text='menu')]
    ]
    keyboard1 = ReplyKeyboardMarkup(keyboard=kb1, resize_keyboard=True)
    await message.answer("Welcome to the restaurant menu bot.\n"
                         "Click on menu button to see the dishes", reply_markup=keyboard1)

@dp.message(F.text == 'end')
async def end(message:Message):
    global dishhh, name, drink, fd
    conn = sqlite3.connect('restaurant.db')
    cursor = conn.cursor()
    cursor.execute('')
    kb1 = [
        [KeyboardButton(text='menu')]
    ]
    di = ''
    dr = ''
    for i in ordd.keys():
        if int(i) % 2 == 0:
            di += ordd[i]
        elif int(i) % 2 != 0:
            dr += ordd[i]
    keyboard1 = ReplyKeyboardMarkup(keyboard=kb1, resize_keyboard=True)
    cursor.execute('INSERT INTO orderss(name, dish, drink) VALUES ((?), (?), (?))', (name, di, dr))
    conn.commit()
    conn.close()
    await message.answer(f"You chose {di} and {dr}.\n"
                         f"Thank you for visiting our telegram restaurant bot!", reply_markup=keyboard1)

@dp.message(F.text == 'dish')
async def dish(message:Message):
    kb2 = [
        [types.KeyboardButton(text='soup'), types.KeyboardButton(text='borscht')],
        [types.KeyboardButton(text='potatoes with cutlets'), types.KeyboardButton(text='cabbage rolls')],
        [types.KeyboardButton(text='french fries'), types.KeyboardButton(text='burger')]
    ]
    keyboard2 = ReplyKeyboardMarkup(keyboard=kb2, resize_keyboard=True)
    await message.answer('Chose', reply_markup=keyboard2)

@dp.message(F.text == 'drink')
async def drink(message:Message):
    kb2 = [
        [types.KeyboardButton(text='coffe'), types.KeyboardButton(text='tea')],
        [types.KeyboardButton(text='lemonade'), types.KeyboardButton(text='cocktail')],
        [types.KeyboardButton(text='martini'), types.KeyboardButton(text='beer')],
        [types.KeyboardButton(text='back'), types.KeyboardButton(text='end')]
    ]
    keyboard2 = ReplyKeyboardMarkup(keyboard=kb2, resize_keyboard=True)
    await message.answer('Chose', reply_markup=keyboard2)


@dp.message(F.text == 'menu')
async def menu(message:Message):
    name = message.from_user.first_name
    kb2 = [
        [types.KeyboardButton(text='soup'), types.KeyboardButton(text='borscht')],
        [types.KeyboardButton(text='potatoes with cutlets'), types.KeyboardButton(text='cabbage rolls')],
        [types.KeyboardButton(text='french fries'), types.KeyboardButton(text='burger')]
    ]
    keyboard2 = ReplyKeyboardMarkup(keyboard=kb2, resize_keyboard=True)
    await message.answer("Chose your dish", reply_markup=keyboard2)

@dp.message(F.text == 'back')
async def menu(message:Message):
    name = message.from_user.first_name
    kb2 = [
        [types.KeyboardButton(text='dish'), types.KeyboardButton(text='drink')]
    ]
    keyboard2 = ReplyKeyboardMarkup(keyboard=kb2, resize_keyboard=True)
    await message.answer("Back to...", reply_markup=keyboard2)

@dp.message(F.text == 'more')
async def more(message:Message):
    kb8 = [
        [types.KeyboardButton(text='dish'), types.KeyboardButton(text='drink')],
        [KeyboardButton(text='end')]
    ]
    keyboard8 = ReplyKeyboardMarkup(keyboard=kb8, resize_keyboard=True)
    await message.answer("Come to...", reply_markup=keyboard8)

@dp.message(F.text == 'soup')
async def dish(message:Message):
    global name, ordd, numdish, numdrink
    ordd.update({numdish: 'soup '})
    numdish += 2
    kb3 = [
        [types.KeyboardButton(text='coffe'), types.KeyboardButton(text='tea')],
        [types.KeyboardButton(text='lemonade'), types.KeyboardButton(text='cocktail')],
        [types.KeyboardButton(text='martini'), types.KeyboardButton(text='beer')],
        [types.KeyboardButton(text='back'), types.KeyboardButton(text='end')]
    ]
    keyboard3 = ReplyKeyboardMarkup(keyboard=kb3, resize_keyboard=True)
    await message.answer('Good, now choose a drink', reply_markup=keyboard3)

@dp.message(F.text == 'borscht')
async def dish(message:Message):
    global name, ordd, numdish, numdrink
    ordd.update({numdish: 'borscht '})
    numdish += 2
    kb3 = [
        [types.KeyboardButton(text='coffe'), types.KeyboardButton(text='tea')],
        [types.KeyboardButton(text='lemonade'), types.KeyboardButton(text='cocktail')],
        [types.KeyboardButton(text='martini'), types.KeyboardButton(text='beer')],
        [types.KeyboardButton(text='back'), types.KeyboardButton(text='end')]
    ]
    keyboard3 = ReplyKeyboardMarkup(keyboard=kb3, resize_keyboard=True)
    await message.answer('Good, now choose a drink', reply_markup=keyboard3)

@dp.message(F.text == 'potatoes with cutlets')
async def dish(message:Message):
    global name, ordd, numdish, numdrink
    ordd.update({numdish: 'potatoes with cutlets '})
    numdish += 2
    kb3 = [
        [types.KeyboardButton(text='coffe'), types.KeyboardButton(text='tea')],
        [types.KeyboardButton(text='lemonade'), types.KeyboardButton(text='cocktail')],
        [types.KeyboardButton(text='martini'), types.KeyboardButton(text='beer')],
        [types.KeyboardButton(text='back'), types.KeyboardButton(text='end')]
    ]
    keyboard3 = ReplyKeyboardMarkup(keyboard=kb3, resize_keyboard=True)
    await message.answer('Good, now choose a drink', reply_markup=keyboard3)

@dp.message(F.text == 'cabbage rolls')
async def dish(message:Message):
    global name, ordd, numdish, numdrink
    ordd.update({numdish: 'cabbage rolls '})
    numdish += 2
    kb3 = [
        [types.KeyboardButton(text='coffe'), types.KeyboardButton(text='tea')],
        [types.KeyboardButton(text='lemonade'), types.KeyboardButton(text='cocktail')],
        [types.KeyboardButton(text='martini'), types.KeyboardButton(text='beer')],
        [types.KeyboardButton(text='back'), types.KeyboardButton(text='end')]
    ]
    keyboard3 = ReplyKeyboardMarkup(keyboard=kb3, resize_keyboard=True)
    await message.answer('Good, now choose a drink', reply_markup=keyboard3)

@dp.message(F.text == 'french fries')
async def dish(message:Message):
    global name, ordd, numdish, numdrink
    ordd.update({numdish: 'french fries '})
    numdish += 2
    kb3 = [
        [types.KeyboardButton(text='coffe'), types.KeyboardButton(text='tea')],
        [types.KeyboardButton(text='lemonade'), types.KeyboardButton(text='cocktail')],
        [types.KeyboardButton(text='martini'), types.KeyboardButton(text='beer')],
        [types.KeyboardButton(text='back'), types.KeyboardButton(text='end')]
    ]
    keyboard3 = ReplyKeyboardMarkup(keyboard=kb3, resize_keyboard=True)
    await message.answer('Good, now choose a drink', reply_markup=keyboard3)

@dp.message(F.text == 'burger')
async def dish(message:Message):
    global name, ordd, numdish, numdrink
    ordd.update({numdish: 'burger '})
    numdish += 2
    kb3 = [
        [types.KeyboardButton(text='coffe'), types.KeyboardButton(text='tea')],
        [types.KeyboardButton(text='lemonade'), types.KeyboardButton(text='cocktail')],
        [types.KeyboardButton(text='martini'), types.KeyboardButton(text='beer')],
        [types.KeyboardButton(text='back'), types.KeyboardButton(text='end')]
    ]
    keyboard3 = ReplyKeyboardMarkup(keyboard=kb3, resize_keyboard=True)
    await message.answer('Good, now choose a drink', reply_markup=keyboard3)


@dp.message(F.text == 'coffe')
async def drink(message:Message):
    kb5 = [
        [types.KeyboardButton(text='Latte'), types.KeyboardButton(text='Americano'), types.KeyboardButton(text='Glasse')],
        [types.KeyboardButton(text='back')]
    ]
    keyboard5 = ReplyKeyboardMarkup(keyboard=kb5, resize_keyboard=True)
    await message.answer("Chose a coffe type", reply_markup=keyboard5)

@dp.message(F.text == 'Latte')
async def coffes(message:Message):
    global name, ordd, numdish, numdrink
    ordd.update({numdrink: 'coffe(latte) '})
    numdrink += 2
    kb1 = [
        [types.KeyboardButton(text='end'), types.KeyboardButton(text='more')]
    ]
    keyboard1 = ReplyKeyboardMarkup(keyboard=kb1, resize_keyboard=True)
    await message.answer(f"Well, did you want chose somthing else", reply_markup=keyboard1)

@dp.message(F.text == 'Americano')
async def Americano(message:Message):
    global name, ordd, numdish, numdrink
    ordd.update({numdrink: 'coffe(Americano) '})
    numdrink += 2
    kb1 = [
        [types.KeyboardButton(text='end'), types.KeyboardButton(text='more')]
    ]
    keyboard1 = ReplyKeyboardMarkup(keyboard=kb1, resize_keyboard=True)
    await message.answer(f"Well, did you want chose somthing else", reply_markup=keyboard1)

@dp.message(F.text == 'Glasse')
async def Glasse(message:Message):
    global name, ordd, numdish, numdrink
    ordd.update({numdrink: 'coffe(Glasse) '})
    numdrink += 2
    kb1 = [
        [types.KeyboardButton(text='end'), types.KeyboardButton(text='more')]
    ]
    keyboard1 = ReplyKeyboardMarkup(keyboard=kb1, resize_keyboard=True)
    await message.answer(f"Well, did you want chose somthing else", reply_markup=keyboard1)

@dp.message(F.text == 'tea')
async def drink(message:Message):
    kb6 = [
        [types.KeyboardButton(text='Green'), types.KeyboardButton(text='White'), types.KeyboardButton(text='Black')],
        [KeyboardButton(text='back')]
    ]
    keyboard6 = ReplyKeyboardMarkup(keyboard=kb6, resize_keyboard=True)
    await message.answer("Chose a tea type", reply_markup=keyboard6)

@dp.message(F.text == 'Green')
async def Green(message:Message):
    global name, ordd, numdish, numdrink
    ordd.update({numdrink: 'tea(Green) '})
    numdrink += 2
    kb1 = [
        [types.KeyboardButton(text='end'), types.KeyboardButton(text='more')]
    ]
    keyboard1 = ReplyKeyboardMarkup(keyboard=kb1, resize_keyboard=True)
    await message.answer(f"Well, did you want chose somthing else", reply_markup=keyboard1)

@dp.message(F.text == 'White')
async def White(message:Message):
    global name, ordd, numdish, numdrink
    ordd.update({numdrink: 'tea(White) '})
    numdrink += 2
    kb1 = [
        [types.KeyboardButton(text='end'), types.KeyboardButton(text='more')]
    ]
    keyboard1 = ReplyKeyboardMarkup(keyboard=kb1, resize_keyboard=True)
    await message.answer(f"Well, did you want chose somthing else", reply_markup=keyboard1)

@dp.message(F.text == 'Black')
async def Green(message:Message):
    global name, ordd, numdish, numdrink
    ordd.update({numdrink: 'tea(Black) '})
    numdrink += 2
    kb1 = [
        [types.KeyboardButton(text='end'), types.KeyboardButton(text='more')]
    ]
    keyboard1 = ReplyKeyboardMarkup(keyboard=kb1, resize_keyboard=True)
    await message.answer(f"Well, did you want chose somthing else", reply_markup=keyboard1)

@dp.message(F.text == 'lemonade')
async def drink(message:Message):
    kb10 = [
        [types.KeyboardButton(text='Berry'), types.KeyboardButton(text='Coconut'), types.KeyboardButton(text='Tropical')],
        [KeyboardButton(text='back')]
    ]
    keyboard10 = ReplyKeyboardMarkup(keyboard=kb10, resize_keyboard=True)
    await message.answer("Chose a lemonade type", reply_markup=keyboard10)

@dp.message(F.text == 'Berry')
async def Berry(message:Message):
    global name, ordd, numdish, numdrink
    ordd.update({numdrink: 'lemonade(Berry) '})
    numdrink += 2
    kb1 = [
        [types.KeyboardButton(text='end'), types.KeyboardButton(text='more')]
    ]
    keyboard1 = ReplyKeyboardMarkup(keyboard=kb1, resize_keyboard=True)
    await message.answer(f"Well, did you want chose somthing else", reply_markup=keyboard1)

@dp.message(F.text == 'Coconut')
async def Coconut(message:Message):
    global name, ordd, numdish, numdrink
    ordd.update({numdrink: 'lemonade(Coconut) '})
    numdrink += 2
    kb1 = [
        [types.KeyboardButton(text='end'), types.KeyboardButton(text='more')]
    ]
    keyboard1 = ReplyKeyboardMarkup(keyboard=kb1, resize_keyboard=True)
    await message.answer(f"Well, did you want chose somthing else", reply_markup=keyboard1)

@dp.message(F.text == 'Tropical')
async def Tropical(message:Message):
    global name, ordd, numdish, numdrink
    ordd.update({numdrink: 'lemonade(Tropical) '})
    numdrink += 2
    kb1 = [
        [types.KeyboardButton(text='end'), types.KeyboardButton(text='more')]
    ]
    keyboard1 = ReplyKeyboardMarkup(keyboard=kb1, resize_keyboard=True)
    await message.answer(f"Well, did you want chose somthing else", reply_markup=keyboard1)
@dp.message(F.text == 'cocktail')
async def drink(message:Message):
    kb5 = [
        [types.KeyboardButton(text='Mojito'), types.KeyboardButton(text='Bumblebee'), types.KeyboardButton(text='Classic')],
        [KeyboardButton(text='back')]
    ]
    keyboard5 = ReplyKeyboardMarkup(keyboard=kb5, resize_keyboard=True)
    await message.answer("Chose a cocktail type", reply_markup=keyboard5)

@dp.message(F.text == 'Mojito')
async def Mojito(message:Message):
    global name, ordd, numdish, numdrink
    ordd.update({numdrink: 'cocktail(Mojito) '})
    numdrink += 2
    kb1 = [
        [types.KeyboardButton(text='end'), types.KeyboardButton(text='more')]
    ]
    keyboard1 = ReplyKeyboardMarkup(keyboard=kb1, resize_keyboard=True)
    await message.answer(f"Well, did you want chose somthing else", reply_markup=keyboard1)

@dp.message(F.text == 'Bumblebee')
async def Bumblebee(message:Message):
    global name, ordd, numdish, numdrink
    ordd.update({numdrink: 'cocktail(Bumblebee) '})
    numdrink += 2
    kb1 = [
        [types.KeyboardButton(text='end'), types.KeyboardButton(text='more')]
    ]
    keyboard1 = ReplyKeyboardMarkup(keyboard=kb1, resize_keyboard=True)
    await message.answer(f"Well, did you want chose somthing else", reply_markup=keyboard1)

@dp.message(F.text == 'Classic')
async def Classic(message:Message):
    global name, ordd, numdish, numdrink
    ordd.update({numdrink: 'coffe(Americano) '})
    numdrink += 2
    kb1 = [
        [types.KeyboardButton(text='end'), types.KeyboardButton(text='more')]
    ]
    keyboard1 = ReplyKeyboardMarkup(keyboard=kb1, resize_keyboard=True)
    await message.answer(f"Well, did you want chose somthing else", reply_markup=keyboard1)

@dp.message(F.text == 'martini')
async def drink(message:Message):
    kb1 = [
        [types.KeyboardButton(text='Rosato'), types.KeyboardButton(text='Bianco'), types.KeyboardButton(text='Fiero')],
        [KeyboardButton(text='back')]
    ]
    keyboard1 = ReplyKeyboardMarkup(keyboard=kb1, resize_keyboard=True)
    await message.answer("Chose a martini type", reply_markup=keyboard1)

@dp.message(F.text == 'Rosato')
async def Classic(message:Message):
    global name, ordd, numdish, numdrink
    ordd.update({numdrink: 'martini(Rosato) '})
    numdrink += 2
    kb1 = [
        [types.KeyboardButton(text='end'), types.KeyboardButton(text='more')]
    ]
    keyboard1 = ReplyKeyboardMarkup(keyboard=kb1, resize_keyboard=True)
    await message.answer(f"Well, did you want chose somthing else", reply_markup=keyboard1)

@dp.message(F.text == 'Bianco')
async def Bianco(message:Message):
    global name, ordd, numdish, numdrink
    ordd.update({numdrink: 'martini(Bianco) '})
    numdrink += 2
    kb1 = [
        [types.KeyboardButton(text='end'), types.KeyboardButton(text='more')]
    ]
    keyboard1 = ReplyKeyboardMarkup(keyboard=kb1, resize_keyboard=True)
    await message.answer(f"Well, did you want chose somthing else", reply_markup=keyboard1)

@dp.message(F.text == 'Fiero')
async def Fiero(message:Message):
    global name, ordd, numdish, numdrink
    ordd.update({numdrink: 'martini(Fiero) '})
    numdrink += 2
    kb1 = [
        [types.KeyboardButton(text='end'), types.KeyboardButton(text='more')]
    ]
    keyboard1 = ReplyKeyboardMarkup(keyboard=kb1, resize_keyboard=True)
    await message.answer(f"Well, did you want chose somthing else", reply_markup=keyboard1)

@dp.message(F.text == 'beer')
async def drink(message:Message):
    kb1 = [
        [types.KeyboardButton(text='end'), types.KeyboardButton(text='more')]
    ]
    keyboard1 = ReplyKeyboardMarkup(keyboard=kb1, resize_keyboard=True)
    await message.answer("Chose a beer type", reply_markup=keyboard1)

@dp.message(F.text == 'Brown Ale')
async def Brown_Ale(message:Message):
    global name, ordd, numdish, numdrink
    ordd.update({numdrink: 'beer(Brown Ale) '})
    numdrink += 2
    kb1 = [
        [types.KeyboardButton(text='end'), types.KeyboardButton(text='more')]
    ]
    keyboard1 = ReplyKeyboardMarkup(keyboard=kb1, resize_keyboard=True)
    await message.answer(f"Well, did you want chose somthing else", reply_markup=keyboard1)

@dp.message(F.text == 'Porter')
async def Porter(message:Message):
    global name, ordd, numdish, numdrink
    ordd.update({numdrink: 'beer(Porter) '})
    numdrink += 2
    kb1 = [
        [types.KeyboardButton(text='end'), types.KeyboardButton(text='more')]
    ]
    keyboard1 = ReplyKeyboardMarkup(keyboard=kb1, resize_keyboard=True)
    await message.answer(f"Well, did you want chose somthing else", reply_markup=keyboard1)

@dp.message(F.text == 'Stout')
async def Stout(message:Message):
    global name, ordd, numdish, numdrink
    ordd.update({numdrink: 'beer(Stout) '})
    numdrink += 2
    kb1 = [
        [types.KeyboardButton(text='end'), types.KeyboardButton(text='more')]
    ]
    keyboard1 = ReplyKeyboardMarkup(keyboard=kb1, resize_keyboard=True)
    await message.answer(f"Well, did you want chose somthing else", reply_markup=keyboard1)

async def main():
    print('bot is working')
    await dp.start_polling(bot)

asyncio.run(main())
