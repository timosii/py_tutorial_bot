from aiogram import Bot, Dispatcher
from aiogram.filters import Command, CommandStart
from aiogram.types import Message
from aiogram import F
from config import settings
import random


BOT_TOKEN = settings.BOT_TOKEN
WHO_SEND_ID = settings.WHO_SEND_ID

bot = Bot(BOT_TOKEN)
dp = Dispatcher()

PHRASES = ["Получил, круто!", "Интересная идея!", "А что, так можно было? Круто, передам хозяину!", "Это действительно может быть интересно!", "Добавлю в руководство!"]


@dp.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer("Привет! Ты можешь прислать задачи и примеры для моего руководства по Python! Также я очень рад любым замечаниям и предложениям!")

@dp.message(Command(commands="help"))
async def process_help_command(message: Message):
    await message.answer("Присылай ошибку, комментарий, задачу или пример в форматах: текст, фото, документ и я добавлю это в руководство")

@dp.message(F.content_type.in_({'photo', 'document'}))
async def process_save_files(message: Message):
    form_message = f"Username: {message.from_user.username}\nid: {message.from_user.id}\nБот: {'Да' if message.from_user.is_bot else 'Нет'}\nИмя: {message.from_user.first_name}\nФамилия: {message.from_user.last_name}"
    message_to_forward_id = message.message_id
    await bot.send_message(WHO_SEND_ID, f"Инфо об отправителе:\n{form_message}\n\n{message.text}")
    await bot.forward_message(WHO_SEND_ID, message.chat.id, message_to_forward_id)

    if message.photo:
        await message.answer(text=f"Сохранил фото, обязательно передам! Спасибо!")
        
    else:
        await message.answer("Сохранил документ, обязательно передам! Спасибо!")

@dp.message()
async def process_send_text(message: Message):
    form_message = f"Username: {message.from_user.username}\nid: {message.from_user.id}\nБот: {'Да' if message.from_user.is_bot else 'Нет'}\nИмя: {message.from_user.first_name}\nФамилия: {message.from_user.last_name}"

    await bot.send_message(WHO_SEND_ID, f"Инфо об отправителе:\n{form_message}\n\n{message.text}")
    await message.answer(f"{random.choice(PHRASES)} Спасибо за участие в проекте!")

    
if __name__ == '__main__':
    dp.run_polling(bot)
