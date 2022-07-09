import asyncio
import random

import aiohttp

# import httpx
# import requests

BASE_URL = "https://pokeapi.co/api/v2/pokemon/"
MAX_POKEMON = 400


# def get_random_id() -> str:
#     random_id = random.randint(1, MAX_POKEMON + 1)
#     return str(random_id)


# async def get_pokemon_async(id_: str) -> str:
#     url = BASE_URL + id_
#     async with aiohttp.ClientSession(trust_env=True) as session:
#         async with session.get(url, ssl=False) as resp:
#             resp_json = await resp.json()
#             return resp_json["name"]


# async def get_random_pokemon_async() -> str:
#     random_id = get_random_id()
#     return await get_pokemon_async(random_id)


# async def main():
#     tasks = [get_random_pokemon_async() for _ in range(SIZE)]
#     random_pokemons = await asyncio.gather(*tasks)
#     print(f"Pokemons: {random_pokemons}")


# asyncio.run(main())


def get_random_id() -> str:
    random_id = random.randint(1, MAX_POKEMON)
    return str(random_id)


async def get_random_pokemon() -> str:
    url = BASE_URL + get_random_id()
    async with aiohttp.ClientSession(trust_env=True) as session:
        async with session.get(url, ssl=False) as resp:
            resp_json = await resp.json()
            return resp_json["name"]


async def main():
    tasks = [get_random_pokemon() for _ in range(100)]
    results = await asyncio.gather(*tasks)
    print(results)


asyncio.run(main())
