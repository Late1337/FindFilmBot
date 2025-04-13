import asyncio
import logging
import aiohttp
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message, FSInputFile, CallbackQuery
from aiogram.filters import CommandStart, Command
import confyg
from app.keyboards import MOVIE_HEROES, MOVIE_HEROES_BUTTONS

bot = Bot(token=confyg.TOKEN)
dp = Dispatcher()
API = "238a2571"

# словник з кодами для пошуку фільму
MOVIE_CODES = {
    "001": "tt1409024", # Men in black
    "002": "tt1375666", # Inception
    "003": "tt0133093", # Matrix
    "004": "tt1431045", # DeadPool
    "005": "tt0232500", # The Fast and the Furious
    "006": "tt0068646", # The Godfather
    "007": "tt0111161", # The Shawshank Redemption
    "008": "tt0137523", # Fight Club
    "009": "tt0109830", # Forrest Gump
    "010": "tt0468569", # The Dark Knight
    "011": "tt0120737", # The Lord of the Rings: The Fellowship of the Ring
    "012": "tt0167260", # The Lord of the Rings: The Return of the King
    "013": "tt5463162", # Deadpool 2
    "014": "tt0075148", # Rocky
    "015": "tt0120338", # Titanic
    "016": "tt0112573", # Braveheart
    "017": "tt1853728", # Django Unchained
    "018": "tt2713180", # Fury
    "019": "tt1637725", # Ted
    "020": "tt0993846", # The Wolf of Wall Street
    "021": "tt1130884", # Shutter Island
    "022": "tt0079817", # Rocky II
    "023": "tt0816711", # World War Z
    "024": "tt0088247", # The Terminator
    "025": "tt2637276", # Ted 2
    "026": "tt1469304", # Baywatch
    "027": "tt6263850", # Deadpool & Wolverine
    "028": "tt0099685", # GoodFellas
    "029": "tt0065832", # Hercules in New York
    "030": "tt7131622", # Once Upon a Time in... Hollywood
    "031": "tt0068767", # Jing wu men
    "032": "tt1489889", # Central Intelligence
    "033": "tt1375670", # Grown Ups
    "034": "tt11245972", # Scream
    "035": "tt0903747", # Breaking Bad
    "036": "tt0144084", # American Psycho
    "037": "tt0829482", # Superbad
    "038": "tt0443453", # Borat: Cultural Learnings of America for Make Benefit Glorious Nation of Kazakhstan
    "039": "tt0109686", # Dumb and Dumber
    "040": "tt0110475", # The Mask
    "041": "tt4276820", # The Founder
    "042": "tt1723121", # We're the Millers
    "043": "tt0084602", # Rocky III
    "044": "tt3076658", # Creed
    "045": "tt0462499", # Rambo
    "046": "tt0452608", # Death Race
    "047": "tt15398776", # Oppenheimer
    "048": "tt0290002", # Meet the Fockers
    "049": "tt0163651", # American Pie
    "050": "tt2191701" # Grown Ups 2

}

# фунція яка використовує API та шукає інформацію про фільм
async def get_movie_info(imdb_id: str):
    url = f"http://www.omdbapi.com/?i={imdb_id}&apikey={API}"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.json()

# команда самого початку боту
@dp.message(Command("start"))
async def command_start(message: Message):
    await message.answer("Greetings! This is a movie search bot. The bot has two commands:\n"
                         "/search_film - search film\n"
                         "/info - information about bot")

# команда для пошуку фільму
@dp.message(Command("search_film"))
async def start_handler(message: Message):
    await message.answer("Write the name of the movie and I will find information about it.(example 001)")

# команда з інформацією про бот
@dp.message(Command("info"))
async def command_info(message: Message):
    await message.answer(f"In real time BOT have 50 films\n"
                         f"--------------------------------------------\n"
                         f"🎬 code 001 - Men in black\n"
                         f"🎬 code 002 - Inception\n"
                         f"🎬 code 003 - Matrix\n"
                         f"🎬 code 004 - DeadPool\n"
                         f"🎬 code 005 - The Fast and the Furious\n"
                         f"🎬 code 006 - The Godfather\n"
                         f"🎬 code 007 - The Shawshank Redemption\n"
                         f"🎬 code 008 - Fight Club\n"
                         f"🎬 code 009 - Forrest Gump\n"
                         f"🎬 code 010 - The Dark Knight\n"
                         f"🎬 code 011 - The Lord of the Rings: The Fellowship of the Ring,\n"
                         f"🎬 code 012 - The Lord of the Rings: The Return of the King\n"
                         f"🎬 code 013 - Deadpool 2\n"
                         f"🎬 code 014 - Rocky\n"
                         f"🎬 code 015 - Titanic\n"
                         f"🎬 code 016 - Braveheart\n"
                         f"🎬 code 017 - Django Unchained\n"
                         f"🎬 code 018 - Fury\n"
                         f"🎬 code 019 - Ted\n"
                         f"🎬 code 020 - The Wolf of Wall Street\n"
                         f"🎬 code 021 - Shutter Island\n"
                         f"🎬 code 022 - Rocky II\n"
                         f"🎬 code 023 - World War Z\n"
                         f"🎬 code 024 - The Terminator\n"
                         f"🎬 code 025 - Ted 2\n"
                         f"🎬 code 026 - Baywatch\n"
                         f"🎬 code 027 - Deadpool & Wolverine\n"
                         f"🎬 code 028 - GoodFellas\n"
                         f"🎬 code 029 - Hercules in New York\n"
                         f"🎬 code 030 - Once Upon a Time in... Hollywood\n"
                         f"🎬 code 031 - Jing wu men\n"
                         f"🎬 code 032 - Central Intelligence\n"
                         f"🎬 code 033 - Grown Ups\n"
                         f"🎬 code 034 - Scream\n"
                         f"🎬 code 035 - Breaking Bad\n"
                         f"🎬 code 036 - American Psycho\n"
                         f"🎬 code 037 - Superbad\n"
                         f"🎬 code 038 - Borat\n"
                         f"🎬 code 039 - Dumb and Dumber\n"
                         f"🎬 code 040 - The Mask\n"
                         f"🎬 code 041 - The Founder\n"
                         f"🎬 code 042 - We're the Millers\n"
                         f"🎬 code 043 - Rocky III\n"
                         f"🎬 code 044 - Creed\n"
                         f"🎬 code 045 - Rambo\n"
                         f"🎬 code 046 - Death Race\n"
                         f"🎬 code 047 - Oppenheimer\n"
                         f"🎬 code 048 - Meet the Fockers\n"
                         f"🎬 code 049 - American Pie\n"
                         f"🎬 code 050 - Grown Ups 2\n"
                         f"-----------------------------------🗿-----------------------------------\n"
                         f"To find a movie, you need to write 001 or 002 after the start command")

# функія для пошуку фільму
@dp.message()
async def movie_handler(message: Message):
    # if message.text.startswith("/"):
    #     return

    code = message.text.strip()

    if code in MOVIE_CODES:
        imdb_id = MOVIE_CODES[code]
        movie_data = await get_movie_info(imdb_id)

        if movie_data.get("Response") == "True":
            response_text = (f"🎬 *{movie_data['Title']}* ({movie_data['Year']})\n"
                             f"⭐️ Rating: {movie_data['imdbRating']}\n"
                             f"📜 {movie_data['Plot']}")

            hero_button_keyboard = MOVIE_HEROES_BUTTONS.get(code, None)

            await message.answer_photo(photo=movie_data['Poster'], caption=response_text, parse_mode="Markdown", reply_markup=hero_button_keyboard)
        else:
            await message.answer("Movie could not be found. Try again!")
    else:
        await message.answer("Unknown code. Please enter the correct movie code (eg 001).")

# функція для обробки кнопки Back
@dp.callback_query()
async def hero_list_callback(callback: CallbackQuery):
    callback_data = callback.data  # callback_data

    if callback_data.startswith("show_heroes_"):
        movie_code = callback_data.split("_")[-1]  # Отримуємо код фільму
        hero_keyboard = MOVIE_HEROES.get(movie_code, None)

        if hero_keyboard:

            await callback.message.edit_caption("🦸 Here are the main characters of the film:", reply_markup=hero_keyboard)
        await callback.answer()

    elif callback_data.startswith("back_"):
        movie_code = callback_data.split("_")[-1]  # Отримуємо код фільму
        imdb_id = MOVIE_CODES.get(movie_code)

        if imdb_id:
            movie_data = await get_movie_info(imdb_id)
            response_text = (f"🎬 *{movie_data['Title']}* ({movie_data['Year']})\n"
                             f"⭐️ Rating: {movie_data['imdbRating']}\n"
                             f"📜 {movie_data['Plot']}")

            hero_button_keyboard = MOVIE_HEROES_BUTTONS.get(movie_code, None)

            await callback.message.edit_caption(response_text, parse_mode="Markdown", reply_markup=hero_button_keyboard)
        await callback.answer()


async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Бот перестав працювати')