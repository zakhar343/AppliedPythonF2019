from collections import namedtuple
import requests
from requests_toolbelt.utils.dump import dump_all
import datetime
Urls = namedtuple('Urls', ['method', 'url', 'headers', 'json', 'data'])

with open('request_dumps.txt', 'w') as f:
    test_data = [
        Urls('get', 'http://localhost:5000/flights', None, None, None),
        Urls('post', 'http://localhost:5000/flights', None, {
            'departure': str(datetime.datetime(2019, 10, 23, 10, 00)),
            'arrival': str(datetime.datetime(2019, 10, 23, 12, 00)),
            'time_in_flight': '2:00',
            'airport': 'SVO',
            'aircraft_type': 'AN28'
        }, None),
        Urls('post', 'http://localhost:8000/registration', None, {
            "username": "zakhar",
            "password": "zakhar",
            "password_conf": "zakhar1",
            "email": "zakhar343@yandex.ru"
        }, None),
        Urls('post', 'http://localhost:8000/registration', None, {
            "username": "zakhar",
            "password": "zakhar",
            "password_conf": "zakhar",
            "email": "zakhar343"
        }, None),
        Urls('post', 'http://localhost:8000/registration', None, {
            "username": "zakhar",
            "password": "zakhar",
            "password_conf": "zakhar",
            "email": "zakhar343@yandex.ru"
        }, None),
        Urls('post', 'http://localhost:8000/registration', None, {
            "username": "zakhar",
            "password": "zakhar123",
            "password_conf": "zakhar123",
            "email": "zakhar123@yandex.ru"
        }, None),
        Urls('post', 'http://localhost:8000/login', None, {
            "username": "zakhar",
            "password": "zakhar1"
        }, None),
        Urls('post', 'http://localhost:8000/login', None, {
            "username": "zakhar",
            "password": "zakhar"
        }, None),
        Urls('post', 'http://localhost:5000/flights', None, {
            'departure': str(datetime.datetime(2019, 10, 23, 10, 00)),
            'arrival': str(datetime.datetime(2019, 10, 23, 12, 00)),
            'time_in_flight': '2:00',
            'airport': 'SVO',
            'aircraft_type': 'AN28'
        }, None),
        Urls('post', 'http://localhost:5000/flights', None, {
            'departure': str(datetime.datetime(2019, 10, 23, 10, 00)),
            'arrival': str(datetime.datetime(2019, 10, 23, 12, 00)),
            'time_in_flight': '1:00',
            'airport': 'SVO',
            'aircraft_type': 'AN28'
        }, None),
        Urls('post', 'http://localhost:5000/flights', None, {
            'departure': str(datetime.datetime(2019, 10, 23, 12, 00)),
            'arrival': str(datetime.datetime(2019, 10, 23, 10, 00)),
            'time_in_flight': '2:00',
            'airport': 'SVO',
            'aircraft_type': 'AN28'
        }, None),
        Urls('post', 'http://localhost:5000/flights', None, {
            'departure': str(datetime.datetime(2019, 10, 23, 10, 00)),
            'arrival': str(datetime.datetime(2019, 10, 23, 12, 00)),
            'time_in_flight': '2:00',
            'airport': 'SV',
            'aircraft_type': 'AN28'
        }, None),
        Urls('post', 'http://localhost:5000/flights', None, {
            'departure': str(datetime.datetime(2019, 10, 24, 10, 00)),
            'arrival': str(datetime.datetime(2019, 10, 24, 14, 25)),
            'time_in_flight': '4:25',
            'airport': 'DMD',
            'aircraft_type': 'SU100'
        }, None),
        Urls('get', 'http://localhost:5000/flights', None, None, None),
        Urls('put', 'http://localhost:5000/flights/2', None, {
            'departure': str(datetime.datetime(2019, 10, 23, 10, 00)),
            'arrival': str(datetime.datetime(2019, 10, 23, 12, 00)),
            'time_in_flight': '2:00',
            'airport': 'DMD',
            'aircraft_type': 'AN28'
        }, None),
        Urls('put', 'http://localhost:5000/flights/3', None, {
            'departure': str(datetime.datetime(2019, 10, 23, 10, 00)),
            'arrival': str(datetime.datetime(2019, 10, 23, 12, 00)),
            'time_in_flight': '2:00',
            'airport': 'DMD',
            'aircraft_type': 'AN28'
        }, None),
        Urls('put', 'http://localhost:5000/flights/2', None, {
            'departure': str(datetime.datetime(2019, 10, 24, 10, 00)),
            'arrival': str(datetime.datetime(2019, 10, 24, 14, 25)),
            'time_in_flight': '4:25',
            'airport': 'SVO',
            'aircraft_type': 'SU104'
        }, None),
        Urls('delete', 'http://localhost:5000/flights/3', None, None, None),
        Urls('post', 'http://localhost:5000/flights', None, {
            'departure': str(datetime.datetime(2019, 10, 25, 10, 00)),
            'arrival': str(datetime.datetime(2019, 10, 25, 13, 00)),
            'time_in_flight': '3:00',
            'airport': 'DIA',
            'aircraft_type': 'A320'
        }, None),
        Urls('get', 'http://localhost:5000/logout', None, None, None),
        Urls('get', 'http://localhost:5000/flights?filter_by_airport=DMD', None, None, None),
        Urls('get', 'http://localhost:5000/flights?sort_by=arrival', None, None, None),
        Urls('delete', 'http://localhost:5000/flights/2', None, None, None),
        Urls('get', 'http://localhost:5000/flights', None, None, None),
        Urls('get', 'http://localhost:5000/show_performance', None, None, None),
    ]
    lu = len(test_data)
    header = dict()
    for index, url in enumerate(test_data):
        resp = requests.request(method=url.method, url=url.url, headers=header, json=url.json, data=url.data)
        if 'Set-Cookie' in resp.headers:
            header['Cookie'] = resp.headers['Set-Cookie']
        print(index, url, resp.status_code, resp.ok, file=f)
        print(dump_all(resp).decode('utf-8'), file=f)
