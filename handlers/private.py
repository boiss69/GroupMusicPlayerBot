from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    await message.reply_sticker("CAACAgQAAx0CTv65QgABBfJlYF6VCrGMm6OJ23AxHmD6qUSWESsAAhoQAAKm8XEeD5nrjz5IJFYeBA")
    await message.reply_text(
        f"""Halo, saya adalah {bn}!
Saya adalah bot Music yang dirancang khusus untuk menemani anda memutar musik dalam grup melalui obrolan suara.
Masukkan saya kedalam grup, dan dengarkan musik sepuasnya!
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "CARA PENGGUNAAN", url="https://t.me/boimusicbotinfo/17")
                  ],[
                    InlineKeyboardButton(
                        "OWNER BOT", url="https://t.me/boiii999"
                    ),
                    InlineKeyboardButton(
                        "INSTAGRAM", url="https://www.instagram.com/aipmarvelous/"
                    )
                ]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**Bot Musik Online ✅**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "CARA PENGGUNAAN", url="https://t.me/boimusicbotinfo/17")
                ]
            ]
        )
   )


