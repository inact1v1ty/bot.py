import typing
from typing import Optional as o


class UpdateType:
    def __init__(

    ) -> None: ...


class User:
    def __init__(
        id: int,
        is_bot: bool,
        first_name: str,
        last_name: o[str] = None,
        username: o[str] = None,
        language_code: o[str] = None
    ) -> None: ...


class ChatPhoto:
    def __init__(
        small_file_id: str,
        big_file_id: str
    ) -> None: ...


class ChatMember:
    def __init__(
        user: User,
        status: str,
        until_date: o[int] = None,
        can_be_edited: o[bool] = None,
        can_post_messages: o[bool] = None,
        can_edit_messages: o[bool] = None,
        can_delete_messages: o[bool] = None,
        can_restrict_members: o[bool] = None,
        can_promote_members: o[bool] = None,
        can_change_info: o[bool] = None,
        can_invite_users: o[bool] = None,
        can_pin_messages: o[bool] = None,
        is_member: o[bool] = None,
        can_send_messages: o[bool] = None,
        can_send_media_messages: o[bool] = None,
        can_send_polls: o[bool] = None,
        can_send_other_messages: o[bool] = None,
        can_add_web_page_previews: o[bool] = None
    ) -> None: ...


class ChatPermissions:
    def __init__(
        can_send_messages: o[bool] = None,
        can_send_media_messages: o[bool] = None,
        can_send_polls: o[bool] = None,
        can_send_other_messages: o[bool] = None,
        can_add_web_page_previews: o[bool] = None,
        can_change_info: o[bool] = None,
        can_invite_users: o[bool] = None,
        can_pin_messages: o[bool] = None
    ) -> None: ...


class Chat:
    def __init__(
        id: int,
        type: str,
        title: o[str] = None,
        username: o[str] = None,
        first_name: o[str] = None,
        last_name: o[str] = None,
        photo: o[ChatPhoto] = None,
        description: o[str] = None,
        invite_link: o[str] = None,
        pinned_message: o[str] = None,
        permissions: o[str] = None,
        sticker_set_name: o[str] = None,
        can_set_sticker_set: o[bool] = None
    ) -> None: ...


class MessageEntity:
    def __init__(
        type: str,
        offset: int,
        length: int,
        url: o[int] = None,
        user: o[User] = None
    ) -> None: ...


class PhotoSize:
    def __init__(
        file_id: str,
        width: int,
        height: int,
        file_size: o[int] = None
    ) -> None: ...


class Audio:
    def __init__(
        file_id: str,
        duration: int,
        performer: o[str] = None,
        title: o[str] = None,
        mime_type: o[str] = None,
        file_size: o[int] = None,
        thumb: o[PhotoSize] = None
    ) -> None: ...


class Document:
    def __init__(
        file_id: str,
        thumb: o[PhotoSize] = None,
        file_name: o[str] = None,
        mime_type: o[str] = None,
        file_size: o[int] = None
    ) -> None: ...


class Video:
    def __init__(
        file_id: str,
        width: int,
        height: int,
        duration: int,
        thumb: o[PhotoSize] = None,
        mime_type: o[str] = None,
        file_size: o[int] = None
    ) -> None: ...


class Animation:
    def __init__(
        file_id: str,
        width: int,
        height: int,
        duration: int,
        thumb: o[PhotoSize] = None,
        file_name: o[str] = None,
        mime_type: o[str] = None,
        file_size: o[int] = None
    ) -> None: ...


class Voice:
    def __init__(
        file_id: str,
        duration: int,
        mime_type: o[str] = None,
        file_size: o[int] = None
    ) -> None: ...


class VideoNote:
    def __init__(
        file_id: str,
        length: int,
        duration: int,
        thumb: o[PhotoSize] = None,
        file_size: o[int] = None
    ) -> None: ...


class Contact:
    def __init__(
        phone_number: str,
        first_name: str,
        last_name: o[str] = None,
        user_id: o[int] = None,
        vcard: o[str] = None
    ) -> None: ...


class Location:
    def __init__(
        longitude: float,
        latitude: float
    ) -> None: ...


class Venue:
    def __init__(
        location: Location,
        title: str,
        address: str,
        foursquare_id: o[str] = None,
        foursquare_type: o[str] = None
    ) -> None: ...


class PollOption:
    def __init__(
        text: str,
        voter_count: int
    ) -> None: ...


class Poll:
    def __init__(
        id: str,
        question: str,
        options: typing.List[PollOption],
        is_closed: bool
    ) -> None: ...


class LoginUrl:
    def __init__(
        url: str,
        forward_text: o[str] = None,
        bot_username: o[str] = None,
        request_write_access: o[bool] = None
    ) -> None: ...


class CallbackGame:
    def __init__(

    ) -> None: ...


class InlineKeyboardButton:
    def __init__(
        text: str,
        url: o[str] = None,
        login_url: o[LoginUrl] = None,
        callback_data: o[str] = None,
        switch_inline_query: o[str] = None,
        switch_inline_query_current_chat: o[str] = None,
        callback_game: o[CallbackGame] = None,
        pay: o[bool] = None
    ) -> None: ...


class InlineKeyboardMarkup:
    def __init__(
        inline_keyboard: typing.List[typing.List[InlineKeyboardButton]] = None
    ) -> None: ...


class Message:
    def __init__(
        message_id: int,
        from_user: User,
        date: int,
        chat: Chat,
        forward_from: o[str] = None,
        forward_from_chat: o[Chat] = None,
        forward_from_message_id: o[int] = None,
        forward_signature: o[str] = None,
        forward_sender_name: o[str] = None,
        forward_date: o[int] = None
    ) -> None: ...


class UserProfilePhotos:
    def __init__(
        total_count: int,
        photos: typing.List[typing.List[PhotoSize]] = None
    ) -> None: ...


class File:
    def __init__(
        file_id: str,
        file_size: o[int] = None,
        file_path: o[str] = None
    ) -> None: ...


class KeyboardButton:
    def __init__(
        text: str,
        request_contact: o[bool] = None,
        request_location: o[bool] = None
    ) -> None: ...


class ReplyKeyboardMarkup:
    def __init__(
        keyboard: typing.List[typing.List[KeyboardButton]] = None,
        resize_keyboard: o[bool] = None,
        one_time_keyboard: o[bool] = None,
        selective: o[bool] = None
    ) -> None: ...


class CallbackQuery:
    def __init__(
        id: str,
        from_user: User,
        chat_instance: str,
        message: o[Message] = None,
        inline_message_id: o[str] = None,
        data: o[str] = None,
        game_short_name: o[str] = None
    ) -> None: ...


class ForceReply:
    def __init__(
        force_reply: bool,
        selective: o[bool] = None
    ) -> None: ...


class ResponseParameters:
    def __init__(
        migrate_to_chat_id: o[int] = None,
        retry_after: o[int] = None
    ) -> None: ...


class InputMedia:
    def __init__(

    ) -> None: ...


class InputMediaPhoto:
    def __init__(
        media: str,
        caption: o[str] = None,
        parse_mode: o[str] = None,
        type: str = 'photo'
    ) -> None: ...


class InputMediaVideo:
    def __init__(
        media: str,
        thumb: o[str] = None,
        caption: o[str] = None,
        parse_mode: o[str] = None,
        width: o[int] = None,
        height: o[int] = None,
        duration: o[int] = None,
        supports_streaming: o[bool] = None,
        type: str = 'video'
    ) -> None: ...


class InputMediaAnimation:
    def __init__(
        media: str,
        thumb: o[str] = None,
        caption: o[str] = None,
        parse_mode: o[str] = None,
        width: o[int] = None,
        height: o[int] = None,
        duration: o[int] = None,
        type: str = 'animation'
    ) -> None: ...


class InputMediaAudio:
    def __init__(
        media: str,
        thumb: o[str] = None,
        caption: o[str] = None,
        parse_mode: o[str] = None,
        duration: o[int] = None,
        performer: o[str] = None,
        title: o[str] = None,
        type: str = 'audio'
    ) -> None: ...


class InputMediaDocument:
    def __init__(
        media: str,
        thumb: o[str] = None,
        caption: o[str] = None,
        parse_mode: o[str] = None,
        type: str = 'document'
    ) -> None: ...


class InlineQuery:
    def __init__(
        id: str,
        from_user: User,
        query: str,
        offset: str,
        location: o[Location] = None
    ) -> None: ...


class InputMessageContent:
    def __init__(

    ) -> None: ...


class InputTextMessageContent:
    def __init__(
        message_text: str,
        parse_mode: o[str] = None,
        disable_web_page_preview: o[bool] = None
    ) -> None: ...


class InputLocationMessageContent:
    def __init__(
        latitude: float,
        longitude: float,
        live_period: o[int] = None
    ) -> None: ...


class InputVenueMessageContent:
    def __init__(
        latitude: float,
        longitude: float,
        title: str,
        address: str,
        foursquare_id: o[str] = None,
        foursquare_type: o[str] = None
    ) -> None: ...


class InputContactMessageContent:
    def __init__(
        phone_number: str,
        first_name: str,
        last_name: o[str] = None,
        vcard: o[str] = None
    ) -> None: ...


class InlineQueryResult:
    def __init__(

    ) -> None: ...


class InlineQueryResultArticle:
    def __init__(
        id: str,
        title: str,
        input_message_content: InputMessageContent,
        reply_markup: o[InlineKeyboardMarkup] = None,
        url: o[str] = None,
        hide_url: o[bool] = None,
        description: o[str] = None,
        thumb_url: o[str] = None,
        thumb_width: o[int] = None,
        thumb_height: o[int] = None,
        type: str = 'article'
    ) -> None: ...


class InlineQueryResultPhoto:
    def __init__(
        id: str,
        photo_url: str,
        thumb_url: str,
        photo_width: o[int] = None,
        photo_height: o[int] = None,
        title: o[str] = None,
        description: o[str] = None,
        caption: o[str] = None,
        parse_mode: o[str] = None,
        reply_markup: o[InlineKeyboardMarkup] = None,
        input_message_content: o[InputMessageContent] = None,
        type: str = 'photo'
    ) -> None: ...


class InlineQueryResultCachedAudio:
    def __init__(
        id: str,
        audio_file_id: str,
        caption: o[str] = None,
        parse_mode: o[str] = None,
        reply_markup: o[InlineKeyboardMarkup] = None,
        input_message_content: o[InputMessageContent] = None,
        type: str = 'audio'
    ) -> None: ...


class Update:
    def __init__(
        update_id: int,
        message: o[Message] = None,
        edited_message: o[Message] = None,
        channel_post: o[Message] = None,
        edited_channel_post: o[Message] = None,
        inline_query: o[InlineQuery] = None
    ) -> None: ...


class WebhookInfo:
    def __init__(
        url: str,
        has_custom_certificate: bool,
        pending_update_count: int,
        last_error_date: o[int] = None,
        last_error_message: o[str] = None,
        max_connections: o[int] = None,
        allowed_updates: typing.List[str] = None
    ) -> None: ...
