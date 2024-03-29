from telethon import TelegramClient, events, Button
import requests
import os
from pynpm import NPMPackage
from nodejs.bindings import node_run
import requests
import cryptg
import asyncio
import shutil
import subprocess
d = os.environ.get("d")
PDISK_APIKEY= os.environ.get("PDISK_APIKEY")
client = TelegramClient('anfghohn',int(os.environ.get("APP_ID")),os.environ.get("API_HASH")).start(bot_token=os.environ.get("BOT_TOKEN"))
@client.on(events.NewMessage(pattern='(?i)/start'))
async def handler(event):
    chat = await event.get_chat()
    await client.send_message(chat, "example /upload file.mp4[filename] link will expire depends on storage weight")

@client.on(events.NewMessage(pattern='/diskusage'))
async def handler(event):
    chat = await event.get_chat()
    stat = shutil.disk_usage("/app/templates/download")
    await client.send_message(chat,str(stat))     

@client.on(events.NewMessage(pattern='/url'))
async def handler(event):
    link =event.text.split(' ')[1]
    l =event.text.split(' ')[2]
    chat = await event.get_chat()   
    s = f"http://linkapi.net/open/create_item?api_key={PDISK_APIKEY}&content_src={link}&link_type=link&title={l}"
    r = requests.get(s).json()
    z=r['data']["item_id"]
    markup  = client.build_reply_markup(Button.url("⚡ PDISK LINK ⚡",f"http://m.pdisk.net/share-video?videoid={z}"))
    await client.send_message(chat, "𝐒𝐮𝐜𝐞𝐬𝐬𝐟𝐮𝐥𝐥𝐲 𝐏𝐫𝐨𝐜𝐞𝐬𝐬𝐞𝐝 𝐘𝐨𝐮𝐫 𝐑𝐞𝐪𝐮𝐞𝐬𝐭..! \n 𝙏𝙄𝙏𝙇𝙀 : {links} \n 𝙐𝙍𝙇 : <code>http://m.pdisk.net/share-video?videoid={z}</code> \n\n 𝙎𝙏𝘼𝙏𝙐𝙎 : <code>Processing...</code> \n\n Link Will Be Active Within 5-10 Mins..! \n\n @KOT_BOTS \n @KOT_REPORS", buttons=markup)

@client.on(events.NewMessage(pattern='/telepdisk'))
async def handler(event):
    chat = await event.get_chat()
    print(chat)
    dw = await event.get_reply_message()
    links =event.text.split(" ")[1]
    await client.send_message(chat,"DOWNLOADING PLZ ...")
    ss=await dw.download_media(links)
    shutil.move(f"/app/{links}",f"/app/templates/download/{links}")
    await client.send_message(chat,f"wait few minutes ...{links}")
    link =f"{d}/files/{links}"
    #l =link.split('/')[-1]
    l =event.text.split(' ')[1]
    print(l)
    s = f"http://linkapi.net/open/create_item?api_key={PDISK_APIKEY}&content_src={link}&link_type=link&title={l}"
    r = requests.get(s).json()
    m=dict(r)
    print(m)
    f=m['data']['item_id']
    #r = requests.get(s).json()
    #print(r)
    #z=r['data']["item_id"]
   # await event.delete()
   # client.delete_messages()
    markup  = client.build_reply_markup(Button.url("⚡ PDISK LINK ⚡",f"http://m.pdisk.net/share-video?videoid={f}"))
    await client.send_message(chat, "𝐒𝐮𝐜𝐞𝐬𝐬𝐟𝐮𝐥𝐥𝐲 𝐏𝐫𝐨𝐜𝐞𝐬𝐬𝐞𝐝 𝐘𝐨𝐮𝐫 𝐑𝐞𝐪𝐮𝐞𝐬𝐭..! \n 𝙏𝙄𝙏𝙇𝙀 : {links} \n 𝙐𝙍𝙇 : <code>http://m.pdisk.net/share-video?videoid={f}</code> \n\n 𝙎𝙏𝘼𝙏𝙐𝙎 : <code>Processing...</code> \n\n Link Will Be Active Within 5-10 Mins..! \n\n @KOT_BOTS \n @KOT_REPORS ", buttons=markup)
    #os.remove(f"/app/templates/download/{links}")  

@client.on(events.NewMessage(pattern='(?i)/upload'))
async def handler(event):
    chat = await event.get_chat()
    print(chat)
    dw = await event.get_reply_message()
    links =event.text.split(" ")[1]
    await client.send_message(chat,"⚡ PDISK LINK ⚡")
    ss=await dw.download_media(links)
    shutil.move(f"/app/{links}",f"/app/templates/download/{links}")
    await client.send_message(chat,f"{d}/files/{links}")
    if os.path.exists(f"/app/Download/{chat.username}"):
        await client.send_message(chat,"downloading")
        ss=await dw.download_media()
        await client.send_message(chat,f"{d}/u?url={ss}")
    
client.start()
client.run_until_disconnected()
