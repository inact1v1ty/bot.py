import aiohttp
import json

import typing
from typing import Optional as o

from .util import ApiException, get_payload, Handler

from . import types

API_URL = "https://api.telegram.org/bot{0}/{1}"


TFunc = typing.Callable[[types.Message], None]


class Bot(object):
    def __init__(self, token: str):
        self.session: aiohttp.ClientSession = aiohttp.ClientSession()
        self.token: str = token
        self.last_update_id = 0
        self.message_handlers = []
        self.edited_message_handlers = []
        self.channel_post_handlers = []
        self.edited_channel_post_handlers = []
        self.inline_query_handlers = []
        self.chosen_inline_result_handlers = []
        self.callback_query_handlers = []
        self.shipping_query_handlers = []
        self.pre_checkout_query_handlers = []
        self.poll_state_handlers = []

    async def __aenter__(self) -> 'Bot':
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb) -> None:
        await self.session.close()
        if exc_val:
            raise

    async def close(self) -> None:
        await self.session.close()

    async def _make_request(self,
                            method_name: str,
                            payload: dict = None,
                            url: str = API_URL) -> dict:
        request_url = url.format(self.token, method_name)

        timeout = aiohttp.ClientTimeout(total=10)

        async with self.session.post(request_url,
                                     json=payload,
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

    async def polling(self, timeout: int = 10):
        while True:
            await self._retrieve_updates(timeout)

    async def _retrieve_updates(self, timeout: int = 10):
        updates = await self.get_updates(
            offset=(self.last_update_id + 1), timeout=timeout
        )
        await self.process_new_updates(updates)

    async def _run_handlers(self,
                            handlers: typing.List[Handler],
                            updates: typing.List[types.UpdateType]):
        for update in updates:
            if len(handlers) > 0:
                await handlers[0].function(update)

    def message_handler(self):
        def decorator(handler):
            self.message_handlers.append(Handler(handler))
            return handler
        return decorator

    def edited_message_handler(self):
        def decorator(handler):
            self.edited_message_handlers.append(Handler(handler))
            return handler
        return decorator

    def channel_post_handler(self):
        def decorator(handler):
            self.channel_post_handlers.append(Handler(handler))
            return handler
        return decorator

    def edited_channel_post_handler(self):
        def decorator(handler):
            self.edited_channel_post_handlers.append(Handler(handler))
            return handler
        return decorator

    def inline_query_handler(self):
        def decorator(handler):
            self.inline_query_handlers.append(Handler(handler))
            return handler
        return decorator

    def chosen_inline_result_handler(self):
        def decorator(handler):
            self.chosen_inline_result_handlers.append(Handler(handler))
            return handler
        return decorator

    def callback_query_handler(self):
        def decorator(handler):
            self.callback_query_handlers.append(Handler(handler))
            return handler
        return decorator

    def shipping_query_handler(self):
        def decorator(handler):
            self.shipping_query_handlers.append(Handler(handler))
            return handler
        return decorator

    def pre_checkout_query_handler(self):
        def decorator(handler):
            self.pre_checkout_query_handlers.append(Handler(handler))
            return handler
        return decorator

    def poll_state_handler(self):
        def decorator(handler):
            self.poll_state_handlers.append(Handler(handler))
            return handler
        return decorator

    async def process_new_updates(self,
                                  updates: typing.List[types.Update]) -> None:
        new_messages = []
        new_edited_new_messages = []
        new_channel_posts = []
        new_edited_channel_posts = []
        new_inline_querys = []
        new_chosen_inline_results = []
        new_callback_querys = []
        new_shipping_querys = []
        new_pre_checkout_querys = []
        new_poll_states = []

        for update in updates:
            if update.update_id > self.last_update_id:
                self.last_update_id = update.update_id
            if update.message:
                new_messages.append(update.message)
            if update.edited_message:
                new_edited_new_messages.append(update.edited_message)
            if update.channel_post:
                new_channel_posts.append(update.channel_post)
            if update.edited_channel_post:
                new_edited_channel_posts.append(update.edited_channel_post)
            if update.inline_query:
                new_inline_querys.append(update.inline_query)
            if update.chosen_inline_result:
                new_chosen_inline_results.append(update.chosen_inline_result)
            if update.callback_query:
                new_callback_querys.append(update.callback_query)
            if update.shipping_query:
                new_shipping_querys.append(update.shipping_query)
            if update.pre_checkout_query:
                new_pre_checkout_querys.append(update.pre_checkout_query)
            if update.poll:
                new_poll_states.append(update.poll)

        if len(new_messages) > 0:
            await self.process_new_messages(new_messages)
        if len(new_edited_new_messages) > 0:
            await self.process_new_edited_messages(new_edited_new_messages)
        if len(new_channel_posts) > 0:
            await self.process_new_channel_posts(new_channel_posts)
        if len(new_edited_channel_posts) > 0:
            await self.process_new_edited_channel_posts(
                new_edited_channel_posts
            )
        if len(new_inline_querys) > 0:
            await self.process_new_inline_querys(new_inline_querys)
        if len(new_chosen_inline_results) > 0:
            await self.process_new_chosen_inline_querys(
                new_chosen_inline_results
            )
        if len(new_callback_querys) > 0:
            await self.process_new_callback_querys(new_callback_querys)
        if len(new_pre_checkout_querys) > 0:
            await self.process_new_pre_checkout_querys(new_pre_checkout_querys)
        if len(new_shipping_querys) > 0:
            await self.process_new_shipping_querys(new_shipping_querys)
        if len(new_poll_states) > 0:
            await self.process_new_poll_states(new_poll_states)

    async def process_new_messages(self, new_messages):
        await self._run_handlers(self.message_handlers,
                                 new_messages)

    async def process_new_edited_messages(self, new_edited_messages):
        await self._run_handlers(self.edited_message_handlers,
                                 new_edited_messages)

    async def process_new_channel_posts(self, new_channel_posts):
        await self._run_handlers(self.channel_post_handlers,
                                 new_channel_posts)

    async def process_new_edited_channel_posts(self, new_edited_channel_posts):
        await self._run_handlers(self.edited_channel_post_handlers,
                                 new_edited_channel_posts)

    async def process_new_inline_querys(self, new_inline_querys):
        await self._run_handlers(self.inline_query_handlers,
                                 new_inline_querys)

    async def process_new_chosen_inline_results(self,
                                                new_chosen_inline_results):
        await self._run_handlers(self.chosen_inline_result_handlers,
                                 new_chosen_inline_results)

    async def process_new_callback_querys(self, new_callback_querys):
        await self._run_handlers(self.callback_query_handlers,
                                 new_callback_querys)

    async def process_new_shipping_querys(self, new_shipping_querys):
        await self._run_handlers(self.shipping_query_handlers,
                                 new_shipping_querys)

    async def process_new_pre_checkout_querys(self, pre_checkout_querys):
        await self._run_handlers(self.pre_checkout_query_handlers,
                                 pre_checkout_querys)

    async def process_new_poll_states(self, new_poll_states):
        await self._run_handlers(self.poll_state_handlers,
                                 new_poll_states)

    async def get_me(self) -> types.User:
        return types.User.de_json(await self._make_request('getMe'))

    async def get_updates(self,
                          offset: o[int] = None,
                          limit: o[int] = None,
                          timeout: o[int] = None,
                          allowed_updates: typing.List[str] = None) \
            -> typing.List[types.Update]:

        payload = get_payload(
            offset=offset,
            limit=limit,
            timeout=timeout,
            allowed_updates=allowed_updates
        )

        return types.de_list(types.Update.de_json)(
            await self._make_request('getUpdates', payload)
        )

    async def answer_inline_query(
        self,
        inline_query_id: str,
        results: typing.List[types.InlineQueryResult],
        cache_time: o[int] = None,
        is_personal: o[bool] = None,
        next_offset: o[str] = None,
        switch_pm_text: o[str] = None,
        switch_pm_parameter: o[str] = None
    ) -> bool:
        payload = get_payload(
            inline_query_id=inline_query_id,
            results=results,
            cache_time=cache_time,
            is_personal=is_personal,
            next_offset=next_offset,
            switch_pm_text=switch_pm_text,
            switch_pm_parameter=switch_pm_parameter
        )

        print(payload)

        return await self._make_request('answerInlineQuery', payload)
