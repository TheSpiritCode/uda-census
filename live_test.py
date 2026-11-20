import sys

import requests

BASE_URL = "https://uda-census.fastapicloud.dev/"


def main() -> int:
    url = f"{BASE_URL}/predict"
    try:
        response = requests.post(
            url,
            json={
                "csv_data": [
                    {
                        "age": 39,
                        "workclass": "State-gov",
                        "fnlgt": 77516,
                        "education": "Bachelors",
                        "education-num": 13,
                        "occupation": "Adm-clerical",
                        "hours-per-week": 40,
                        "native-country": "United-States",
                        "race": "white",
                        "sex": "male",
                    }
                ]
            },
            timeout=60,  # free-tier hosts can take a while to wake up
        )
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
        return 1

    print(f"Status code: {response.status_code}")

    try:
        body = response.json()
    except ValueError:
        print(f"Non-JSON response: {response.text}")
        return 1

    if response.ok:
        print(f"Model inference result: {body['predictions']}")
        return 0

    print(f"Error response: {body}")
    return 1


if __name__ == "__main__":
    sys.exit(main())
