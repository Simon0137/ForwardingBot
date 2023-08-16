import asyncio

import aiogram.utils.markdown as md
from aiogram import Bot, Dispatcher, F, Router
from aiogram.enums import ParseMode
from aiogram.filters import Command, CommandStart
from aiogram.types import Message, Poll

from app_settings import AppSettings

main_router = Router()
bot = Bot(token=AppSettings().token)

@main_router.message(CommandStart())
async def start_command_handler(message: Message):
    pass

@main_router.message(F.chat.func(lambda chat: chat.type == 'group' or chat.type == 'supergroup'), Command('get_group_id'))
async def get_group_id_command_handler(message: Message):
    try:
        await bot.delete_message(message.chat.id, message.message_id)
    except Exception:
        pass
    user_id = message.from_user.id
    try:
        await bot.send_message(user_id, 'Group ID: `' + str(message.chat.id) + '`', parse_mode=ParseMode.MARKDOWN)
    except Exception as e:
        print(f'ERROR: {e}')
    
@main_router.channel_post(F.text == '/get_channel_id')
async def channel_get_id_handler(message: Message):
    try:
        await bot.delete_message(message.chat.id, message.message_id)
    except Exception:
        pass
    try:
        await bot.send_message(message.chat.id, 'Channel ID: `' + str(message.chat.id) + '`', parse_mode=ParseMode.MARKDOWN)
    except Exception as e:
        print(f'ERROR: {e}')

@main_router.message(F.chat.func(lambda chat: chat.type == 'private'))
async def anymessage_handler(message: Message):
    app_settings = AppSettings()
    if app_settings.usernames.__contains__(message.from_user.username):
        try:
            msg = await bot.copy_message(app_settings.main_channel_id, message.chat.id, message.message_id)
            for group_id in app_settings.group_ids:
                try:
                    await bot.forward_message(group_id, app_settings.main_channel_id, msg.message_id)
                except Exception as e:
                    print(f'ERROR: {e}')
        except Exception as e:
            print(f'ERROR: {e}')


async def main():
    dp = Dispatcher()
    dp.include_router(main_router)
    
    print('Bot started!')
    await dp.start_polling(bot)
    
if __name__ == '__main__':
    try:
        asyncio.run(main())
    except Exception as e:
        print(f'ERROR: {e}')
    print('Bot stopped!')