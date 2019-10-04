# -*- coding: utf-8 -*-

import json
import attr
import typing
from typing import Optional as o


@attr.s()
class DeJson(object):
    @classmethod
    def de_json(cls, data):
        if data is None:
            return None
        if type(data) is str:
            data = json.loads(data)
        # Hack to fix 'from' key
        if 'from' in data:
            data['from_user'] = data['from']
            del data['from']
        return cls(**data)


def de_list(converter):
    def wrapped(data):
        if data is None:
            return None
        if type(data) is str:
            data = json.loads(data)
        res = []
        for d in data:
            res.append(converter(d))
        return res
    return wrapped


@attr.s(auto_attribs=True)
class UpdateType(DeJson):
    pass


@attr.s(auto_attribs=True)
class User(DeJson):
    id: int
    is_bot: bool
    first_name: str
    last_name: o[str] = None
    username: o[str] = None
    language_code: o[str] = None


@attr.s(auto_attribs=True)
class ChatPhoto(DeJson):
    small_file_id: str
    big_file_id: str


@attr.s(auto_attribs=True)
class ChatMember(DeJson):
    user: User = attr.ib(converter=User.de_json)
    status: str
    until_date: o[int] = None
    can_be_edited: o[bool] = None
    can_post_messages: o[bool] = None
    can_edit_messages: o[bool] = None
    can_delete_messages: o[bool] = None
    can_restrict_members: o[bool] = None
    can_promote_members: o[bool] = None
    can_change_info: o[bool] = None
    can_invite_users: o[bool] = None
    can_pin_messages: o[bool] = None
    is_member: o[bool] = None
    can_send_messages: o[bool] = None
    can_send_media_messages: o[bool] = None
    can_send_polls: o[bool] = None
    can_send_other_messages: o[bool] = None
    can_add_web_page_previews: o[bool] = None


@attr.s(auto_attribs=True)
class ChatPermissions(DeJson):
    can_send_messages: o[bool] = None
    can_send_media_messages: o[bool] = None
    can_send_polls: o[bool] = None
    can_send_other_messages: o[bool] = None
    can_add_web_page_previews: o[bool] = None
    can_change_info: o[bool] = None
    can_invite_users: o[bool] = None
    can_pin_messages: o[bool] = None


@attr.s(auto_attribs=True)
class Chat(DeJson):
    id: int
    type: str
    title: o[str] = None
    username: o[str] = None
    first_name: o[str] = None
    last_name: o[str] = None
    photo: o[ChatPhoto] = attr.ib(default=None, converter=ChatPhoto.de_json)
    description: o[str] = None
    invite_link: o[str] = None
    pinned_message: o[str] = None
    permissions: o[str] = None
    sticker_set_name: o[str] = None
    can_set_sticker_set: o[bool] = None


@attr.s(auto_attribs=True)
class MessageEntity(DeJson):
    type: str
    offset: int
    length: int
    url: o[int] = None
    user: o[User] = attr.ib(default=None, converter=User.de_json)


@attr.s(auto_attribs=True)
class PhotoSize(DeJson):
    file_id: str
    width: int
    height: int
    file_size: o[int] = None


@attr.s(auto_attribs=True)
class Audio(DeJson):
    file_id: str
    duration: int
    performer: o[str] = None
    title: o[str] = None
    mime_type: o[str] = None
    file_size: o[int] = None
    thumb: o[PhotoSize] = attr.ib(default=None, converter=PhotoSize.de_json)


@attr.s(auto_attribs=True)
class Document(DeJson):
    file_id: str
    thumb: o[PhotoSize] = attr.ib(default=None, converter=PhotoSize.de_json)
    file_name: o[str] = None
    mime_type: o[str] = None
    file_size: o[int] = None


@attr.s(auto_attribs=True)
class Video(DeJson):
    file_id: str
    width: int
    height: int
    duration: int
    thumb: o[PhotoSize] = attr.ib(default=None, converter=PhotoSize.de_json)
    mime_type: o[str] = None
    file_size: o[int] = None


@attr.s(auto_attribs=True)
class Animation(DeJson):
    file_id: str
    width: int
    height: int
    duration: int
    thumb: o[PhotoSize] = attr.ib(default=None, converter=PhotoSize.de_json)
    file_name: o[str] = None
    mime_type: o[str] = None
    file_size: o[int] = None


@attr.s(auto_attribs=True)
class Voice(DeJson):
    file_id: str
    duration: int
    mime_type: o[str] = None
    file_size: o[int] = None


@attr.s(auto_attribs=True)
class VideoNote(DeJson):
    file_id: str
    length: int
    duration: int
    thumb: o[PhotoSize] = attr.ib(default=None, converter=PhotoSize.de_json)
    file_size: o[int] = None


@attr.s(auto_attribs=True)
class Contact(DeJson):
    phone_number: str
    first_name: str
    last_name: o[str] = None
    user_id: o[int] = None
    vcard: o[str] = None


@attr.s(auto_attribs=True)
class Location(DeJson):
    longitude: float
    latitude: float


@attr.s(auto_attribs=True)
class Venue(DeJson):
    location: Location = attr.ib(converter=Location.de_json)
    title: str
    address: str
    foursquare_id: o[str] = None
    foursquare_type: o[str] = None


@attr.s(auto_attribs=True)
class PollOption(DeJson):
    text: str
    voter_count: int


@attr.s(auto_attribs=True)
class Poll(UpdateType):
    id: str
    question: str
    options: typing.List[PollOption] = attr.ib(
        converter=de_list(PollOption.de_json)
    )
    is_closed: bool


@attr.s(auto_attribs=True)
class LoginUrl(DeJson):
    url: str
    forward_text: o[str] = None
    bot_username: o[str] = None
    request_write_access: o[bool] = None


@attr.s(auto_attribs=True)
class CallbackGame(DeJson):
    pass


@attr.s(auto_attribs=True)
class InlineKeyboardButton(DeJson):
    text: str
    url: o[str] = None
    login_url: o[LoginUrl] = attr.ib(default=None, converter=LoginUrl.de_json)
    callback_data: o[str] = None
    switch_inline_query: o[str] = None
    switch_inline_query_current_chat: o[str] = None
    callback_game: o[CallbackGame] = attr.ib(
        default=None, converter=CallbackGame.de_json
    )
    pay: o[bool] = None


@attr.s(auto_attribs=True)
class InlineKeyboardMarkup(DeJson):
    inline_keyboard: typing.List[typing.List[InlineKeyboardButton]] = attr.ib(
        default=None, converter=de_list(de_list(InlineKeyboardButton.de_json))
    )


@attr.s(auto_attribs=True)
class Message(UpdateType):
    message_id: int
    from_user: User = attr.ib(converter=User.de_json)
    date: int
    chat: Chat = attr.ib(converter=Chat.de_json)
    forward_from: o[str] = None
    forward_from_chat: o[Chat] = attr.ib(default=None, converter=Chat.de_json)
    forward_from_message_id: o[int] = None
    forward_signature: o[str] = None
    forward_sender_name: o[str] = None
    forward_date: o[int] = None
    # Hack because Python don't see Message type here yet
    reply_to_message: o['Message'] = attr.ib(
        default=None, converter=lambda data: Message.de_json(data)
    )
    edit_date: o[int] = None
    media_group_id: o[str] = None
    author_signature: o[str] = None
    text: o[str] = None
    entities: typing.List[MessageEntity] = attr.ib(
        default=None, converter=de_list(MessageEntity.de_json)
    )
    caption_entities: typing.List[MessageEntity] = attr.ib(
        default=None, converter=de_list(MessageEntity.de_json)
    )
    audio: o[Audio] = attr.ib(default=None, converter=Audio.de_json)
    document: o[Document] = attr.ib(default=None, converter=Document.de_json)
    animation: o[Animation] = attr.ib(
        default=None, converter=Animation.de_json)
    game: o[str] = None
    photo: typing.List[PhotoSize] = attr.ib(
        default=None, converter=de_list(PhotoSize.de_json)
    )
    sticker: o[str] = None
    video: o[Video] = attr.ib(default=None, converter=Video.de_json)
    voice: o[Voice] = attr.ib(default=None, converter=Voice.de_json)
    video_note: o[VideoNote] = attr.ib(
        default=None, converter=VideoNote.de_json)
    caption: o[str] = None
    contact: o[Contact] = attr.ib(default=None, converter=Contact.de_json)
    location: o[Location] = attr.ib(default=None, converter=Location.de_json)
    venue: o[Venue] = attr.ib(default=None, converter=Venue.de_json)
    poll: o[Poll] = attr.ib(default=None, converter=Poll.de_json)
    new_chat_members: typing.List[User] = attr.ib(
        default=None, converter=de_list(User.de_json)
    )
    left_chat_member: o[User] = attr.ib(default=None, converter=User.de_json)
    new_chat_title: o[str] = None
    new_chat_photo: typing.List[PhotoSize] = attr.ib(
        default=None, converter=de_list(PhotoSize.de_json)
    )
    delete_chat_photo: o[bool] = None
    group_chat_created: o[bool] = None
    supergroup_chat_created: o[bool] = None
    channel_chat_created: o[bool] = None
    migrate_to_chat_id: o[int] = None
    migrate_from_chat_id: o[int] = None
    # Hack because Python don't see Message type here yet
    pinned_message: o['Message'] = attr.ib(
        default=None, converter=lambda data: Message.de_json(data)
    )
    invoice: o[str] = None
    succesful_payment: o[str] = None
    connected_website: o[str] = None
    passport_data: o[str] = None
    reply_markup: o[str] = None


@attr.s(auto_attribs=True)
class UserProfilePhotos(DeJson):
    total_count: int
    photos: typing.List[typing.List[PhotoSize]] = attr.ib(
        default=None, converter=de_list(de_list(PhotoSize.de_json))
    )


@attr.s(auto_attribs=True)
class File(DeJson):
    file_id: str
    file_size: o[int] = None
    file_path: o[str] = None


@attr.s(auto_attribs=True)
class KeyboardButton(DeJson):
    text: str
    request_contact: o[bool] = None
    request_location: o[bool] = None


@attr.s(auto_attribs=True)
class ReplyKeyboardMarkup(DeJson):
    keyboard: typing.List[typing.List[KeyboardButton]] = attr.ib(
        default=None, converter=de_list(de_list(KeyboardButton.de_json))
    )
    resize_keyboard: o[bool] = None
    one_time_keyboard: o[bool] = None
    selective: o[bool] = None


@attr.s(auto_attribs=True)
class CallbackQuery(UpdateType):
    id: str
    from_user: User = attr.ib(converter=User.de_json)
    chat_instance: str
    message: o[Message] = attr.ib(default=None, converter=Message.de_json)
    inline_message_id: o[str] = None
    data: o[str] = None
    game_short_name: o[str] = None


@attr.s(auto_attribs=True)
class ForceReply(DeJson):
    force_reply: bool
    selective: o[bool] = None


@attr.s(auto_attribs=True)
class ResponseParameters(DeJson):
    migrate_to_chat_id: o[int] = None
    retry_after: o[int] = None


@attr.s(auto_attribs=True)
class InputMedia(DeJson):
    pass


@attr.s(auto_attribs=True)
class InputMediaPhoto(InputMedia):
    media: str
    caption: o[str] = None
    parse_mode: o[str] = None
    type: str = 'photo'


@attr.s(auto_attribs=True)
class InputMediaVideo(InputMedia):
    media: str
    thumb: o[str] = None
    caption: o[str] = None
    parse_mode: o[str] = None
    width: o[int] = None
    height: o[int] = None
    duration: o[int] = None
    supports_streaming: o[bool] = None
    type: str = 'video'


@attr.s(auto_attribs=True)
class InputMediaAnimation(InputMedia):
    media: str
    thumb: o[str] = None
    caption: o[str] = None
    parse_mode: o[str] = None
    width: o[int] = None
    height: o[int] = None
    duration: o[int] = None
    type: str = 'animation'


@attr.s(auto_attribs=True)
class InputMediaAudio(InputMedia):
    media: str
    thumb: o[str] = None
    caption: o[str] = None
    parse_mode: o[str] = None
    duration: o[int] = None
    performer: o[str] = None
    title: o[str] = None
    type: str = 'audio'


@attr.s(auto_attribs=True)
class InputMediaDocument(InputMedia):
    media: str
    thumb: o[str] = None
    caption: o[str] = None
    parse_mode: o[str] = None
    type: str = 'document'


@attr.s(auto_attribs=True)
class InlineQuery(UpdateType):
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
class InlineQueryResultGame(InlineQueryResult):
    id: str
    game_short_name: str
    reply_markup: o[InlineKeyboardMarkup] = None
    type: str = 'game'


@attr.s(auto_attribs=True)
class InlineQueryResultCachedAudio(InlineQueryResult):
    id: str
    audio_file_id: str
    caption: o[str] = None
    parse_mode: o[str] = None
    reply_markup: o[InlineKeyboardMarkup] = None
    input_message_content: o[InputMessageContent] = None
    type: str = 'audio'


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
    chosen_inline_result: o[typing.Any] = attr.ib(
        default=None
    )
    callback_query: o[CallbackQuery] = attr.ib(
        default=None, converter=CallbackQuery.de_json
    )
    # shipping_query: o[ShippingQuery] = attr.ib(
    #    default=None, converter=ShippingQuery.de_json
    # )
    shipping_query: o[typing.Any] = attr.ib(
        default=None
    )
    # pre_checkout_query: o[PreCheckoutQuery] = attr.ib(
    #    default=None, converter=PreCheckoutQuery.de_json
    # )
    pre_checkout_query: o[typing.Any] = attr.ib(
        default=None
    )
    poll: o[Poll] = attr.ib(
        default=None, converter=Poll.de_json
    )


print(Update.__init__.__annotations__)


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
