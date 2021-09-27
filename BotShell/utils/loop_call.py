import asyncio
import aioschedule
from ..utils.dbcommands import clear24h_watches, clear7d_watches, clear1m_watches


async def clear24h():
    await clear24h_watches()


async def clear7d():
    await clear7d_watches()


async def clear1m():
    await clear1m_watches()


async def scheduler():
    aioschedule.every().days.at("10:00").do(clear24h)
    aioschedule.every(7).days.at("10:00").do(clear7d)
    aioschedule.every(30).days.at("10:00").do(clear1m)
    while True:
        await aioschedule.run_pending()
        await asyncio.sleep(1)
