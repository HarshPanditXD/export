from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    
    await message.reply_text(
        f"""**Hi 😉️!

I'ᴍ Tʜᴇ Kɪᴀʀᴀ Roʙᴏᴛ! A Pᴏᴡᴇʀғᴜʟ Bᴏᴛ ᴛᴏ Pʟᴀʏ Mᴜsɪᴄ ɪɴ Yᴏᴜʀ Gʀᴏᴜᴘ Vᴏɪᴄᴇ Cʜᴀᴛ 😇! 

Aʟsᴏ I ʜᴀᴠᴇ ᴍᴏʀᴇ ғᴇᴀᴛᴜʀᴇs! Pʟᴇᴀsᴇ ʜɪᴛ ᴏɴ  ᴛᴏ sᴇᴇ ᴛʜᴇᴍ 😘!...

Dᴇᴠᴇʟᴏᴘᴇʀ Bʏ : [Lᴏɢ Oᴜᴛ XD](https://t.me/Log_out_xd**
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "✨Aᴅᴅ Mᴇ Tᴏ Yᴏᴜʀ Gʀᴏᴜᴘ✨", url="https://t.me/Kiara_ro_bot?startgroup=true")
                  ],[
                    InlineKeyboardButton(
                        "🌷Sᴜᴘᴘᴏʀᴛ Gʀᴏᴜᴘ🥀", url="https://t.me/The_SECRET_worlds"
                    ),
                    InlineKeyboardButton(
                        "Sᴜᴘᴘᴏʀᴛ Cʜᴀɴɴᴇʟ", url="https://t.me/The_Blaze_Network"
                    )
                ],[ 
                    InlineKeyboardButton(
                        "Hᴇʟᴘ & Cᴏᴍᴍᴀɴᴅs", url="https://telegra.ph/BLAZE-MUSIC-BOT-12-09"
                    )]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("hexor") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**𝗕𝗼𝘁 𝗢𝗻𝗹𝗶𝗻𝗲..😎**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "𝗦𝘂𝗽𝗽𝗼𝗿𝘁", url="https://t.me/kiara_support")
                ]
            ]
        )
   )
