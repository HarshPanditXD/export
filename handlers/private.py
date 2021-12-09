
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    
    await message.reply_text(
        f"""**Hi  ,I'ᴍ Tʜᴇ Kiara  RoBᴏᴛ! A Pᴏᴡᴇʀғᴜʟ Bᴏᴛ ᴛᴏ Pʟᴀʏ Mᴜsɪᴄ ɪɴ Yᴏᴜʀ Gʀᴏᴜᴘ Vᴏɪᴄᴇ Cʜᴀᴛ 😇! 

Aʟsᴏ I ʜᴀᴠᴇ ᴍᴏʀᴇ ғᴇᴀᴛᴜʀᴇs! Pʟᴇᴀsᴇ ʜɪᴛ ᴏɴ  ᴛᴏ sᴇᴇ ᴛʜᴇᴍ 😘!...
𝗣𝗼𝘄𝗲𝗿𝗲𝗱 𝗕𝘆 : [𓆩𓆩𝐋𝐎𝐆 𝐎𝐔𝐓 𝘅𝗗𓆪𓆪](https://t.me/log_out_xd)/[༆ᎬꪜᎥᏝꦿ★乂B🅾️y♠️](https://t.me/Evil_boy_xd)**
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text="✨Aᴅᴅ Mᴇ Tᴏ Yᴏᴜʀ Gʀᴏᴜᴘ✨", url="http://t.me/Kiara_ro_bot?startgroup=true")
                ],
                [
                    
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("hexor") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**𝗕𝗼𝘁 𝗢𝗻𝗹𝗶𝗻𝗲..😎**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "𝗦𝘂𝗽𝗽𝗼𝗿𝘁", url="https://t.me/proud_of_Indian")
                ]
            ]
        )
   )
