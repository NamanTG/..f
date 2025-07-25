import asyncio, re
from pyrogram import Client, filters
from pyrogram.errors import FloodWait
from vars import FROM_DB, TO_DB

import logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

media_filter = filters.document | filters.video
lock = asyncio.Lock()

forwarded = 0
count = 3593
mcount = 991

@Client.on_message(filters.chat(FROM_DB) & media_filter)
async def auto_forward(bot, message):
    global forwarded, count, mcount
    file_caption = re.sub(r"(❤️‍🔥 Join ~ [ @Moonknight_media ])|(🤖 Join Us \[@BoB_Files1\])|(𝗧𝗛𝗘 𝗣𝗥𝗢𝗙𝗘𝗦𝗦𝗢𝗥 )|(𝙿𝚘𝚠𝚎𝚛e𝚍 𝙱𝚢 ➥  @Theprofessers)|(❤️‍🔥 Join ~ [ @Moonknight_media ])|(\n🔸 Upload By \[@BlackDeath_0\])|(\n❤️‍🔥 Join ~ \[@Moonknight_media\])|(@Ac_Linkzz)|(\n⚡️Join:- \[@BlackDeath_0\]‌‌)|(EonMovies)|(\nJOIN 💎 : @M2LINKS)|@\w+|(_|\- |\.|\+)", " ", str(message.caption))
    file_caption = f"""<b>{file_caption}</b>"""
    async with lock:
        try:
            if count != 0:
                if mcount != 0:
                    await message.copy(
                            chat_id=int(TO_DB),
                            caption=file_caption
                        )
                    forwarded += 1
                    count -= 1
                    mcount -= 1
                    logger.info(f"Forwarded {message.caption} from {FROM_DB} to {TO_DB}\nforwarded {forwarded} files")
                    await asyncio.sleep(2)
                else:
                    logger.info(f"⏸️ {forwarded} files sent! Taking a break of 10 minutes...")
                    await asyncio.sleep(600)
                    mcount = 991
            else:
                logger.info(f"⏸️ {forwarded} files sent! Taking a break of 1 hour...")
                await asyncio.sleep(3600)
                count = 3593
        except FloodWait as e:
            logger.warning(f"Got FloodWait.\n\nWaiting for {e.value} seconds.")
            await asyncio.sleep(e.value + 2)
            if count != 0:
                if mcount != 0:
                    await message.copy(
                            chat_id=int(TO_DB),
                            caption=file_caption
                        )
                    forwarded += 1
                    count -= 1
                    mcount -= 1
                    logger.info(f"Forwarded {message.caption} from {FROM_DB} to {TO_DB}\nforwarded {forwarded} files")
                    await asyncio.sleep(2)
                else:
                    logger.info(f"⏸️ {forwarded} files sent! Taking a break of 10 minutes...")
                    await asyncio.sleep(600)
                    mcount = 991
            else:
                logger.info(f"⏸️ {forwarded} files sent! Taking a break of 1 hour...")
                await asyncio.sleep(3600)
                count = 3593
