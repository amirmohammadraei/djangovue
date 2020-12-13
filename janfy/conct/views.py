from django.shortcuts import render, HttpResponse
from requests.auth import HTTPBasicAuth
import requests
import random
import json


def tess(request):
    context = {"token": "new"}

    return


def call_api(request):
    count = 1
    array = []
    while True:
        try:
            url = 'http://192.168.5.10:1080/api/persons/?page=' + str(count)
            r = requests.get(url, auth=HTTPBasicAuth('admin', '$et@reyeSohe!1a'))
            array.append(r.json())
            var = r.json()['results']
            count += 1
        except KeyError:
            break

    # print(array[0]['results'][0])
    vu = array[2]['results'][9]
    print(vu)
    return HttpResponse(array)


def index(request):
    names = ("bob", "dan", "jack", "lizzy", "susan")

    items = []
    for i in range(100):
        items.append({
            "name": random.choice(names),
            "age": random.randint(20, 80),
            "url": "https://example.com",
        })

    context = {}
    context["items_json"] = json.dumps(items)
    # print(context)

    return render(request, 'list.html', context)
