# from telegram import Update
# from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# app = ApplicationBuilder().token("6022340038:AAFqgfIjX-_HOPSmGt14N8Tf2UEPp5zBtts").build()
# app.run_polling()

# async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
#     await update.message.reply_text(f'Hello {update.effective_user.first_name}')

# app.add_handler(CommandHandler("hello", hello))
# Адрес нашего бота https://web.telegram.org/k/#@Bot_traveltikets_bot

import aiohttp
import time
import logging
from aiogram import Bot, Dispatcher, executor, types

# 'UTF-8-sig'
logging.basicConfig(level=logging.INFO, filename="Putevka\\bot_log.csv", filemode="w",
                    format="%(asctime)s: %(levelname)s %(funcName)s-%(lineno)d %(message)s")


MSG = "{}, choose an action:"

bot = Bot("6022340038:AAFqgfIjX-_HOPSmGt14N8Tf2UEPp5zBtts")
dp = Dispatcher(bot=bot)

@dp.message_handler(commands=['start'])
async def start_handler(message: types.Message):
    user_id = message.from_user.id
    user_name = message.from_user.first_name
    user_full_name = message.from_user.full_name
    user_bot = message.from_user.is_bot
    user_message = message.text
    logging.info(f'{user_id=} {user_bot=} {user_message=}')
    await message.reply(f"Hi, {user_full_name}!")
    time.sleep(1)
    btns = types.ReplyKeyboardMarkup(row_width=4)
    btn_calc = types.KeyboardButton('/calculator')
    btn_notes = types.KeyboardButton('/notes')
    btn_image = types.KeyboardButton('/send_image')
    btn_out = types.KeyboardButton('/quit')
    btns.add(btn_calc, btn_notes, btn_image, btn_out)
    await bot.send_message(user_id, MSG.format(user_name), reply_markup=btns)

@dp.message_handler(commands=['quit'])
async def quit_handler(message: types.Message):
    await bot.send_message(message.from_user.id, 'Goodbye! See you...',
                           reply_markup=types.ReplyKeyboardRemove())

@dp.message_handler(commands=['notes'])
async def quit_handler(message: types.Message):
    await bot.send_message(message.from_user.id, 'This is notes!',
                           reply_markup=types.ReplyKeyboardRemove())


@dp.message_handler(commands=['send_image'])
async def cmd_send_image(message):
    with open("Putevka\Cats.jpg", "rb") as f:
        await bot.send_photo(message.chat.id, photo=f)


# async def get_image(url):
#     async with aiohttp.ClientSession() as session:
#         async with session.get(url) as resp:
#             if resp.status != 200:
#                 # handle error here
#                 return None
#             image = await resp.content.read()
#             return image

# async def save_image(image):
#     with open("random_image.jpg", "wb") as f:
#         f.write(image)

# async def main():
#     image = await get_image("https://random-d.uk/api/random")
#     if image is not None:
#         await save_image(image)

# value = ""
# old_value = ""
# keyboard = types.InlineKeyboardMarkup(resize_keyboard=True)
# keyboard.row(types.InlineKeyboardButton("C", callback_data="C"),
#              types.InlineKeyboardButton("<=", callback_data="<="),
#              types.InlineKeyboardButton("(", callback_data="("),
#              types.InlineKeyboardButton("/", callback_data="/"))
# keyboard.row(types.InlineKeyboardButton("7", callback_data="7"),
#              types.InlineKeyboardButton("8", callback_data="8"),
#              types.InlineKeyboardButton("9", callback_data="9"),
#              types.InlineKeyboardButton("*", callback_data="*"))
# keyboard.row(types.InlineKeyboardButton("Button 1", callback_data="4"),
#              types.InlineKeyboardButton("5", callback_data="5"),
#              types.InlineKeyboardButton("6", callback_data="6"),
#              types.InlineKeyboardButton("-", callback_data="-"))
# keyboard.row(types.InlineKeyboardButton("1", callback_data="1"),
#              types.InlineKeyboardButton("2", callback_data="2"),
#              types.InlineKeyboardButton("3", callback_data="3"),
#              types.InlineKeyboardButton("+", callback_data="+"))
# keyboard.row(types.InlineKeyboardButton("0", callback_data="0"),
#              types.InlineKeyboardButton(",", callback_data="."),
#              types.InlineKeyboardButton(")", callback_data=")"),
#              types.InlineKeyboardButton("=", callback_data="="))

# @dp.message_handler(commands=['calculator'])
# async def start_handler(message: types.Message):
#     await bot.send_message(message.from_user.id, "I open the calculator")
#     if value == "":
#         await bot.send_message(message.from_user.id, "0", reply_markup=keyboard)
#     else:
#         await bot.send_message(message.from_user.id, value, reply_markup=keyboard)

# @dp.callback_query_handler(lambda c: True)
# async def callback_calc(query):

#     global value, old_value
#     data = query.data

#     if data == "C":
#         value = ""
#     elif data == "<=":
#         if value != "":
#             if len(value) == 1:
#                 value = ""
#             else:
#                 value = value[:len(value)-1]
#     elif data == "=":
#         try:
#             value = str(eval(value))
#         except:
#             value = "Error"
#     else:
#         value += data

#     if (value != old_value and value != "") or ("0" != old_value and value == ""):
#         if value == "":
#             await bot.edit_message_text(chat_id=query.message.chat.id,
#                                         message_id=query.message.message_id,
#                                         text="0", reply_markup=keyboard)
#             old_value = "0"
#         else:
#             await bot.edit_message_text(chat_id=query.message.chat.id,
#                                         message_id=query.message.message_id,
#                                         text=value, reply_markup=keyboard)

#             old_value = value

#     if value == "Error":
#         value = ""

if __name__ == '__main__':
    executor.start_polling(dp)

