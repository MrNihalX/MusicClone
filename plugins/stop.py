# Powered By NOBITA_XD 
# ©️ Copy Right By NOBITA_XD 
# Any Problem To Report NOBITA_XD 
# Bot Owner NOBITA_XD 
from pyrogram import filters
from pyrogram.types import Message

from Nobita.config import BANNED_USERS
from Nobita.strings import get_command
from Nobita import app
from Nobita.core.call import Nobita
from Nobita.utils.database import set_loop
from Nobita.utils.decorators import AdminRightsCheck

# Commands
STOP_COMMAND = get_command("STOP_COMMAND")


@app.on_message(
    filters.command(STOP_COMMAND)
    & filters.group
    & ~filters.edited
    & ~BANNED_USERS
)
@AdminRightsCheck
async def stop_music(cli, message: Message, _, chat_id):
    if not len(message.command) == 1:
        return await message.reply_text(_["general_2"])
    await Nobita.stop_stream(chat_id)
    await set_loop(chat_id, 0)
    await message.reply_text(
        _["bh_9"].format(message.from_user.mention)
    )
