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
                
@app.on_message(filters.command(["السورس","ياسورس","يا سورس","سورس"],""))
async def huhh(client: Client, message: Message):
        caption=f"""◉ 𝙽𝙰𝙼𝙴 : ❪[Sᴏᴜʀᴄᴇ ғʀ𝟹ᴏɴ](https://t.me/LinkXFrend)❫
◉ 𝚄𝚂𝙴𝚁 : ❪ @PV_FR3ON ❫
◉ 𝙸𝙳      : ❪ 5490392130 ❫
◉ 𝙱𝙸𝙾    : ❪ صلي علي الحبيب محمد ✨♥ ❫""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "᳒ᴅᴇᴠ ҒᎡ3ΌΝ", url=f"https://t.me/IZ3Zp"), 
                 ],[
                   InlineKeyboardButton(
                        "☭ ՏΌႮᎡᏟᎬ  ҒᎡ3ΌΝ ☭", url=f"https://t.me/LinkXFrend"),
                ],

            ]

        ),

    )
