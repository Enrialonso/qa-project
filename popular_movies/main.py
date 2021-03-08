import logging

from utils.cache.cache import Cache
from utils.utils import build_response


def popular_movies(event, context):
    try:
        logging.info("Popular Movie start")
        res = Cache.search('popular-movies', 'popular_movies', {})
        logging.info("Popular Movie end")
        return build_response(status_code=200, body=res)
    except Exception as error:
        logging.error(f"ERROR: {error}")
        return build_response(status_code=500, body={"error": True, "message": "server error"})
