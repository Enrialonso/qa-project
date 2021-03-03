import logging
import os
import sys

from utils.api_tmdb import ApiTmdb
from utils.utils import build_response

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)


def search_movie(event, context):
    try:
        logging.info("Search Movie start")
        query = event["pathParameters"].get("query")
        api = ApiTmdb(api_key=os.getenv("API_KEY"))
        res = api.search_movie(query)
        logging.info("Search Movie end")
        return build_response(status_code=200, body=res)
    except Exception as error:
        logging.error(f"ERROR: {error}")
        return build_response(
            status_code=500, body={"error": True, "message": "server error"}
        )
