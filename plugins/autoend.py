# # Powered By NOBITA_XD IF You Fresh Any Problem To Contact The Owner

# Powered By @NOBI_XXD

# ©️ Copy Right By NOBITA_XD

# Any Problem To Report @AAPLI_YAARI

# Bot Owner @NOBI_XXD

from pyrogram import filters

from Nobita import config
from Nobita.strings import get_command
from Nobita import app
from Nobita.misc import SUDOERS
from Nobita.utils.database import autoend_off, autoend_on
from Nobita.utils.decorators.language import language

# Commands
AUTOEND_COMMAND = get_command("AUTOEND_COMMAND")


@app.on_message(filters.command(AUTOEND_COMMAND) & SUDOERS)
async def auto_end_stream(client, message):
    usage = "🔰 ᴜsᴀɢᴇ 🔰 :\n\n/autoend [enable|disable]"
    if len(message.command) != 2:
        return await message.reply_text(usage)
    state = message.text.split(None, 1)[1].strip()
    state = state.lower()
    if state == "enable":
        await autoend_on()
        await message.reply_text(
            "🔰 ᴀᴜᴛᴏ ᴇɴᴅ sᴛʀᴇᴀᴍ ᴇɴᴀʙʟᴇᴅ ✅.\n\n💥 ɴᴏʙɪᴛᴀ ᴍᴜsɪᴄ ʙᴏᴛ ᴀssɪsᴛᴀɴᴛ ᴡɪʟ ᴀᴜᴛᴏ ʟᴇᴀᴠᴇ ᴛʜᴇ ᴠᴏɪᴄᴇ ᴄʜᴀᴛ ᴡʜᴇɴ ᴀɴʏᴏɴᴇ ɴᴏ ᴀᴄᴛɪᴠᴇ ᴛʜᴇ ᴠᴏɪᴄᴇ ᴄʜᴀᴛ ᴀɴᴅ ʙᴏᴛ sᴇɴᴅ ᴀ ʟᴇᴀᴠᴇ ᴍᴀssᴀɢᴇ 📝."
        )
    elif state == "disable":
        await autoend_off()
        await message.reply_text("🔰 ᴀᴜᴛᴏ ᴇɴᴅ sᴛʀᴇᴀᴍ ᴅɪsᴀʙʟᴇᴅ ❎.")
    else:
        await message.reply_text(usage)
