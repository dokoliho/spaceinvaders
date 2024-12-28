import asyncio
import src.space_invaders

WIDTH = 640
HEIGHT = 400
SIZE = (WIDTH, HEIGHT)

async def main():
    game = src.space_invaders.SpaceInvaders("Space Invaders", size=SIZE)
    await game.run()

asyncio.run(main())