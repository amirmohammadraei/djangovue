from django.shortcuts import render, HttpResponse
from requests.auth import HTTPBasicAuth
import requests

def tess(request):
    context={"token":"new"}

    return


def call_api(request):
    count = 1
    array = []
    loop = 0
    while loop == 0:
        try:
            url = '' + str(count)
            r = requests.get(url, auth=HTTPBasicAuth('username', 'password'))
            array.append(r.json())
            r.json()['results']
            count += 1
        except KeyError:
            loop = 1

    print(array[3])
    return HttpResponse(array)
