from config import REF_URL
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import WebAppInfo

class ClientKeyboard:
    async def menu_list_game():
        ikb = InlineKeyboardBuilder()
        ikb.button(text="✈AVIATOR✈",callback_data="aviator")
        ikb.button(text="⭐MINES⭐",callback_data="mines")
        ikb.button(text="🚀LUCKY JET 🚀",callback_data="lucky_jet")
        # ikb.button(text="🏴‍☠️BRAWL PIRATES 🏴‍☠️",callback_data="brawl_pirates")
        # ikb.button(text="⚽PENALTY⚽",callback_data="penalty")
        ikb.button(text="💣ROYAL MINES💣",callback_data="royal_mines")
        ikb.button(text="🆕BOMBUCKS🆕",callback_data="bombucks")

        ikb.adjust(1,1,1)

        return ikb.as_markup()

    async def menu_keyboard_aviator():
        ikb = InlineKeyboardBuilder()

        ikb.button(text="📱Registration", callback_data="register")
        ikb.button(text="📚Instruction", callback_data="aviator_instruction")
        ikb.button(text="💣Get signal💣", callback_data="get_signal_aviator")
        
        ikb.adjust(2, 1)

        return ikb.as_markup()
    
    async def menu_keyboard_lucky():
        ikb = InlineKeyboardBuilder()

        ikb.button(text="📱Registration", callback_data="register")
        ikb.button(text="📚Instruction", callback_data="luckyjet_instruction")
        ikb.button(text="💣Get signal💣", callback_data="get_signal_luckyjet")
        
        ikb.adjust(2, 1)

        return ikb.as_markup()

    async def WebAppLuckyJet(): #WebAppLuckyJet
        ikb = InlineKeyboardBuilder()

        ikb.button(text="💣Get signal💣", web_app=WebAppInfo(url="https://luckyjet-kill.vercel.app/")) #link to LuckyJet webapp

        ikb.adjust(1)
        return ikb.as_markup()

    async def menu_keyboard_royalmines():
        ikb = InlineKeyboardBuilder()

        ikb.button(text="📱Registration", callback_data="register")
        ikb.button(text="📚Instruction", callback_data="royalmines_instruction")
        ikb.button(text="💣Get signal💣", callback_data="get_signal_royalmines")
        
        ikb.adjust(2, 1)

        return ikb.as_markup()

    async def WebAppRoyalMines(): #WebAppMines
        ikb = InlineKeyboardBuilder()

        ikb.button(text="💣Get signal💣", web_app=WebAppInfo(url="https://royalmines-seves.vercel.app/")) #link to royalmines webapp

        ikb.adjust(1)
        return ikb.as_markup()
    
    async def WebAppAviatorSignal(): #WebAppAviator
        ikb = InlineKeyboardBuilder()
       
        ikb.button(text="💣Get signal💣", web_app=WebAppInfo(url="https://aviator-seves.vercel.app/")) #link to aviator webapp

        ikb.adjust(1)

        return ikb.as_markup()

    async def menu_keyboard_mines():
        ikb = InlineKeyboardBuilder()

        ikb.button(text="📱Registration", callback_data="register")
        ikb.button(text="📚Instruction", callback_data="instruction_mines")
        ikb.button(text="💣Get signal💣", callback_data="get_signal_mines")

        ikb.adjust(2,1)

        return ikb.as_markup()
    
    async def WebAppMinesSignal(): #WebAppMines
        ikb = InlineKeyboardBuilder()

        ikb.button(text="💣Get signal💣", web_app=WebAppInfo(url="https://mines-seves.vercel.app/")) #link to mines webapp

        ikb.adjust(1)
        return ikb.as_markup()

    async def menu_keyboard_bombucks():
        ikb = InlineKeyboardBuilder()

        ikb.button(text="📱Registration", callback_data="register")
        ikb.button(text="📚Instruction", callback_data="instruction_bombucks")
        ikb.button(text="💣Get signal💣", callback_data="get_signal_bombucks")

        ikb.adjust(2,1)

        return ikb.as_markup()

    async def WebAppBomBucks():
        ikb = InlineKeyboardBuilder()

        ikb.button(text="💣Get signal💣", web_app=WebAppInfo(url="https://bombucks-seves.vercel.app/")) #link to mines webapp
        
        ikb.adjust(1)
        return ikb.as_markup()

    async def register_keyboard():
        ikb = InlineKeyboardBuilder()

        ikb.button(text="📱🔸 Registration", url=REF_URL)
        ikb.button(text="🔙Back",
                   callback_data="back")

        ikb.adjust(1)

        return ikb.as_markup()

    async def back_keyboard():
        ikb = InlineKeyboardBuilder()
        ikb.button(text="🔙Back",
                   callback_data="back")

        return ikb.as_markup()

