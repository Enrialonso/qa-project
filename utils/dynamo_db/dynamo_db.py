import os
from time import time

from pynamodb.attributes import UnicodeAttribute, JSONAttribute, NumberAttribute
from pynamodb.models import Model


def default_ttl():
    return int(time() + int(os.getenv("DYNAMODB_TTL")))


class CacheModel(Model):
    class Meta:
        table_name = "CacheAPI"
        region = "eu-west-1"

    cache_key = UnicodeAttribute(hash_key=True, null=False, attr_name="cache_key")
    data = JSONAttribute(null=False, attr_name="data")
    TTL = NumberAttribute(null=False, default=default_ttl())
