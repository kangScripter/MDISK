import os
from pyrogram import Client, filters,enums
import time
from pyrogram.errors import FloodWait, UserNotParticipant, MessageNotModified
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message, CallbackQuery, InputMediaPhoto
from helpers.display_progress import progress_for_pyrogram

MDISK = Client(
    name= 'Mdisk',
    api_id=5540967,
    api_hash='eedf0196b0533f361b51b5b7082358e9',
    bot_token='1860781460:AAHOUPAWKur2BzMRfmLU1wIBedlm6GGGL8g'
)

@MDISK.on_message(filters.private & filters.command("start"))
async def start(bot: MDISK,m: Message):
      await m.reply_text(
        text='Hello This is Mdisk Bot',
        disable_web_page_preview=True,
        quote=True,
        )

@MDISK.on_message(filters.private & (filters.document | filters.video))   
async def video(bot: MDISK,m: Message):
    media = m.video or m.document
    if media.file_name is None:
        await m.reply_text("File Name Not Found!")
        return
    if media.file_name.rsplit(".", 1)[-1].lower() not in ["mp4", "mkv", "webm"]:
        await m.reply_text("This Video Format not Supported!\nOnly send MP4 or MKV or WEBM.", quote=True)
        return  
    else:
       file_dl_path = None
       try:
                c_time = time.time()
                file_dl_path = await bot.download_media(
                    message=media,
                    file_name=f"mdisk_vudeo.mkv",
                    progress=progress_for_pyrogram,
 
                )
       except Exception as downloadErr:
                print(f"Failed to Download File!\nError")
               
                await m.edit_text("File Skipped!")
                await asyncio.sleep(3)
                
MDISK.run()
