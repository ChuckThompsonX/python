import requests
from pprint import pprint

def api_call():
    try:
        # make API call
        resp = requests.get('https://jsonplaceholder.typicode.com/posts')

        if resp.status_code == 200:
            # retrieve json data
            data = resp.json()
            return data
        else:
            print('Error:', resp.status_code)
            return None
    except requests.exceptions.RequestException as e:
        print('Error:', e)
        return None

if __name__ == '__main__':
    # display json data
    data = api_call()
    pprint(data)
