"""
≛ <b>Commands Available ✅</b> ≛

──────────────────────────
- <code>/buy<code>: Check Available plans for unlocking paid checker gates.
──────────────────────────

© 2023 | <a href="https://t.me/DEVPHPJS">⏤͟͞𝐋𝐮𝐂𝐢𝐅𝐞𝐑 ☬ 🇪🇬</a>
"""
import inspect
import io
import json
import os
import time
from fuzzywuzzy.process import extractOne
from telethon import utils
# from telethon import Button
from telethon.tl.custom import Button

from mills import BOT_PIC, client
from mills.decorators import bot_cmd


@bot_cmd(pattern="buy$")
async def _(m):
    text = f"""

┌──────────────────────────┐
    • Premium Plans •

◦ 5$ - Get access to all gates for 5 days.
◦ 10$ - Get access to all gates. for 10 days
◦ 20$ - Get access to all gates. for 20 days

○ Payment Methods : Crypto Only 📛.

└──────────────────────────┘
"""
    buttons = [
        Button.url('Buy Now', 'https://t.me/DEVPHPJS'),
        Button.url('Test Keys', 'https://t.me/XIX_V1'),
    ]
    await m.reply(text,buttons= buttons, file = BOT_PIC)