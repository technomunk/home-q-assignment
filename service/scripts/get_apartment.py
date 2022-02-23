import sys

import requests


def get_apartment(id: str = "") -> None:
    url = "http://localhost:8000/apartments/"
    if id:
        url += f"{id}/"

    response = requests.get(url)

    print(response.content.decode(response.encoding or response.apparent_encoding))


if __name__ == "__main__":
    get_apartment(sys.argv[1] if len(sys.argv) >= 2 else "")
