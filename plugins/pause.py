# Powered By @NOBITA_XD 
# ©️ Copy Right By NOBITA_XD 
# Any Problem To Report NOBITA_XD 
# Bot Owner NOBITA_XD 

from pyrogram import filters
from pyrogram.types import Message

from Nobita.config import BANNED_USERS
from Nobita.strings import get_command
from Nobita import app
from Nobita.core.call import Nobita as Anon
from Nobita.utils.database import is_music_playing, music_off
from Nobita.utils.decorators import AdminRightsCheck

# Commands
PAUSE_COMMAND = get_command("PAUSE_COMMAND")


@app.on_message(
    filters.command(PAUSE_COMMAND)
    & filters.group
    & ~filters.edited
    & ~BANNED_USERS
)
@AdminRightsCheck
async def pause_admin(cli, message: Message, _, chat_id):
    if not len(message.command) == 1:
        return await message.reply_text(_["general_2"])
    if not await is_music_playing(chat_id):
        return await message.reply_text(_["admin_1"])
    await music_off(chat_id)
    await Anon.pause_stream(chat_id)
    await message.reply_text(
        _["admin_2"].format(message.from_user.mention)
    )
