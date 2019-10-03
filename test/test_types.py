import sys

sys.path.append('../')

from bot import types


def test_User_de_json():
    json_string = r'''{"id": 101234567, "first_name": "Testy",
"username": "testy_bot", "is_bot": true}'''

    u = types.User.de_json(json_string)
    assert u.id == 101234567


def test_Chat_de_json():
    json_string = r'''{"id": -111111,"title": "Test Title","type": "group",
"photo": {"small_file_id": "123456", "big_file_id": "654321"}}'''

    chat = types.Chat.de_json(json_string)
    assert chat.photo is not None
    assert chat.photo.small_file_id == '123456'


def test_Message_reply_de_json():
    json_string = r'''{"message_id":1,"from":{"id":108929734,
"first_name":"Frank","last_name":"Wang","username":"eternnoir","is_bot":true},
"chat":{"id":1734,"first_name":"F","type":"private",
"last_name":"Wa","username":"oir"},"date":1435296025,"text":"HIHI",
"reply_to_message":{"message_id":2,"from":{"id":108929734,
"first_name":"Frank","last_name":"Wang","username":"eternnoir","is_bot":true},
"chat":{"id":1734,"first_name":"F","type":"private",
"last_name":"Wa","username":"oir"},"date":1435296025,"text":"HIHI"}}'''

    message = types.Message.de_json(json_string)
    assert message.reply_to_message.message_id == 2


def test_Message_Entities_de_json():
    json_string = r'''{"message_id":1,"from":{"id":108929734,
"first_name":"Frank","last_name":"Wang","username":"eternnoir","is_bot":true},
"chat":{"id":1734,"first_name":"F","type":"private",
"last_name":"Wa","username":"oir"},"date":1435296025,"text":"HIHI",
"entities": [{"type":"hashtag","offset":1,"length":2},
{"type":"hashtag","offset":4,"length":2}]}'''

    message = types.Message.de_json(json_string)
    assert len(message.entities) == 2
    assert message.entities[1].offset == 4


def test_UserProfilePhotos_de_json():
    json_string = r'''{"total_count": 2,
"photos": [[{"file_id":"1234","width":100,"height":100}],
[{"file_id":"1234","width":100,"height":100}]]}'''
    user_photos = types.UserProfilePhotos.de_json(json_string)
    assert len(user_photos.photos) == 2
    assert len(user_photos.photos[0]) == 1
    assert user_photos.photos[0][0].file_id == '1234'
