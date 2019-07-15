from abc import ABC
from requests import session
from api_auth_provider import session as s


class EndpointFetcher(ABC):
    base_api_url = 'https://api.hitbtc.com/api/2'

    def __init__(self, url: str, auth: session):
        pass

    def _fetch_url(self):
        pass

    async def normalize(self):
        pass


class TransactionsFetcher(EndpointFetcher):
    @staticmethod
    def _to_chunks(iterable: list):
        yield from iterable

    def __init__(self, method: str, normalization_rules: dict, uri: str, auth: session = s, *args, **kwargs):
        self._auth = auth
        self._method = method
        self._url = self.base_api_url + uri
        self._normalization_rules = normalization_rules

    def _fetch_url(self) -> list:
        res = self._auth.request(self._method, self._url)
        res.raise_for_status()
        return res.json()

    def normalize(self):
        res = []
        for each in self._to_chunks(self._fetch_url()):
            r = {}
            for i in self._normalization_rules.keys():
                val = self._normalization_rules.get(i)
                r.update({i: each.get(val, "ERROR - CHECK SCHEMA") if not isinstance(val, dict) else val['default']})
            res.append(r)
        return res
