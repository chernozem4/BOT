import os
import random
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import FSInputFile
from dotenv import load_dotenv
import asyncio

load_dotenv()
API_TOKEN = os.getenv('TOKEN')

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

unique_users = set()


@dp.message(Command("start"))
async def send_welcome(message: types.Message):
    user_id = message.from_user.id
    user_first_name = message.from_user.first_name


    if user_id not in unique_users:
        unique_users.add(user_id)

    unique_user_count = len(unique_users)

    await message.reply(f'Привет, {user_first_name}, наш бот обслуживает уже {unique_user_count} пользователя(ей).')


@dp.message(Command("myinfo"))
async def send_myinfo(message: types.Message):
    user_id = message.from_user.id
    user_first_name = message.from_user.first_name
    user_username = message.from_user.username

    info_message = (
        f"Ваш id: {user_id}\n"
        f"Ваше имя: {user_first_name}\n"
        f"Ваш username: {user_username}"
    )

    await message.reply(info_message)


@dp.message(Command("random"))
async def send_random_image(message: types.Message):
    images_path = 'images'
    images = [os.path.join(images_path, file) for file in os.listdir(images_path) if
              file.endswith(('jpg', 'jpeg', 'png', 'gif'))]

    random_image_path = random.choice(images)
    random_image = FSInputFile(random_image_path)

    await message.reply_photo(random_image)


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
