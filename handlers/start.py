from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from helpers.filters import command, other_filters, other_filters2


@Client.on_message(command("start") & other_filters)
async def start(_, message: Message):
    await message.reply_text(
        f"""<b>🚭👯🎻HELLO.!!! {message.from_user.first_name}!</b>

THESE IS AN MUSIC PLAYER BOT CAN PLAY'S MUSIC ON YOUR TELEGRAPH GROUP VOICE CHAT. 

USE THE BUTTONS BELOW TO KNOW MORE ABOUT ME AND MY SAURCE CODE ALSO GIVEN.""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "⚡DEVLOPER⚡", url="https://t.me/MR_PURUSHOTTAM_M"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "⚡ASK FOR SUPPORT🙃⚡", url="https://t.me/su_Chats"
                    ),
                    InlineKeyboardButton(
                        "🌏SAURCE CODE🌎", url="https://github.com/PURHSHOTTAM/M-PLAYERH2.3"
                    )
                ]
            ]
        )
    )


@Client.on_message(command("start") & other_filters2)
async def start2(_, message: Message):
    await message.reply_text(
        "💁🏻‍♂️ Do you want to search for a YouTube video?",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "✅ Yes", switch_inline_query_current_chat=""
                    ),
                    InlineKeyboardButton(
                        "No ❌", callback_data="close"
                    )
                ]
            ]
        )
    )
