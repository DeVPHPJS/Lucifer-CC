"""
≛ <b>Commands Available ✅</b> ≛

──────────────────────
<code>/scr</code> <Username> <Amount>  - Scrape CC ❇️
──────────────────────

© 2023 | <a href="https://t.me/DEVPHPJS">⏤͟͞𝐋𝐮𝐂𝐢𝐅𝐞𝐑 ☬ 🇪🇬</a>
"""


import os
from pathlib import Path
import re
import time
import requests

from telethon import Button
import telethon

from mills import uclient
from mills.decorators import bot_cmd
from telethon.utils import *
from telethon.tl.functions.messages import ImportChatInviteRequest

from mills.plugins.checkers.utils.tools import getcards

ccs = []





@bot_cmd(cmd="scr", text_only = True)
async def _(m):
    inp = m.pattern_match.group(1).strip()
    if len(inp) < 1:
        return await m.reply("ヤ 𝘞𝘙𝘰𝘯𝘎 𝘜𝘴𝘦 ⚠️️\nヤ 𝘕𝘰𝘳𝘔𝘢𝘭 𝘚𝘤𝘙𝘢𝘗𝘦𝘳 : /scr LuciferSCR 100")
    channel , amount_str = inp.split()
    if not (channel, amount_str):
        return await m.reply("ヤ 𝘞𝘙𝘰𝘯𝘎 𝘜𝘴𝘦 ⚠️️\nヤ 𝘕𝘰𝘳𝘔𝘢𝘭 𝘚𝘤𝘙𝘢𝘗𝘦𝘳 : /scr LuciferSCR 100")
    if 'joinchat' in channel:
        resolve = resolve_invite_link(channel)
        if all(ele is None for ele in resolve):
            return await m.reply("Link Not Work ❌.")
        else:
            chat_hash = re.findall('joinchat/(.*\w)', channel)
            if not chat_hash:
                return await m.reply("Invalid link.")
            try:
                chat_invite = await uclient(ImportChatInviteRequest(chat_hash[0]))
            except telethon.errors.rpcerrorlist.UserAlreadyParticipantError:
                pass
            except:
                return await m.reply("Invalid link.")
                
    try:
        amount = int(amount_str)
    except:
        return await m.sod("Amount must be number and < 10000.\nFormat: .scrape roldexversechats 50", time = 10)
    if  amount > 10000 or amount < 1:
        return await m.sod("Amount must be number and < 10000.\nFormat: .scrape roldexversechats 50", time = 10)
    try:
        ent = await uclient.get_entity(channel)
        if not ent:
            return await m.sod("Invalid Username or id.", time = 10)
    except: 
        return await m.sod("Invalid Username or id.", time = 10)
    entType  = ent.stringify().split('(')[0]
    if entType == 'User':  
        return await m.sod("Can't use Private chats.", time = 10)
    all_cards = []
    # all_mess = await  uclient.get_messages(ent, limit = amount)
    async for event in uclient.iter_messages(channel, limit = amount, wait_time = 5 if amount > 1000 else 2):
        if not event.text:
            continue
        cards = getcards(event.text)    
        if cards and cards[0] not in all_cards:
            cc,mes,ano,cvv = cards
            if len(mes) == 1: mes = '0' + str(mes)
            if len(ano) == 2: ano = '20' + str(ano)
            # print(f'{cc}|{mes}|{ano}|{cvv}')
            all_cards.append([cc,mes,ano,cvv])
    
    for cards in all_cards:
        cc,mes,ano,cvv = cards
        with open(f'{len(all_cards)}x{ent.username if ent.username else ""}.txt', 'a') as w:
            w.write(f'{cc}|{mes}|{ano}|{cvv}' + '\n')
    
    if len(all_cards) > 1:
        mess = f"""
✅ [ ֆ - Successful! ]

<b>[ֆ] Source</b> -» <code>{ent.username}</code>
<b>[ֆ] Type</b> -» <code>{entType}</code>
<b>[ֆ] Amount</b> -» <code>{amount}</code> cards
<b>[>] Skipped</b> -» <code>{amount - len(all_cards)}</code> cards
<b>[ֆ] CC Found</b> -» <code>{len(all_cards)}</code> cards

<b>[🏴‍☠️] Scrapped By</b> -» <a href= "tg://user?id={m.sender.id}">{m.sender.first_name}</a>
<b>[⚡️] Host</b> -» <a href="https://t.me/DEVPHPJS">⏤͟͞𝐋𝖚𝐂𝖎𝐅𝖊𝐑 ֆ 🇪🇬</a>
"""
        is_true = await m.sod(mess , file = f'{len(all_cards)}x{ent.username if ent.username else ""}.txt')
        if is_true:
            name = f'{len(all_cards)}x{ent.username if ent.username else ""}.txt'
            my_file = Path(name)
            my_file.unlink(missing_ok=True)
    else:
        return await m.sod("No Cards Found.", time = 10)