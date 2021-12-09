
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
                        "✨𝗔𝗗𝗗 𝗠𝗘 𝗧𝗢 𝗬𝗢𝗨𝗥 𝗚𝗥𝗢𝗨𝗣✨", url="http://t.me/Kiara_ro_bot?startgroup=true")
                  ],[
                    InlineKeyboardButton(
                        "🌷𝗦𝘂𝗽𝗽𝗼𝗿𝘁 𝗖𝗵𝗮𝗻𝗻𝗲𝗹🥀", url="http://t.me/The_Blaze_NETWORK"
                    ),
                    InlineKeyboardButton(
                        "✨𝗦𝘂𝗽𝗽𝗼𝗿𝘁 𝗚𝗿𝗼𝘂𝗽✨", url="https://t.me/The_Secret_worlds"
                    )
                ],[ 
                    InlineKeyboardButton(
                        "🌷𝗛𝗲𝗹𝗽 & 𝗖𝗼𝗺𝗺𝗮𝗻𝗱𝘀💥", url="https://telegra.ph/eSport-MusicX-Command-11-30"
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
                        "𝗦𝘂𝗽𝗽𝗼𝗿𝘁", url="https://t.me/proud_of_Indian")
                ]
            ]
        )
   )
