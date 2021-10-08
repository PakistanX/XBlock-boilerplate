from json import JSONEncoder
from datetime import datetime
from webob import Response


def json_response(payload):
    """
    This function converts dictionary to json http response object.
    :param payload: dict
    :return: Response
    """
    class CustomJSONEncoder(JSONEncoder):
        def default(self, o):
            if isinstance(o, datetime.date):
                return dict(year=o.year, month=o.month, day=o.day)
            return o.__dict__
    return Response(CustomJSONEncoder().encode(payload), content_type='application/json', charset='UTF-8')
