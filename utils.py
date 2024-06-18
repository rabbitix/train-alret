import logging
from json import JSONDecodeError


def send_message_to_user(user_id):
    token = "<BOT_TOKEN_HERE>"

    import requests

    url = "https://curl_msg-1-d5167660.deta.app/send"
    headers = {
        "accept": "application/json",
        "Content-Type": "application/json"
    }
    data = {
        "token": f"{token}",
        "channel_id": f"{user_id}",
        "text": "there are some available trains🥳"
    }

    response = requests.post(url, headers=headers, json=data, verify=False)

    print(response.json())


def raja_trains(query) -> bool:
    import requests

    url = f"https://hostservice.raja.ir/Api/ServiceProvider/TrainListEq?q={query}"
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:126.0) Gecko/20100101 Firefox/126.0",
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "en-US,en;q=0.5",
        "Content-Type": "application/json",
        "api-key": "sDSLk2rGId8L0jUz7N2vQK02vkGPf3DgqB0Yi9oqgI9yH3xWqxewCFOxdCmpMjbOROGTPMg162oK40pvX1asop23b0m2MNIulmNUxjwS2Vuq4opmBS4kVuHJUdSf60bJ",
        "Authorization": "",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-site"
    }

    response = requests.get(url, headers=headers, verify=False)
    print(response.status_code)
    try:
        data = response.json()
        if len(data.get("GoTrains", [])):
            return True
        return False
    except JSONDecodeError:
        print(response.content.decode('utf-8'))
        return False


def check_mr_bilit(data: str) -> bool:
    import requests
    url = "https://train.atighgasht.com/TrainService/api/GetAvailable/v2"
    params = {
        "from": 1,
        "to": 167,
        "date": data,
        "adultCount": 4,
        "childCount": 0,
        "infantCount": 0,
        "exclusive": "false",
        "availableStatus": "Both",
        "genderCode": 3
    }
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:126.0) Gecko/20100101 Firefox/126.0",
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "en-US,en;q=0.5",
        "X-PlayerID": "faa31cf2-9d83-4f01-bb5a-6859cf55d20c",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "cross-site",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJidXMiOiI0ZiIsInRybiI6IjE3Iiwic3JjIjoiMiJ9.vvpr9fgASvk7B7I4KQKCz-SaCmoErab_p3csIvULG1w"
    }

    response = requests.get(url, params=params, headers=headers)

    logging.info(f"called mr bilit with response {response.status_code}")
    try:
        data = response.json()
        if len(data.get("Trains", [])):
            return True

        logging.info(f"no train available")
        return False
    except JSONDecodeError:
        logging.info(response.content.decode('utf-8'))
        return False
