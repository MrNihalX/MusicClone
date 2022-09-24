# # Powered By NOBITA_XD IF You Fresh Any Problem To Contact The Owner

# Powered By @NOBI_XXD

# ©️ Copy Right By NOBITA_XD

# Any Problem To Report @AAPLI_YAARI

# Bot Owner @NOBI_XXD
from pyrogram import filters

from Bikash import config
from Bikash.strings import get_command
from Bikash import app
from Bikash.misc import SUDOERS
from Bikash.utils.database import autoend_off, autoend_on
from Bikash.utils.decorators.language import language

# Commands
AUTOEND_COMMAND = get_command("AUTOEND_COMMAND")


@app.on_message(filters.command(AUTOEND_COMMAND) & SUDOERS)
async def auto_end_stream(client, message):
    usage = "🔰 𝐔𝐬𝐚𝐠𝐞 🔰 :\n\n/autoend [enable|disable]"
    if len(message.command) != 2:
        return await message.reply_text(usage)
    state = message.text.split(None, 1)[1].strip()
    state = state.lower()
    if state == "enable":
        await autoend_on()
        await message.reply_text(
            "🔰 𝐀𝐮𝐭𝐨 𝐄𝐧𝐝 𝐒𝐭𝐫𝐞𝐚𝐦 𝐄𝐧𝐚𝐛𝐥𝐞𝐝 ✅.\n\n💥 𝐁𝐠𝐭 𝐌𝐮𝐬𝐢𝐜 𝐁𝐨𝐭 𝐀𝐬𝐬𝐢𝐬𝐭𝐚𝐧𝐭 𝐖𝐢𝐥𝐥 𝐀𝐮𝐭𝐨 𝐋𝐞𝐚𝐯𝐞 𝐓𝐡𝐞 𝐕𝐨𝐢𝐜𝐞 𝐂𝐡𝐚𝐭 𝐖𝐡𝐞𝐧 𝐀𝐧𝐲𝐨𝐧𝐞 𝐍𝐨 𝐀𝐯𝐭𝐢𝐯𝐞 𝐓𝐡𝐞 𝐕𝐨𝐢𝐜𝐞 𝐂𝐡𝐚𝐭 𝐀𝐧𝐝 𝐁𝐨𝐭 𝐒𝐞𝐧𝐝 𝐀 𝐋𝐞𝐚𝐯𝐞 𝐌𝐞𝐬𝐬𝐚𝐠𝐞 📝."
        )
    elif state == "disable":
        await autoend_off()
        await message.reply_text("🔰 𝐀𝐮𝐭𝐨 𝐄𝐧𝐝 𝐒𝐭𝐫𝐞𝐚𝐦 𝐃𝐢𝐬𝐚𝐛𝐥𝐞𝐝 ❎.")
    else:
        await message.reply_text(usage)
