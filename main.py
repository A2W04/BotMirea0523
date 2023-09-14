import asyncio
import logging

from aiogram import Bot, Dispatcher, Router
from aiogram.enums.parse_mode import ParseMode
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.fsm.storage.memory import MemoryStorage


API_TOKEN = '6083527395:AAFD3nhQ6_jXrc-WycN5ZfgdkfIkQ6W3f0E'
router = Router()

admin = ['a2w04']
mute_chat = []


# @router.message(Command("starеt"))
# async def start_handler(msg: Message):
#     await msg.answer(f'{msg}')


@router.message(Command('mute_all'))
async def mute_all_handler(msg: Message):
    if msg.from_user.username in admin:
        mute_chat.append(msg.message_thread_id)
    else:
        await msg.delete()

        # await msg.answer(f'{msg.message_thread_id}')


@router.message(Command('mute_all_off'))
async def mute_all_off_handler(msg: Message):
    if msg.from_user.username in admin:
        mute_chat.remove(msg.message_thread_id)
    else:
        await msg.delete()


@router.message()
async def mute_handler(msg: Message):
    if msg.message_thread_id in mute_chat:
        if msg.from_user.username is None or msg.from_user.username not in admin:
            await msg.delete()


async def main():
    bot = Bot(token=API_TOKEN, parse_mode=ParseMode.HTML)
    dp = Dispatcher(storage=MemoryStorage())
    dp.include_router(router)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
