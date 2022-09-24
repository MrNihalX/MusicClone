# Powered By NOBITA_XD IF You Fresh Any Problem To Contact The Owner

# Powered By @NOBI_XXD

# ©️ Copy Right By NOBITA_XD

# Any Problem To Report @AAPLI_YAARI

# Bot Owner @NOBI_XXD 

import asyncio
from datetime import datetime

from Nobita import config
from Nobita import app
from Nobita.core.call import Nobita, autoend
from Nobita.utils.database import (get_client, is_active_chat,
                                       is_autoend)


async def auto_leave():
    if config.AUTO_LEAVING_ASSISTANT == str(True):
        while not await asyncio.sleep(
            config.AUTO_LEAVE_ASSISTANT_TIME
        ):
            from NobitaX.core.userbot import assistants

            for num in assistants:
                client = await get_client(num)
                try:
                    async for i in client.iter_dialogs():
                        chat_type = i.chat.type
                        if chat_type in [
                            "supergroup",
                            "group",
                            "channel",
                        ]:
                            chat_id = i.chat.id
                            if (
                                chat_id != Nobita.config.LOG_GROUP_ID
                                and chat_id != -1001438979109
                            ):
                                if not await is_active_chat(chat_id):
                                    try:
                                        await client.leave_chat(
                                            chat_id
                                        )
                                    except:
                                        continue
                except:
                    pass


asyncio.create_task(auto_leave())


async def auto_end():
    while not await asyncio.sleep(5):
        if not await is_autoend():
            continue
        for chat_id in autoend:
            timer = autoend.get(chat_id)
            if not timer:
                continue
            if datetime.now() > timer:
                if not await is_active_chat(chat_id):
                    autoend[chat_id] = {}
                    continue
                autoend[chat_id] = {}
                try:
                    await Nobita.stop_stream(chat_id)
                except:
                    continue
                try:
                    await app.send_message(
                        chat_id,
                        "🌷 𝐁𝐠𝐭 𝐁𝐨𝐭 𝐀𝐬𝐬𝐢𝐬𝐭𝐚𝐧𝐭 𝐀𝐮𝐭𝐨  𝐋𝐞𝐟𝐭 𝐓𝐡𝐞 𝐕𝐨𝐢𝐜𝐞 𝐂𝐡𝐚𝐭 𝐁𝐞𝐚𝐜𝐚𝐮𝐬𝐞 𝐍𝐨 𝐎𝐧𝐞 𝐀𝐜𝐭𝐢𝐯𝐞 𝐎𝐧 𝐕𝐨𝐢𝐜𝐞 𝐜𝐡𝐚𝐭 🌷.",
                    )
                except:
                    continue


asyncio.create_task(auto_end())
