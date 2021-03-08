import logging

from utils.cache.cache import Cache
from utils.utils import build_response


def search_movie(event, context):
    try:
        logging.info("Search Movie start")
        query = event["pathParameters"].get("query")
        res = Cache.search(query, "search_movie", {"query": query})
        logging.info("Search Movie end")
        return build_response(status_code=200, body=res)
    except Exception as error:
        logging.error(f"ERROR: {error}")
        return build_response(
            status_code=500, body={"error": True, "message": "server error"}
        )
