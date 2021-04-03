import functools
import json
from json.decoder import JSONDecodeError

from aiohttp.web_exceptions import HTTPBadRequest


def str_to_int(data: dict, field_name: str) -> int:
    try:
        return int(data[field_name])
    except (ValueError, TypeError):
        text = {
            f'{field_name}': f"can't transform to integer {data[field_name]} "
        }
        raise HTTPBadRequest(text=json.dumps(text))
    except IndexError:
        text = {
            f'{field_name}': 'field is required'
        }
        raise HTTPBadRequest(text=json.dumps(text))


def json_parse_exception(view):
    async def internal_func(*args, **kwargs):
        try:
            return await view(*args, **kwargs)
        except JSONDecodeError:
            raise HTTPBadRequest(text='Invalid JSON')
    return internal_func
