# Powered By NOBITA_XD IF You Fresh Any Problem To Contact The Owner


from typing import Union

from pyrogram import filters, types
from pyrogram.types import InlineKeyboardMarkup, Message

from Nobita import config
from Nobita.config import BANNED_USERS
from Nobita.strings import get_command, get_string, helpers
from Nobita import app
from Nobita.misc import SUDOERS
from Nobita.utils import help_pannel
from Nobita.utils.database import get_lang, is_commanddelete_on
from Nobita.utils.decorators.language import (LanguageStart,
                                                  languageCB)
from Nobita.utils.inline.help import (help_back_markup,
                                          private_help_panel)




### Command
HELP_COMMAND = get_command("HELP_COMMAND")


@app.on_message(
    filters.command(["HELP_COMMAND"])
    & filters.private
    & ~filters.edited
    & ~BANNED_USERS
)
@app.on_callback_query(
    filters.regex("settings_back_helper") & ~BANNED_USERS
)
async def helper_private(
    client: app, update: Union[types.Message, types.CallbackQuery]
):
    is_callback = isinstance(update, types.CallbackQuery)
    if is_callback:
        try:
            await update.answer()
        except:
            pass
        chat_id = update.message.chat.id
        language = await get_lang(chat_id)
        _ = get_string(language)
        keyboard = help_pannel(_, True)
        if update.message.photo:
            await update.message.delete()
            await update.message.reply_text(
                "**✅ ᴄʟɪᴄᴋ ᴏɴ ᴛʜᴇ ʙᴇʟᴏᴡ ʙᴜᴛᴛᴏɴs ғᴏʀ\nᴍᴏʀᴇ ɪɴғᴏʀᴍᴀᴛɪᴏɴ✨ ...\n\n🥀ɪғ ʏᴏᴜ ᴀʀᴇ ғᴀᴄɪɴɢ » ᴀɴʏ ᴘʀᴏʙʟᴇᴍs ɪɴ ᴄᴏᴍᴍᴀɴᴅ ᴛʜᴇɴ ❥︎ ʏᴏᴜ ᴄᴀɴ ᴄᴏɴᴛᴀᴄᴛ ᴛᴏ\nᴍʏ ᴏᴡɴᴇʀ ❥︎ ᴏʀ ᴀsᴋ ɪɴ ❥︎ ᴏᴜʀ sᴜᴘᴘᴏʀᴛ\nᴄʜᴀᴛ ɢʀᴏᴜᴘ 💞 ...\n\n🌷ᴀʟʟ ᴄᴏᴍᴍᴀɴᴅs ᴄᴀɴ ʙᴇ ᴜsᴇᴅ ᴡɪᴛʜ : /**", reply_markup=keyboard
            )
        else:
            await update.edit_message_text(
                "**✅ ᴄʟɪᴄᴋ ᴏɴ ᴛʜᴇ ʙᴇʟᴏᴡ ʙᴜᴛᴛᴏɴs ғᴏʀ\nᴍᴏʀᴇ ɪɴғᴏʀᴍᴀᴛɪᴏɴ ✨ ...\n\n🥀ɪғ ʏᴏᴜ ᴀʀᴇ ғᴀᴄɪɴɢ » ᴀɴʏ ᴘʀᴏʙʟᴇᴍs ɪɴ ᴄᴏᴍᴍᴀɴᴅ ᴛʜᴇɴ ❥︎ ʏᴏᴜ ᴄᴀɴ ᴄᴏɴᴛᴀᴄᴛ ᴛᴏ\nᴍʏ ᴏᴡɴᴇʀ ❥︎ ᴏʀ ᴀsᴋ ɪɴ ❥︎ ᴏᴜʀ sᴜᴘᴘᴏʀᴛ\nᴄʜᴀᴛ ɢʀᴏᴜᴘ 💞 ...\n\n🌷ᴀʟʟ ᴄᴏᴍᴍᴀɴᴅs ᴄᴀɴ ʙᴇ ᴜsᴇᴅ ᴡɪᴛʜ: /**", reply_markup=keyboard
            )
    else:
        chat_id = update.chat.id
        if await is_commanddelete_on(update.chat.id):
            try:
                await update.delete()
            except:
                pass
        language = await get_lang(chat_id)
        _ = get_string(language)
        keyboard = help_pannel(_)
        await update.reply_text("**✅ ᴄʟɪᴄᴋ ᴏɴ ᴛʜᴇ ʙᴇʟᴏᴡ ʙᴜᴛᴛᴏɴs ғᴏʀ\nᴍᴏʀᴇ ɪɴғᴏʀᴍᴀᴛɪᴏɴ ✨ ...\n\n🥀𝐈𝐟 𝐘𝐨𝐮 𝐀𝐫𝐞 𝐅𝐚𝐜𝐢𝐧𝐠 » 𝐀𝐧𝐲 𝐏𝐫𝐨𝐛𝐥𝐞𝐦𝐬 𝐢𝐧 𝐂𝐨𝐦𝐦𝐚𝐧𝐝 𝐓𝐡𝐞𝐧 ❥︎ 𝐘𝐨𝐮 𝐂𝐚𝐧 𝐂𝐨𝐧𝐭𝐚𝐜𝐭 𝐓𝐨\n𝐌𝐲 𝐎𝐰𝐧𝐞𝐫 ❥︎ 𝐎𝐫 𝐀𝐬𝐤 𝐢𝐧 ❥︎ 𝐎𝐮𝐫 𝐒𝐮𝐩𝐩𝐨𝐫𝐭\n𝐂𝐡𝐚𝐭 𝐆𝐫𝐨𝐮𝐩 💞 ...\n\n🌷𝐀𝐥𝐥 𝐂𝐨𝐦𝐦𝐚𝐧𝐝𝐬 𝐂𝐚𝐧 𝐁𝐞 𝐔𝐬𝐞𝐝 𝐖𝐢𝐭𝐡: /**", reply_markup=keyboard)


@app.on_message(
    filters.command(["help"])
    & filters.group
    & ~filters.edited
    & ~BANNED_USERS
)
@LanguageStart
async def help_com_group(client, message: Message, _):
    keyboard = private_help_panel(_)
    await message.reply_text(
        "**🥀 𝐂𝐨𝐧𝐭𝐚𝐜𝐭 𝐌𝐞 » 𝐢𝐧 𝐏𝐫𝐢𝐯𝐚𝐭𝐞\n𝐅𝐨𝐫 𝐌𝐨𝐫𝐞 𝐇𝐞𝐥𝐩 💞 ...**", reply_markup=InlineKeyboardMarkup(keyboard)
    )


@app.on_callback_query(filters.regex("help_callback") & ~BANNED_USERS)
@languageCB
async def helper_cb(client, CallbackQuery, _):
    callback_data = CallbackQuery.data.strip()
    cb = callback_data.split(None, 1)[1]
    keyboard = help_back_markup(_)
    if cb == "hb5":
        if CallbackQuery.from_user.id not in SUDOERS:
            return await CallbackQuery.answer(
                "🥀 𝐎𝐧𝐥𝐲 𝐅𝐨𝐫 𝐒𝐮𝐝𝐨 𝐔𝐬𝐞𝐫𝐬 💞", show_alert=True
            )
        else:
            await CallbackQuery.edit_message_text(
                helpers.HELP_5, reply_markup=keyboard
            )
            return await CallbackQuery.answer()
    try:
        await CallbackQuery.answer()
    except:
        pass
    if cb == "hb1":
        await CallbackQuery.edit_message_text(
            helpers.HELP_1, reply_markup=keyboard
        )
    elif cb == "hb2":
        await CallbackQuery.edit_message_text(
            helpers.HELP_2, reply_markup=keyboard
        )
    elif cb == "hb3":
        await CallbackQuery.edit_message_text(
            helpers.HELP_3, reply_markup=keyboard
        )
    elif cb == "hb4":
        await CallbackQuery.edit_message_text(
            helpers.HELP_4, reply_markup=keyboard
        )
