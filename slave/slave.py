
import json
import os
import re

from flask import (
    Flask,
    request, 
    #redirect, 
    #url_for, 
    #make_response, 
    #jsonify
) 
#from flask_sqlalchemy import SQLAlchemy
#from sqlalchemy.dialects.postgresql import insert
import requests
from bs4 import BeautifulSoup
#import asyncio
#import aiohttp


# ----------------------------------------------------------


app = Flask(__name__)


# ----------------------------------------------------------


def get_data(url: str):
    resp = requests.get(url)
    words = {}
    if (resp.status_code == 200):
        soup1 = BeautifulSoup(resp.text, 'html.parser')
        soup2 = soup1.find('body')
        match_list = re.findall(r'[А-Яа-я]{3,30}', soup2.text.lower(), re.I)

        for item in match_list:
            if (item in words):
                words[item] += 1
            else:
                words[item] = 1
    return words


# ----------------------------------------------------------


'''
@app.route('/test', methods=['GET'])
def test():
  return make_response(jsonify({'message': 'test route'}), 200)


@app.route('/', methods=['GET'])
def index():
    return 'Im slave'
'''


@app.route('/')
def slave_info():
    return 'Hello, I am slave-container!'


@app.route('/slave/run', methods=['POST'])
def slave_run():
    json_data = request.get_json()
    url_list = []
    url_list.append(json.loads(json_data))
    words = get_data(url_list[0])
    return json.dumps(words, indent = 4, ensure_ascii=False)




if __name__ == "__main__":
    app.run()
