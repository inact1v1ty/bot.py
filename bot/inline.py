import attr
from typing import Optional as o
from types import (
    DeJson, User, Location, InlineKeyboardMarkup
)


@attr.s(auto_attribs=True)
class InlineQuery(DeJson):
    id: str
    from_user: User = attr.ib(converter=User.de_json)
    query: str
    offset: str
    location: o[Location] = attr.ib(default=None, converter=Location.de_json)


@attr.s(auto_attribs=True)
class InputMessageContent(object):
    pass


@attr.s(auto_attribs=True)
class InputTextMessageContent(object):
    message_text: str
    parse_mode: o[str] = None
    disable_web_page_preview: o[bool] = None


@attr.s(auto_attribs=True)
class InputLocationMessageContent(object):
    latitude: float
    longitude: float
    live_period: o[int] = None


@attr.s(auto_attribs=True)
class InputVenueMessageContent(object):
    latitude: float
    longitude: float
    title: str
    address: str
    foursquare_id: o[str] = None
    foursquare_type: o[str] = None


@attr.s(auto_attribs=True)
class InputContactMessageContent(object):
    phone_number: str
    first_name: str
    last_name: o[str] = None
    vcard: o[str] = None


@attr.s(auto_attribs=True)
class InlineQueryResult(object):
    pass


@attr.s(auto_attribs=True)
class InlineQueryResultArticle(InlineQueryResult):
    id: str
    title: str
    input_message_content: InputMessageContent
    reply_markup: o[InlineKeyboardMarkup] = None
    url: o[str] = None
    hide_url: o[bool] = None
    description: o[str] = None
    thumb_url: o[str] = None
    thumb_width: o[int] = None
    thumb_height: o[int] = None
    type: str = 'article'


@attr.s(auto_attribs=True)
class InlineQueryResultPhoto(InlineQueryResult):
    id: str
    photo_url: str
    thumb_url: str
    photo_width: o[int] = None
    photo_height: o[int] = None
    title: o[str] = None
    description: o[str] = None
    caption: o[str] = None
    parse_mode: o[str] = None
    reply_markup: o[InlineKeyboardMarkup] = None
    input_message_content: o[InputMessageContent] = None
    type: str = 'photo'


@attr.s(auto_attribs=True)
class InlineQueryResultCachedAudio(InlineQueryResult):
    id: str
    audio_file_id: str
    caption: o[str] = None
    parse_mode: o[str] = None
    reply_markup: o[InlineKeyboardMarkup] = None
    input_message_content: o[InputMessageContent] = None
    type: str = 'audio'
