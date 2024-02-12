import asyncio
import aiohttp
import aiofiles
import json
import csv


async def get_data(url, session):
    async with session.get(url, allow_redirects=True) as response:
        data = await response.text()
        json_data = json.loads(data)
        last_name, first_name, patronymic = json_data["name"].split()
        csv_row = [last_name, first_name, patronymic,
                   json_data["company"], json_data["phone_w"],
                   json_data["phone_h"]]
        await write_to_file(csv_row)


async def start_session(number):
    url = "https://api.namefake.com/ukrainian-ukraine/male"
    tasks = []

    async with aiohttp.ClientSession() as session:
        for _ in range(number):
            task = asyncio.create_task(get_data(url, session))
            tasks.append(task)

        await asyncio.gather(*tasks)


async def write_to_file(csv_row):
    async with aiofiles.open("./phonebook_app/db/phone_book.csv", "a") as csv_file:
        writer = csv.writer(csv_file)
        await writer.writerow(csv_row)


def auto_complete_csv_file(number):
    asyncio.run(start_session(number))
