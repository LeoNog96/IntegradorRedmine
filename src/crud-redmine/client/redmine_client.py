import requests
from settings import settings
import json

headers = {
    'Content-Type': "application/json",
    'Authorization': "Basic {}".format(settings.REDMINE_TOKEN),
    'Cache-Control': "no-cache",       
}

def get (id):

    url = '{}issues/{}.json'.format(settings.REDMINE_URL, id)

    response = requests.request("GET", url, headers=headers)

    return response

def post (obj):

    url = "{}issues.json".format(settings.REDMINE_URL)

    response = requests.request("POST", url, json=obj, headers=headers)

    return response

def put (id, obj):

    url = '{}issues/{}.json'.format(settings.REDMINE_URL, id)

    response = requests.request("PUT", url,json=obj, headers=headers)

    return response

def delete (id):

    url = '{}issues/{}.json'.format(settings.REDMINE_URL, id)

    response = requests.request("DELETE", url, headers=headers)

    return response