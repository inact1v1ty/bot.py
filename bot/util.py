
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
