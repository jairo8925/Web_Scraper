import requests


def get_quote(url):
    r = requests.get(url)
    quote = r.json().get('content')
    return quote if quote else "Invalid quote resource!"


user_input = input()
print(get_quote(user_input))
