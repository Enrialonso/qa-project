import requests


class ApiTmdb:
    def __init__(self, api_key: str, language: str = "en-US"):
        self.__api_base_url = "https://api.themoviedb.org/3/%s"
        self.__api_key = api_key
        self.__language = language
        self.include_adult = False

    def popular_movies(self):
        endpoint = "movie/popular"
        url = self.__api_base_url % endpoint
        params = {
            "api_key": self.__api_key,
            "language": self.__language,
            "include_adult": self.include_adult,
        }
        res = requests.get(url, params=params)
        if res.ok:
            return res.json()
        else:
            raise Exception(f"ERROR: http error: {res.status_code}")

    def search_movie(self, query: str) -> dict:
        endpoint = "search/movie"
        url = self.__api_base_url % endpoint
        params = {
            "api_key": self.__api_key,
            "language": self.__language,
            "include_adult": self.include_adult,
            "query": query,
        }
        res = requests.get(url, params=params)
        if res.ok:
            return res.json()
        else:
            raise Exception(f"ERROR: http error: {res.status_code}")
