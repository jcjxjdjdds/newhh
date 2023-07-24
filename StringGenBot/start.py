from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message

from config import OWNER_ID


def filter(cmd: str):
    return filters.private & filters.incoming & filters.command(cmd)

@Client.on_message(filter("start"))
async def start(bot: Client, msg: Message):
    me2 = (await bot.get_me()).mention
    await bot.send_message(
        chat_id=msg.chat.id,
        text=f"""
مـࢪحبـًا عـزيـزي {msg.from_user.mention},
أنـا مـخـصـص لاسـتخـࢪاج اެݪجـلـسات
بـايـࢪوجࢪام أو تـيـࢪمـكس
للبـدء في الاسـتـخࢪاج اضغط بدأ استـخࢪاج اެݪجـلـسة

[الـمـطـور](tg://user?id={OWNER_ID})""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(text="بـدأ استـخـࢪاج اެݪجـلسة", callback_data="generate")
                ],
                [
                    InlineKeyboardButton("قناتي", url="https://t.me/Q1IIQ"),
                    InlineKeyboardButton("الـمـطـور", user_id=OWNER_ID)
                ]
            ]
        ),
        disable_web_page_preview=True,
    )
