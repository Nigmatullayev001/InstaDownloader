from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text
from keyboard import video_downloader

BOT_TOKEN = "6756093184:AAGrwaDg2_V7qp9-tQQARAwslFfYCOQ0_Q8"
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot=bot)


@dp.message_handler(commands="start")
async def start_bot(message: types.Message):
    await message.answer("Botga xush kelibsiz")


@dp.message_handler(Text(startswith="https://www.instagram.com/"))
async def start_bot(message: types.Message):
    await message.answer("1 daqiqa kutib turing")

# @dp.message_handler(Text(startswith="https://www.instagram.com/"))
# async def start_bot(message: types.Message):
#     result = video_downloader(message.text)
#     await message.answer_photo(photo=result['media'])


@dp.message_handler(Text(startswith="https://www.instagram.com/"))
async def s_bot(message: types.Message):
    result = video_downloader(message.text)
    if result['type'] == "image":
        await message.answer_photo(photo=result['media'])
    elif result['type'] == "video":
        await message.answer_video(video=result['media'])
    elif result['type'] == "carousel":
        for result_m in result['media']:
            await message.answer_photo(photo=result_m['media'])


if __name__ == '__main__':
    executor.start_polling(dp)
