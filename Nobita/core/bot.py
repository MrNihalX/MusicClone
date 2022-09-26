# Powered By NOBITA_XD IF You Fresh Any Problem To Contact The Owner

import sys
from pyrogram import Client
from Nobita import config
from ..logging import LOGGER



class NobitaXBot(Client):
    def __init__(self):
        LOGGER(__name__).info(f"Starting Bot...")
        super().__init__(
            "shizuka_nobi",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            bot_token=config.BOT_TOKEN,
        )

    async def start(self):
        await super().start()
        get_me = await self.get_me()
        self.username = get_me.username
        self.id = get_me.id
        try:
            await self.send_message(
                config.LOG_GROUP_ID, "**😍 sʜɪᴢᴜᴋᴀ_ɴᴏʙɪ ᴍᴜsɪᴄ ʙᴏᴛ ɪs sᴛᴀʀᴛᴇᴅ ᴛᴏ ᴘʟᴀʏ ᴀɴʏ ᴛʜɪɴɢ 🎧**"
            )
        except:
            LOGGER(__name__).error(
                "💥 ʙᴏᴛ ғᴀɪʟᴇᴅ ᴛᴏ ᴀᴄᴄᴇss ʟᴏɢ ɢʀᴏᴜᴘ . 📌 ᴍᴀᴋᴇ sᴜʀᴜ ʏᴏᴜ ᴀᴅᴅ ᴛʜᴇ ʟᴏɢ ɢʀᴏᴜᴘ ᴀɴᴅ ᴘʀᴏᴍᴏᴛᴇ ᴀs ᴀᴅᴍɪɴ 𝐒𝐮𝐫𝐞 𝐘𝐨𝐮 𝐀𝐝𝐝 𝐁𝐨𝐭 𝐓𝐡𝐞 𝐋𝐨𝐠 𝐆𝐫𝐨𝐮𝐩 🌷 𝐚𝐧𝐝  𝐏𝐫𝐨𝐦𝐨𝐭𝐞 𝐀𝐬 𝐚 𝐀𝐝𝐦𝐢𝐧 💥 "
            )
            sys.exit()
        a = await self.get_chat_member(config.LOG_GROUP_ID, self.id)
        if a.status != "administrator":
            LOGGER(__name__).error(
                "💥 𝐏𝐥𝐞𝐚𝐬𝐞 𝐏𝐫𝐨𝐦𝐨𝐭𝐞 𝐁𝐠𝐭 𝐌𝐮𝐬𝐢𝐜 𝐁𝐨𝐭 🔊 𝐀𝐬 𝐀𝐝𝐦𝐢𝐧 𝐈𝐧 𝐘𝐨𝐮𝐫 𝐁𝐨𝐭 𝐋𝐨𝐠𝐠𝐞𝐫 𝐆𝐫𝐨𝐮𝐩 👑"
            )
            sys.exit()
        if get_me.last_name:
            self.name = get_me.first_name + " " + get_me.last_name
        else:
            self.name = get_me.first_name
        LOGGER(__name__).info(f"💥 𝐁𝐠𝐭 𝐌𝐮𝐬𝐢𝐜 𝐁𝐨𝐭 𝐒𝐭𝐚𝐫𝐭𝐞𝐝 𝐀𝐬 {self.name}")
