from json import loads
from urllib.request import urlopen
from urllib.error import HTTPError


def getData(username: str) -> tuple[dict | None, str]:
    url = f"https://api.github.com/users/{username}/events"
    try:
        res = urlopen(url)
    except HTTPError:
        return (None, "Data not fetched successfully")
    raw_bytes = res.read()
    text = raw_bytes.decode("utf-8")
    data = loads(text)
    return (data, "Data fetched successfully")
