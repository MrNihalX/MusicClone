# Powered By NOBITA_XD IF You Fresh Any Problem To Contact The  Owner

import sys

from pyrogram import Client

from Nobita import config

from ..logging import LOGGER

assistants = []
assistantids = []


class Userbot(Client):
    def __init__(self):
        self.one = Client(
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_name=str(config.STRING1),
            no_updates=True,
        )
        self.two = Client(
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_name=str(config.STRING2),
            no_updates=True,
        )
        self.three = Client(
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_name=str(config.STRING3),
            no_updates=True,
        )
        self.four = Client(
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_name=str(config.STRING4),
            no_updates=True,
        )
        self.five = Client(
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_name=str(config.STRING5),
            no_updates=True,
        )

    async def start(self):
        LOGGER(__name__).info(f"🌷 ɢᴇᴛᴛɪɴɢs ᴀssɪsᴛᴀɴᴛ ɪɴғᴏ 🔍...")
        if config.STRING1:
            await self.one.start()
            try:
                await self.one.join_chat("AAPLI_YARRI")
                await self.one.join_chat("Nobita_Logo")
            except:
                pass
            assistants.append(1)
            get_me = await self.one.get_me()
            self.one.username = get_me.username
            self.one.id = get_me.id
            assistantids.append(get_me.id)
            if get_me.last_name:
                self.one.name = (
                    get_me.first_name + " " + get_me.last_name
                )
            else:
                self.one.name = get_me.first_name
            LOGGER(__name__).info(
                f"🌷 sʜɪᴢᴜᴋᴀ_ɴᴏʙɪ ᴀssɪsᴛᴀɴᴛ sᴛᴀʀᴛᴇᴅ ᴀs {self.one.name}"
            )
            try:
                await self.one.send_message(
                    config.LOG_GROUP_ID, f"🌷 sʜɪᴢᴜᴋᴀ_ɴᴏʙɪ ✵ ʙᴏᴛ ᴀssɪsᴛᴀɴᴛ  1 sᴛᴀʀᴛᴇᴅ 🌺.\n\n✅ ɴᴀᴍᴇ :**{self.one.name}\n👑 ᴜsᴇʀɴᴀᴍᴇ : @{self.one.username}\n🌷 ɪᴅ : {self.one.id}"
                )
            except:
                LOGGER(__name__).error(
                    f"💥 ᴀssɪsᴛᴀɴᴛ 1 ғᴀɪʟᴇᴅ ᴛᴏ ᴀᴄᴄᴇss ʟᴏɢ ɢʀᴏᴜᴘ 🥀. 📌 ᴍᴀᴋᴇ sᴜʀᴜ ʏᴏᴜ ᴀᴅᴅ ᴀsɪsɪᴛᴀɴᴛ ᴛʜᴇ ʟᴏɢs ɢʀᴏᴜᴘ 🌷 ᴀɴᴅ ᴘʀᴏᴍᴏᴛᴇ ᴀs ᴀ ᴀᴅᴍɪɴ  💥 "
                )
                sys.exit()
        if config.STRING2:
            await self.two.start()
            try:
                await self.two.join_chat("AAPLI_YARRI")
                await self.two.join_chat("Nobita_Logo")
            except:
                pass
            assistants.append(2)
            get_me = await self.two.get_me()
            self.two.username = get_me.username
            self.two.id = get_me.id
            assistantids.append(get_me.id)
            if get_me.last_name:
                self.two.name = (
                    get_me.first_name + " " + get_me.last_name
                )
            else:
                self.two.name = get_me.first_name
            try:
                await self.two.send_message(
                    config.LOG_GROUP_ID, f"🌷 sʜɪᴢᴜᴋᴀ_ɴᴏʙɪ ✵ ʙᴏᴛ ᴀssɪsᴛᴀɴᴛ 2 sᴛᴀʀᴛᴇᴅ.\n\n✅ ɴᴀᴍᴇ :{self.two.name}\n👑 ᴜsᴇʀɴᴀᴍᴇ : @{self.two.username}\n🌷 ɪᴅ : {self.two.id}"
                )
            except:
                LOGGER(__name__).error(
                    f"💥 ᴀssɪsᴛᴀɴᴛ 2 ғᴀɪʟᴇᴅ ᴛᴏ ᴀᴄᴄᴇss ʟᴏɢ ɢʀᴏᴜᴘ 🥀. 📌 ᴍᴀᴋᴇ sᴜʀᴜ ʏᴏᴜ ᴀᴅᴅ ᴀsɪsɪᴛᴀɴᴛ ᴛʜᴇ ʟᴏɢs ɢʀᴏᴜᴘ 🌷 ᴀɴᴅ ᴘʀᴏᴍᴏᴛᴇ ᴀs ᴀ ᴀᴅᴍɪɴ 💥"
                )
                sys.exit()
            LOGGER(__name__).info(
                f"🌷 𝐁𝐠𝐭 𝐀𝐬𝐬𝐢𝐬𝐭𝐚𝐧𝐭 2 𝐒𝐭𝐚𝐫𝐭𝐞𝐝 𝐀𝐬 {self.two.name}"
            )
        if config.STRING3:
            await self.three.start()
            try:
                await self.three.join_chat("Bgt_Chat")
                await self.three.join_chat("BikashGadgetsTech")
            except:
                pass
            assistants.append(3)
            get_me = await self.three.get_me()
            self.three.username = get_me.username
            self.three.id = get_me.id
            assistantids.append(get_me.id)
            if get_me.last_name:
                self.three.name = (
                    get_me.first_name + " " + get_me.last_name
                )
            else:
                self.three.name = get_me.first_name
            try:
                await self.three.send_message(
                    config.LOG_GROUP_ID, f"🌷 𝐁𝐠𝐭 ✵ 𝐑𝐨𝐛𝐨𝐭 𝐀𝐬𝐬𝐢𝐬𝐭𝐚𝐧𝐭 3 𝐒𝐭𝐚𝐫𝐭𝐞𝐝.\n\n✅ 𝐍𝐚𝐦𝐞 :{self.three.name}\n👑 𝐔𝐬𝐞𝐫𝐧𝐚𝐦𝐞 : @{self.three.username}\n🌷 𝐈𝐝 : {self.three.id}"
                )
            except:
                LOGGER(__name__).error(
                    f"💥 𝐀𝐬𝐬𝐢𝐬𝐭𝐚𝐧𝐭 3 𝐅𝐚𝐢𝐥𝐞𝐝 𝐓𝐨 𝐀𝐜𝐜𝐞𝐬𝐬 𝐋𝐨𝐠 𝐆𝐫𝐨𝐮𝐩 🥀. 📌 𝐌𝐚𝐤𝐞 𝐒𝐮𝐫𝐞 𝐘𝐨𝐮 𝐀𝐝𝐝 𝐀𝐬𝐬𝐢𝐬𝐭𝐚𝐧𝐭 𝐓𝐡𝐞 𝐋𝐨𝐠 𝐆𝐫𝐨𝐮𝐩 🌷 𝐚𝐧𝐝  𝐏𝐫𝐨𝐦𝐨𝐭𝐞 𝐀𝐬 𝐚 𝐀𝐝𝐦𝐢𝐧 💥"
                )
                sys.exit()
            LOGGER(__name__).info(
                f"🌷 𝐁𝐠𝐭 𝐀𝐬𝐬𝐢𝐬𝐭𝐚𝐧𝐭 3 𝐒𝐭𝐚𝐫𝐭𝐞𝐝 𝐀𝐬 {self.three.name}"
            )
        if config.STRING4:
            await self.four.start()
            try:
                await self.four.join_chat("Bgt_Chat")
                await self.four.join_chat("BikashGadgetsTech")
            except:
                pass
            assistants.append(4)
            get_me = await self.four.get_me()
            self.four.username = get_me.username
            self.four.id = get_me.id
            assistantids.append(get_me.id)
            if get_me.last_name:
                self.four.name = (
                    get_me.first_name + " " + get_me.last_name
                )
            else:
                self.four.name = get_me.first_name
            try:
                await self.four.send_message(
                    config.LOG_GROUP_ID, f"🌷 𝐁𝐠𝐭 ✵ 𝐑𝐨𝐛𝐨𝐭 𝐀𝐬𝐬𝐢𝐬𝐭𝐚𝐧𝐭 4 𝐒𝐭𝐚𝐫𝐭𝐞𝐝.\n\n✅ 𝐍𝐚𝐦𝐞 :{self.four.name}\n👑 𝐔𝐬𝐞𝐫𝐍𝐚𝐦𝐞 : @{self.four.username}\n🌷 𝐈𝐝 : {self.four.id}"
                )
            except:
                LOGGER(__name__).error(
                    f"💥 𝐀𝐬𝐬𝐢𝐬𝐭𝐚𝐧𝐭 4 𝐅𝐚𝐢𝐥𝐞𝐝 𝐓𝐨 𝐀𝐜𝐜𝐞𝐬𝐬 𝐋𝐨𝐠 𝐆𝐫𝐨𝐮𝐩 🥀. 📌 𝐌𝐚𝐤𝐞 𝐒𝐮𝐫𝐞 𝐘𝐨𝐮 𝐀𝐝𝐝 𝐀𝐬𝐬𝐢𝐬𝐭𝐚𝐧𝐭 𝐓𝐡𝐞 𝐋𝐨𝐠 𝐆𝐫𝐨𝐮𝐩 🌷 𝐚𝐧𝐝  𝐏𝐫𝐨𝐦𝐨𝐭𝐞 𝐀𝐬 𝐚 𝐀𝐝𝐦𝐢𝐧 💥"
                )
                sys.exit()
            LOGGER(__name__).info(
                f"🌷 𝐁𝐠𝐭 𝐀𝐬𝐬𝐢𝐬𝐭𝐚𝐧𝐭 4 𝐒𝐭𝐚𝐫𝐭𝐞𝐝 𝐀𝐬 {self.four.name}"
            )
        if config.STRING5:
            await self.five.start()
            try:
                await self.five.join_chat("Bgt_Chat")
                await self.five.join_chat("BikashGadgetsTech")
            except:
                pass
            assistants.append(5)
            get_me = await self.five.get_me()
            self.five.username = get_me.username
            self.five.id = get_me.id
            assistantids.append(get_me.id)
            if get_me.last_name:
                self.five.name = (
                    get_me.first_name + " " + get_me.last_name
                )
            else:
                self.five.name = get_me.first_name
            try:
                await self.five.send_message(
                    config.LOG_GROUP_ID, f"🌷 𝐁𝐠𝐭 ✵ 𝐑𝐨𝐛𝐨𝐭 𝐀𝐬𝐬𝐢𝐬𝐭𝐚𝐧𝐭 5 𝐒𝐭𝐚𝐫𝐭𝐞𝐝.\n\n✅ 𝐍𝐚𝐦𝐞 :{self.five.name}\n👑 𝐔𝐬𝐞𝐫𝐍𝐚𝐦𝐞:** @{self.five.username}\n🌷 𝐈𝐝 : {self.five.id}"
                )
            except:
                LOGGER(__name__).error(
                    f"💥 𝐀𝐬𝐬𝐢𝐬𝐭𝐚𝐧𝐭 5 𝐅𝐚𝐢𝐥𝐞𝐝 𝐓𝐨 𝐀𝐜𝐜𝐞𝐬𝐬 𝐋𝐨𝐠 𝐆𝐫𝐨𝐮𝐩 🥀. 📌 𝐌𝐚𝐤𝐞 𝐒𝐮𝐫𝐞 𝐘𝐨𝐮 𝐀𝐝𝐝 𝐀𝐬𝐬𝐢𝐬𝐭𝐚𝐧𝐭 𝐓𝐡𝐞 𝐋𝐨𝐠 𝐆𝐫𝐨𝐮𝐩 🌷 𝐚𝐧𝐝  𝐏𝐫𝐨𝐦𝐨𝐭𝐞 𝐀𝐬 𝐚 𝐀𝐝𝐦𝐢𝐧 💥 "
                )
                sys.exit()
            LOGGER(__name__).info(
                f"🌷 𝐁𝐠𝐭 𝐀𝐬𝐬𝐢𝐬𝐭𝐚𝐧𝐭 4 𝐒𝐭𝐚𝐫𝐭𝐞𝐝 𝐀𝐬 {self.five.name}"
            )
