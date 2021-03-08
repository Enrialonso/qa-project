import os

from utils.api_tmdb import ApiTmdb
from utils.dynamo_db.dynamo_db import CacheModel


class Cache:
    @staticmethod
    def search(cache_key: str, requests_attr: str, kwargs: dict) -> dict:
        try:
            item = CacheModel.get(cache_key)
            return item.data
        except CacheModel.DoesNotExist:
            api = ApiTmdb(api_key=os.getenv("API_KEY"))
            response = getattr(api, requests_attr)(**kwargs)
            cache = CacheModel(cache_key)
            cache.data = response
            cache.save()
            return response
