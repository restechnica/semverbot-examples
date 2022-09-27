from requests import get

def get_my_ip()->str:
    response = get("https://api.ipify.org?format=json").json()
    return response.get("ip")


if __name__ == "__main__":
    print(get_my_ip())