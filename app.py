import requests
from flask import Flask, request
from bs4 import BeautifulSoup

app = Flask(__name__)

#HTTP GET at root path
@app.route('/')
def home():
    return
