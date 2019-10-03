import aiohttp
import json

from .util import ApiException

from . import types

API_URL = "https://api.telegram.org/bot{0}/{1}"


class Bot(object):
    def __init__(self, token: str):
        self.session: aiohttp.ClientSession = aiohttp.ClientSession()
        self.token: str = token

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.session.close()
        if exc_val:
            raise

    async def close(self):
        await self.session.close()

    async def _make_request(self,
                            method_name: str,
                            payload: dict = None,
                            url: str = API_URL) -> dict:
        data = json.dumps(payload)
        request_url = url.format(self.token, method_name)

        timeout = aiohttp.ClientTimeout(total=10)

        async with self.session.post(request_url,
                                     data=data,
                                     proxy='http://51.15.38.26:3128',
                                     timeout=timeout) as resp:
            text = await resp.text()
            if resp.status != 200:
                msg = 'The API returned HTTP {0} {1}. Response body:\n[{2}]' \
                    .format(resp.status, resp.reason, text)
                raise ApiException(msg, method_name, resp)

            try:
                json_data = json.loads(text)
            except Exception:
                msg = 'The API returned an invalid JSON response. ' + \
                    'Response body:\n[{0}]'.format(text)
                raise ApiException(msg, method_name, resp)

            if not json_data['ok']:
                msg = 'API request was unsuccesful.\n' + \
                    'Error code: {0} Description: {1}' \
                    .format(json_data['error_code'], json_data['description'])
                raise ApiException(msg, method_name, resp)

            return json_data['result']

    async def get_me(self) -> types.User:
        return types.User.de_json(await self._make_request('getMe'))
