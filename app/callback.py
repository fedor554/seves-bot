from aiogram.types import CallbackQuery,InputMediaPhoto, Message
from aiogram import types
import asyncio
import os
import datetime
from random import choice, uniform, randint
from aiogram import F, Router, Bot
from aiogram.fsm.state import StatesGroup,State
from aiogram.fsm.context import FSMContext
import app.keyboards as kb
import app.text as txt
from database.db import DataBase
from app.keyboards import ClientKeyboard
from other.filters import RegisteredFilter

router1 = Router()

class RegisterState(StatesGroup):
   input_id = State()

class GetSignalStates(StatesGroup):
   chosing_mines = State()

@router1.callback_query(F.data == "aviator")
async def select_aviator(callback: CallbackQuery):
   photo = types.FSInputFile("C:/Users/gring/Desktop/Project SEVES/img/aviator_preview.png")
   file = InputMediaPhoto(media=photo,caption=txt.aviator_txt,parse_mode="html")
   await callback.message.edit_media(file,reply_markup=await ClientKeyboard.menu_keyboard_aviator())

@router1.callback_query(F.data=="register")
async def registers_aviator(callback:CallbackQuery, state: FSMContext):
   photo = types.FSInputFile("C:/Users/gring/Desktop/Project SEVES/img/registration_preview.jpg")
   file = InputMediaPhoto(media=photo, caption=txt.forma_registers,parse_mode="html")
   await callback.message.edit_media(file, reply_markup=await ClientKeyboard.register_keyboard())
   await state.set_state(RegisterState.input_id)

@router1.callback_query(F.data=="lucky_jet")
async def select_lucky(callback: CallbackQuery):
   photo = types.FSInputFile("C:/Users/gring/Desktop/Project SEVES/img/luckyjet_preview.jpg")
   file = InputMediaPhoto(media=photo,caption=txt.luckyjet_txt,parse_mode="html")
   await callback.message.edit_media(file,reply_markup=await ClientKeyboard.menu_keyboard_lucky())

@router1.callback_query(F.data=="luckyjet_instruction")
async def instruction_luckyjet(callback: CallbackQuery):
   photo = types.FSInputFile("C:/Users/gring/Desktop/Project SEVES/img/luckyjet_preview.jpg")
   file = InputMediaPhoto(media=photo,caption=txt.luckyjet_instruction,parse_mode="html")
   await callback.message.edit_media(file,reply_markup=await ClientKeyboard.menu_keyboard_lucky())

@router1.callback_query(F.data=="get_signal_luckyjet", RegisteredFilter())
async def game_signal(callback: CallbackQuery, state: FSMContext, bot: Bot):
   photo = types.FSInputFile("C:/Users/gring/Desktop/Project SEVES/img/luckyjet_preview.jpg")
   try:
      await callback.message.delete()
   except:
      pass
   await callback.message.answer_photo(photo=photo, reply_markup=await ClientKeyboard.WebAppLuckyJet())

@router1.callback_query(F.data=="royal_mines")
async def select_royalmines(callback: CallbackQuery):
   photo = types.FSInputFile("C:/Users/gring/Desktop/Project SEVES/img/royalmines_preview.jpg")
   file = InputMediaPhoto(media=photo,caption=txt.royalmines_txt,parse_mode="html")
   await callback.message.edit_media(file, reply_markup=await ClientKeyboard.menu_keyboard_royalmines())

@router1.callback_query(F.data == "royalmines_instruction")
async def instruction__royalmines(callback: CallbackQuery):
   photo = types.FSInputFile("C:/Users/gring/Desktop/Project SEVES/img/royalmines_preview.jpg")
   file = InputMediaPhoto(media=photo,caption=txt.royalmines_instruction,parse_mode="html")
   await callback.message.edit_media(file, reply_markup=await ClientKeyboard.menu_keyboard_royalmines())

@router1.callback_query(F.data=="register")
async def registers_royalmines(callback:CallbackQuery, state: FSMContext):
   photo = types.FSInputFile("C:/Users/gring/Desktop/Project SEVES/img/registration_preview.jpg")
   file = InputMediaPhoto(media=photo, caption=txt.forma_registers,parse_mode="html")
   await callback.message.edit_media(file, reply_markup=await ClientKeyboard.register_keyboard())
   await state.set_state(RegisterState.input_id)

@router1.callback_query(F.data=="get_signal_royalmines", RegisteredFilter())
async def game_signal(callback: CallbackQuery, state: FSMContext, bot: Bot):
   photo = types.FSInputFile("C:/Users/gring/Desktop/Project SEVES/img/royalmines_preview.jpg")
   try:
      await callback.message.delete()
   except:
      pass
   await callback.message.answer_photo(photo=photo, reply_markup=await ClientKeyboard.WebAppRoyalMines())

@router1.callback_query(F.data=="register")
async def registers_luckyjet(callback:CallbackQuery, state: FSMContext):
   photo = types.FSInputFile("C:/Users/gring/Desktop/Project SEVES/img/registration_preview.jpg")
   file = InputMediaPhoto(media=photo, caption=txt.forma_registers,parse_mode="html")
   await callback.message.edit_media(file, reply_markup=await ClientKeyboard.register_keyboard())
   await state.set_state(RegisterState.input_id)

@router1.callback_query(F.data == "mines")
async def select_mines(callback: CallbackQuery):
   photo = types.FSInputFile("C:/Users/gring/Desktop/Project SEVES/img/mines_preview.jpg")
   file = InputMediaPhoto(media=photo,caption=txt.mines_txt,parse_mode="html")
   await callback.message.edit_media(file,reply_markup=await ClientKeyboard.menu_keyboard_mines())

@router1.callback_query(F.data == "instruction_mines")
async def select_mines(callback: CallbackQuery):
   photo = types.FSInputFile("C:/Users/gring/Desktop/Project SEVES/img/mines_preview.jpg")
   file = InputMediaPhoto(media=photo,caption=txt.mines_instructions,parse_mode="html")
   await callback.message.edit_media(file,reply_markup=await ClientKeyboard.menu_keyboard_mines())

@router1.callback_query(F.data=="get_signal_mines", RegisteredFilter())
async def game_signal(callback: CallbackQuery, state: FSMContext, bot: Bot):
   photo = types.FSInputFile("C:/Users/gring/Desktop/Project SEVES/img/mines_preview.jpg")
   try:
      await callback.message.delete()
   except:
      pass
   await callback.message.answer_photo(photo=photo, reply_markup=await ClientKeyboard.WebAppMinesSignal())

@router1.callback_query(F.data=="register")
async def registers_mines(callback:CallbackQuery, state: FSMContext):
   photo = types.FSInputFile("C:/Users/gring/Desktop/Project SEVES/img/registration_preview.jpg")
   file = InputMediaPhoto(media=photo, caption=txt.forma_registers,parse_mode="html")
   await callback.message.edit_media(file, reply_markup=await ClientKeyboard.register_keyboard())
   await state.set_state(RegisterState.input_id)

@router1.callback_query(F.data == "bombucks")
async def select_bombucks(callback: CallbackQuery):
   photo = types.FSInputFile("C:/Users/gring/Desktop/Project SEVES/img/bombucks_preview.jpg")
   file = InputMediaPhoto(media=photo,caption=txt.bombucks_txt,parse_mode="html")
   await callback.message.edit_media(file,reply_markup=await ClientKeyboard.menu_keyboard_bombucks())

@router1.callback_query(F.data == "instruction_bombucks")
async def select_bombucks(callback: CallbackQuery):
   photo = types.FSInputFile("C:/Users/gring/Desktop/Project SEVES/img/bombucks_preview.jpg")
   file = InputMediaPhoto(media=photo,caption=txt.bombucks_instructions,parse_mode="html")
   await callback.message.edit_media(file,reply_markup=await ClientKeyboard.menu_keyboard_bombucks())

@router1.callback_query(F.data=="get_signal_bombucks", RegisteredFilter())
async def game_signal(callback: CallbackQuery, state: FSMContext, bot: Bot):
   photo = types.FSInputFile("C:/Users/gring/Desktop/Project SEVES/img/bombucks_preview.jpg")
   try:
      await callback.message.delete()
   except:
      pass
   await callback.message.answer_photo(photo=photo, reply_markup=await ClientKeyboard.WebAppBomBucks())

@router1.callback_query(F.data=="register")
async def registers_bombucks(callback:CallbackQuery, state: FSMContext):
   photo = types.FSInputFile("C:/Users/gring/Desktop/Project SEVES/img/registration_preview.jpg")
   file = InputMediaPhoto(media=photo, caption=txt.forma_registers,parse_mode="html")
   await callback.message.edit_media(file, reply_markup=await ClientKeyboard.register_keyboard())
   await state.set_state(RegisterState.input_id)

@router1.message(RegisterState.input_id)
async def register_handler_finaly(message: Message, state: FSMContext):
   try:
        number = int(message.text)

        if len(message.text) >= 8:
            await DataBase.update_verifed(message.from_user.id)
            await message.answer("<b>You have successfully registered✅</b>",parse_mode="html")
            await state.clear()
            photo = types.FSInputFile("C:/Users/gring/Desktop/Project SEVES/img/choice_game.jpg")
            await message.answer_photo(photo=photo, caption="Choose a game:",reply_markup=await ClientKeyboard.menu_list_game())
        else:
            print(message.text)
            await message.answer("<b>Invalid ID❌</b>",parse_mode="html")
            return

   except Exception as e:
      print(e)
      print(message.text)
      await message.answer("<b>Invalid ID❌</b>",parse_mode="html")
      return

@router1.callback_query(F.data=="aviator_instruction")
async def aviator_instruction(callback: CallbackQuery):
   photo = types.FSInputFile("C:/Users/gring/Desktop/Project SEVES/img/aviator_preview.png")
   file = InputMediaPhoto(media=photo, caption=txt.aviator_instruction,parse_mode="html")
   await callback.message.edit_media(file, reply_markup=await ClientKeyboard.menu_keyboard_aviator())

@router1.callback_query(F.data=="get_signal_aviator", RegisteredFilter())
async def game_signal(callback: CallbackQuery, state: FSMContext, bot: Bot):
   photo = types.FSInputFile("C:/Users/gring/Desktop/Project SEVES/img/Aviator_WebApp_Signal.jpg")
   try:
      await callback.message.delete()
   except:
      pass
   await callback.message.answer_photo(photo=photo, reply_markup=await ClientKeyboard.WebAppAviatorSignal())

# Этот хендлер сработает если пользователь не зарегестрирован
@router1.callback_query(F.data == "get_signal_mines")
async def get_signal_start_handler(callback: types.CallbackQuery, state: FSMContext):
   await registers_mines(callback, state)

@router1.callback_query(F.data == "get_signal_aviator")
async def get_signal_start_handler(callback: types.CallbackQuery, state: FSMContext):
   await registers_aviator(callback, state)

@router1.callback_query(F.data == "get_signal_bombucks")
async def get_signal_start_handler(callback: types.CallbackQuery, state: FSMContext):
   await registers_bombucks(callback, state)

@router1.callback_query(F.data == "get_signal_luckyjet")
async def get_signal_start_handler(callback: types.CallbackQuery, state: FSMContext):
   await registers_luckyjet(callback, state)

@router1.callback_query(F.data=="get_signal_royalmines")
async def get_signal_start_handler(callback: types.CallbackQuery, state: FSMContext):
   await registers_royalmines(callback, state)




@router1.callback_query(F.data=="back")
async def main_menu(callback: CallbackQuery):
   photo = types.FSInputFile("C:/Users/gring/Desktop/Project SEVES/img/choice_game.jpg")
   file = InputMediaPhoto(media=photo, caption="Choose a game:")
   await callback.message.edit_media(file,reply_markup=await ClientKeyboard.menu_list_game())