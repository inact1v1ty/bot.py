import attr
import typing
from typing import Optional as o
from types import DeJson, Message, CallbackQuery, Poll, de_list
from inline import InlineQuery


@attr.s(auto_attribs=True)
class Update(DeJson):
    update_id: int
    message: o[Message] = attr.ib(
        default=None, converter=Message.de_json
    )
    edited_message: o[Message] = attr.ib(
        default=None, converter=Message.de_json
    )
    channel_post: o[Message] = attr.ib(
        default=None, converter=Message.de_json
    )
    edited_channel_post: o[Message] = attr.ib(
        default=None, converter=Message.de_json
    )
    inline_query: o[InlineQuery] = attr.ib(
        default=None, converter=InlineQuery.de_json
    )
    # chosen_inline_result: o[ChosenInlineResult] = attr.ib(
    #    default=None, converter=ChosenInlineResult.de_json
    # )
    callback_query: o[CallbackQuery] = attr.ib(
        default=None, converter=CallbackQuery.de_json
    )
    # shipping_query: o[ShippingQuery] = attr.ib(
    #    default=None, converter=ShippingQuery.de_json
    # )
    # pre_checkout_query: o[PreCheckoutQuery] = attr.ib(
    #    default=None, converter=PreCheckoutQuery.de_json
    # )
    poll: o[Poll] = attr.ib(
        default=None, converter=Poll.de_json
    )


@attr.s(auto_attribs=True)
class WebhookInfo(DeJson):
    url: str
    has_custom_certificate: bool
    pending_update_count: int
    last_error_date: o[int] = None
    last_error_message: o[str] = None
    max_connections: o[int] = None
    allowed_updates: typing.List[str] = attr.ib(
        default=None, converter=de_list(str)
    )
