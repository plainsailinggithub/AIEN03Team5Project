from django.shortcuts import render
from django.http import HttpResponse
from .models import Economist
import requests
import time
from bs4 import BeautifulSoup
import re


# Create your views here.
def index(request):
    Economist.objects.all().delete()
    scraping()
    return render(request, 'Sophia/index.html', locals())

def scraping():
    url = "https://www.cw.com.tw/search/doSearch.action?getSort=&channel=ch16&key=%E8%96%AA%E6%B0%B4"

    headers_data = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
    }

    response = requests.get(url, headers=headers_data)
    response.encoding = "utf-8"
    soup = BeautifulSoup(response.text, "lxml")

    a = soup.select("div.articleGroup section h3 a")
    for url in a:
        c = url["href"]
        x = url.text
        title = re.sub(r'經濟學人', '', x).strip()

        datas = {
        "title":title,
        "url":c,
        }
        Economist.objects.create(**datas)

        # print(title)
        # print(c)