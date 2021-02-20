import base64
import json
import os

import requests


GITHUB_TOKEN = os.environ.get('GITHUB_TOKEN')


def main():
    api_url = 'https://api.github.com/repos/'
    old_name = os.environ.get('GITHUB_REPOSITORY')
    j = requests.get(api_url+old_name).json()
    stars = j.get('stargazers_count')
    new_name = f"This-Repo-Has-{stars}-Star{'s' if stars != 1 else ''}"
    print(old_name, stars, new_name)
    headers = {'Authorization': f"Bearer {GITHUB_TOKEN}"}
    data = {'name': new_name}
    repository_url = 'https://api.github.com/repos/'+ old_name
    response = requests.patch(repository_url, headers=headers, json=data)

main()
