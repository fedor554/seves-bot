from aiogram.filters import CommandStart, Command
from aiogram.types import Message,CallbackQuery,InputMediaPhoto
from aiogram import F, Router, types
from app.keyboards import ClientKeyboard
import app.keyboards as kb
from database.db import DataBase
from aiogram import types


router = Router()

@router.message(CommandStart())
async def cmd_start(message: Message):
    user = await DataBase.get_user(message.from_user.id)
    
    if user is None:
        await DataBase.register(message.from_user.id, verifed="0")
        print(f"Новый пользователь:\nID: {message.from_user.id}\nCOUNTRY: {message.from_user.language_code}\n")
    photo = types.FSInputFile("C:/Users/gring/Desktop/Project SEVES/img/choice_game.jpg")
    await message.answer_photo(photo=photo, caption="Choose a game:",reply_markup=await ClientKeyboard.menu_list_game())

# @router.message(F.photo)
# async def getId_photo(message: Message):
#     await message.answer(f"ID photo: {message.photo[-1].file_id}")

# @router.message(F.video)
# async def getID_video(message: Message):
#     await message.answer(f"ID video: {message.video.file_id}")
