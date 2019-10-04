import attr
import typing


class ApiException(Exception):
    """
    This class represents an Exception thrown
    when a call to the Telegram API fails.
    In addition to an informative message,
    it has a `function_name` attribute which
    contains the name of the failed function
    and a `result` attribute that contains
    the returned result.
    failed.
    """

    def __init__(self, msg: str, function_name: str, result):
        super(ApiException, self).__init__(
            "A request to the Telegram API was unsuccessful. {0}".format(msg)
        )
        self.function_name: str = function_name
        self.result = result


@attr.s(auto_attribs=True)
class Handler(object):
    function: typing.Callable


def attr_filter(a: attr.Attribute, value):
    return value is not None


def get_dict(data):
    if attr.has(data):
        return attr.asdict(data, recurse=True, filter=attr_filter)
    elif type(data) == list:
        res = []
        for item in data:
            res.append(get_dict(item))
        return res
    else:
        return data


def get_payload(**kwargs):
    payload = {}

    for key, value in kwargs.items():
        if value is not None:
            payload[key] = get_dict(value)

    return payload
