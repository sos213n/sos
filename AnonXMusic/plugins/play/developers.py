import asyncio

import os
import time
import requests
from config import START_IMG_URL
from pyrogram import filters
import random
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from strings.filters import command
from AnonXMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from AnonXMusic import app
from random import  choice, randint

#          
                
@app.on_message(filters.command(["فرعون","المبرمج فرعون","مبرمج السورس","مبرمج"],"")
)
async def huhh(client: Client, message: Message):
    await message.reply_photo(
        caption=f"""◉ 𝙽𝙰𝙼𝙴 : ❪[sos](https://t.me/IZ3Zp)❫
◉ 𝚄𝚂𝙴𝚁 : ❪ @PV_FR3ON ❫
◉ 𝙸𝙳      : ❪ 5490392130 ❫
◉ 𝙱𝙸𝙾    : ❪ صلي علي الحبيب محمد ✨♥ ❫""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "᳒ᴅᴇᴠ ҒᎡ3ΌΝ", url=f"https://t.me/LinkXFrend"), 
                 ],[
                   InlineKeyboardButton(
                        "☭ ՏΌႮᎡᏟᎬ  ҒᎡ3ΌΝ ☭", url=f"https://t.me/LinkXFrend"),
                ],

            ]

        ),

    )
