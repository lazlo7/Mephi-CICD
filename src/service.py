from random import choice
from asyncio import sleep

# Some business logic here...

BERRIES = [
    "blueberry",
    "strawberry",
    "cranberry",
    "blackberry",
    "raspberry"
]


async def get_random_berry() -> str:
    # Simulate some actual computation.
    await sleep(0.5)
    return choice(BERRIES)


async def calculate_some_value(x: int) -> int:
    return x + 123
