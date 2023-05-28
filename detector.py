import requests

def detect():
    door = requests.get('https://pyexer-13801-default-rtdb.firebaseio.com/.json')
    return door