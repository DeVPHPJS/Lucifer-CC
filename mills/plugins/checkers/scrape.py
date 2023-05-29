"""
≛ <b>Commands Available ✅</b> ≛

──────────────────────
<code>/scr</code> <Username> <Amount>  - Scrape CC ❇️
──────────────────────

© 2023 | <a href="https://t.me/DEVPHPJS">⏤͟͞𝐋𝐮𝐂𝐢𝐅𝐞𝐑 ☬ 🇪🇬</a>
"""


import os, requests
from telethon.tl.functions.messages import ImportChatInviteRequest
from telethon.utils import *
from telethon.sessions import StringSession
from handlers.user.jocastaclient import JocastaClient

from telethon import Button
from pathlib import Path

from bs4 import BeautifulSoup as bsoup

from main import dp


PREFIX = "!/."
import re






def getcards(text: str):
  text = text.replace('\n', ' ').replace('\r', '')
  card = re.findall(r"[0-9]+", text)
  if not card or len(card) < 3:
    return
  if len(card) == 3:
    cc = card[0]
    if len(card[1]) == 3:
      mes = card[2][:2]
      ano = card[2][2:]
      cvv = card[1]
    else:
      mes = card[1][:2]
      ano = card[1][2:]
      cvv = card[2]
  else:
    cc = card[0]
    if len(card[1]) == 3:
      mes = card[2]
      ano = card[3]
      cvv = card[1]
    else:
      mes = card[1]
      ano = card[2]
      cvv = card[3]
    if len(mes) == 2 and (mes > '12' or mes < '01'):
      ano1 = mes
      mes = ano
      ano = ano1
  if cc[0] == 3 and len(cc) != 15 or len(cc) != 16 or int(
      cc[0]) not in [3, 4, 5, 6]:
    return
  if len(mes) not in [
      2, 4
  ] or len(mes) == 2 and mes > '12' or len(mes) == 2 and mes < '01':
    return
  if len(ano) not in [
      2, 4
  ] or len(ano) == 2 and ano < '21' or len(ano) == 4 and ano < '2021' or len(
      ano) == 2 and ano > '29' or len(ano) == 4 and ano > '2029':
    return
  if cc[0] == 3 and len(cvv) != 4 or len(cvv) != 3:
    return
  if (cc, mes, ano, cvv):
    return cc, mes, ano, cvv


APP_ID = "20497298"
API_HASH = "fd14967582d94a2d6237c2c024d4ec10"
SESSION = "1AZWarzQBu30fdAd7LNOqrflKl6zHlN6SHLo438OEs4Ed40hlDLdrdooeCkDC-szsSrLpJaSbxp06ILQJww-7C4qCl4H7uhHtfrX8peZK3_mpqKkMyz4FFYatz01zTogN3fLJyL1gF1SRyd_xG-nSl8AMuX_JMtGTERyUbPXjJZ8jExob7u-4XmtJbB7MEmKLXUL9nWb8Dab0j_j-O194OnXhsT6iUZPYdAKyhSuje-dZi8h3W3SluuhenSqxaomZvR-9LgEBvPT5M8C9pD9UnY8IzflVLq1OAOFtFGlEKDCyL7hTIQefDMJR5_z0DzhKGP42nkc3KP1GPssvLgBdrhXPHM9xjrE="

uclient = JocastaClient(
  StringSession(SESSION),
  (APP_ID),
  (API_HASH),
)

ccs = []


@dp.message_handler(commands=["scr"], commands_prefix=PREFIX)
async def kk(message: types.Message):
  gf = await message.reply("<code>Scrapping...</code>")
  inp = message.text[len('/scr '):]

  if len(inp) < 1:
    return await gf.edit_text(
      "Incorrect data.\n Format: .scrape team_sharif 50")
  try:
    channel, amount_str = inp.split()
  except:
    return await gf.edit_text(
      "Incorrect data.\n Format: .scrape team_sharif 50")

  try:
    amount = int(amount_str)
  except:
    return await gf.edit_text("invalid amount \nFormat: .scrape team_sharif 50"
                              )
  if amount > 5000 or amount < 1:
    return await gf.edit_text(
      "Amount must be number and under 2000.\nFormat: .scrape team_sharif 50")
  if 'joinchat' in channel:
    resolve = resolve_invite_link(channel)
    if all(ele is None for ele in resolve):
      return await gf.edit_text("Invalid link.")
    else:
      chat_hash = re.findall('joinchat/(.*\w)', channel)
      if not chat_hash:
        return await gf.edit_text("Invalid link.")
      try:
        chat_invite = await uclient(ImportChatInviteRequest(chat_hash[0]))

      except:
        return await gf.edit_text("Invalid link.")

  try:
    ent = await uclient.get_entity(channel)
    if not ent:
      return await gf.edit_text("Invalid Username or id.")
  except:
    return await gf.edit_text("Invalid Username or id.")
  entType = ent.stringify().split('(')[0]
  if entType == 'User':
    return await gf.edit_text("Can't use Private chats.")
  all_cards = []
  # all_mess = await  uclient.get_messages(ent, limit = amount)
  async for event in uclient.iter_messages(
    channel, limit=amount, wait_time=0 if amount > 10000 else 2):
    if not event.text:
      continue
    cards = getcards(event.text)
    if cards and cards[0] not in all_cards:
      cc, mes, ano, cvv = cards
      if len(mes) == 1:
        mes = '0' + str(mes)
      if len(ano) == 2:
        ano = '20' + str(ano)
      # print(f'{cc}|{mes}|{ano}|{cvv}')
      all_cards.append([cc, mes, ano, cvv])

  for cards in all_cards:
    cc, mes, ano, cvv = cards
    kog = f'{len(all_cards)}_@team_sharif.txt'
    with open(kog, 'a') as w:
      w.write(f'{cc}|{mes}|{ano}|{cvv}' + '\n')

  if len(all_cards) > 1:
    mess = f"""
<b>[ success ] Scrapped! ✅ </b>
<b>Amount -» </b>{amount}
<b>Found -» </b>{len(all_cards)}
<b>Bin -» </b>NONE
<b>Target -» </b>{channel}
<b>Scrapped by -» </b><a href="tg://user?id={message.from_user.id}">{message.from_user.first_name}</a>
<b>Bot by -» </b><a href="tg://user?id=5234223466"><b>srfxdz</b></a>🦋
"""
    md = open(kog, "rb")
    await gf.delete()
    is_true = await message.reply_document(document=md, caption=mess)
    os.remove(kog)
    if is_true:
      name = f'{len(all_cards)}x{ent.username if ent.username else ""}.txt'
      my_file = Path(name)
      my_file.unlink(missing_ok=True)

  else:
    return await gf.edit_text("No Cards Found.")



