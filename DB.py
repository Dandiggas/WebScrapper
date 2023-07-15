import asyncio
from prisma import Prisma


async def main() -> None:
    db = Prisma()
    await db.connect()
    await db.user.find_first()

    await db.disconnect()


if __name__ == '__main__':
    asyncio.run(main())