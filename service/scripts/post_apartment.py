import requests


def post_apartment() -> None:
    apartment = {
        "city": "Helm's Deep",
        "street": "Helm's Dike",
        "street_number": "1",
        "rooms": 8,
        "floor": 0,
        "area": 4000,
        "rent": 10000,
        "latitude": 3.14,
        "longitude": 42.0,
    }
    response = requests.post(url="http://localhost:8000/apartments/", json=apartment)
    print(response.content.decode(response.encoding or response.apparent_encoding))


if __name__ == "__main__":
    post_apartment()
