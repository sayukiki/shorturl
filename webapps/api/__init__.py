import asyncio
import aioredis
from asgiref.sync import async_to_sync, sync_to_async

redis = async_to_sync(aioredis.create_redis_pool)(('database', 6379), encoding='utf-8', db=0, minsize=1, maxsize=10)