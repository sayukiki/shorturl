import os
import asyncio
import aioredis
from asgiref.sync import async_to_sync, sync_to_async

redis = async_to_sync(aioredis.create_redis_pool)(
    ('database', 6379),
    encoding='utf-8',
    db=0,
    minsize=int(os.environ['POOL_MIN_SIZE']),
    maxsize=int(os.environ['POOL_MAX_SIZE'])
)