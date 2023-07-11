from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton

bot = Bot(token="6223148132:AAECLT5qjVj2LsB-zl7gHJuOAazFVzNiF3A")
sj = Dispatcher(bot)

button1 = KeyboardButton("Video Courses 📹")
button2 = KeyboardButton("Books 📚")
button3 = KeyboardButton("Contact  ☎️")
keyboard1 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(button1).add(button2).add(button3)

@sj.message_handler(commands=["start", "help"])
async def welcome(message: types.Message):
    await message.reply("Ooo! Hello new User! \nWelcome our BOT \nYou can use this BOT for only study purpose!", reply_markup=keyboard1)

@sj.message_handler()
async def kb_aswer(message: types.Message):
    if message.text == "Video Courses 📹":
        await message.answer("IELTS materials 👇🏻\n"
                            "@freeieltscourse1\n\n"

                            "SAT materials 👇🏻\n"
                            "@freesatcourse\n\n"

                            "IT materials 👇🏻\n"
                            "@IT_journey_1\n\n"

                            "MAIN channel 👉🏻  @Successfull_journey\n\n"

                            "new features {SOON}")
    elif message.text == "Books 📚":
        await message.answer("MAIN channel 👉🏻  @Successfull_journey\n\n"

                            "new features {SOON}")
    elif message.text == "Contact  ☎️":
        await message.answer("You can contact ☎️ with me in this way: "
                            "Open this channel's comment and wrote to me something you interested -> \n@Successfull_journey ")
    else:
        await message.answer(f"your message is {message.text}")

executor.start_polling(sj)