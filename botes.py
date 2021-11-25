import logging
from aiogram import Bot, Dispatcher, executor, types
from oxfordLookUp import get_definition
from googletrans import Translator

translator = Translator()

API_TOKEN = '2006834748:AAFV5tV8mUaCjIOJVEPrlMc53lvs6Vz1ga8'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply("Hi!\nI'm EchoBot!\nPowered by aiogram.")

@dp.message_handler()
async def tarjimon(message: types.Message):
    lang = translator.detect(message.text).lang
    if len(message.text.split())>2:
        if lang == 'en':
            dest = 'uz'
        else:
            dest='en'
        # dest='uz' if lang == 'en' else 'en'
        await message.reply(translator.translate(message.text, dest).text)
    else:
        if lang=='en':
            word_id = message.text
        else:
            word_id = translator.translate(message.text,dest='en').text
        lookup = get_definition(word_id)
        if lookup:
            print(word_id,lookup['definitions']," hech narsa kelmadimi")
            await message.reply(f"Word: {word_id} \nDefinitions:\n{lookup['definitions']}\n\n{lookup['audio']}")
            if lookup.get('audio'):
                await message.reply_audio(lookup['audio'])
        else:
            await message.reply("Bunday so'z topilmadi")

    # old style:
    # await bot.send_message(message.chat.id, message.text)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)